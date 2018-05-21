import logging
import urllib.parse

import requests

from django.conf import settings
from raven.contrib.django.raven_compat.models import client

from common.utils import full_url
from open_humans.models import Member

from .utils import get_upload_dir

logger = logging.getLogger(__name__)


def task_params_for_source(user, source):
    """
    Return the task parameters for a given user and source. Called by
    data-processing after a task has been submitted.
    """
    user_data = getattr(user, source)

    if hasattr(user_data, 'refresh_from_db'):
        user_data.refresh_from_db()

    task_params = user_data.get_retrieval_params()

    task_params.update({
        'oh_user_id': user.id,
        'oh_username': user.username,
        's3_key_dir': get_upload_dir(source),
        's3_bucket_name': settings.AWS_STORAGE_BUCKET_NAME,
    })

    try:
        auth = user.social_auth.filter(provider=source).order_by('-id')[0]
    except IndexError:
        auth = None

    if auth:
        # Checks to avoid token invalidation by dev use of production data.
        # (a) ALLOW_TOKEN_REFRESH is true. (Should usually be false in dev.)
        # (b) Either we're in production, or there's less than 20 users.
        if (settings.ALLOW_TOKEN_REFRESH and
                (settings.ENV == 'production' or
                    Member.objects.count() < 20) and
                'refresh_token' in auth.extra_data and
                auth.extra_data['refresh_token']):
            backend = auth.get_backend_instance()
            token = backend.refresh_token(auth.extra_data['refresh_token'])

            auth.extra_data['access_token'] = token['access_token']
            auth.extra_data['refresh_token'] = token['refresh_token']
            auth.extra_data['expires'] = token['expires_in']

            auth.save()

            task_params['access_token'] = token['access_token']
        else:
            task_params['access_token'] = auth.extra_data['access_token']

    return task_params


def start_task(user, source, force=False):
    """
    Send a task to data-processing.
    """
    task_url = '{}/'.format(
        urllib.parse.urljoin(settings.DATA_PROCESSING_URL, source))

    try:
        task_req = requests.post(
            task_url,
            params={'key': settings.PRE_SHARED_KEY},
            json={
                'oh_user_id': user.id,
                'oh_base_url': full_url('/data-import/'),
                'force': force,
            })
    except requests.exceptions.RequestException:
        logger.error('Error in sending request to data processing')

        error_message = 'Error in call to Open Humans Data Processing.'

    if 'task_req' in locals() and not task_req.status_code == 200:
        logger.error('Non-200 response from data processing')

        error_message = 'Open Humans Data Processing not returning 200.'

    if 'error_message' in locals():
        if not settings.TESTING:
            client.captureMessage(error_message)

        return 'error'
