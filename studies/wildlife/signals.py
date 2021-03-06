from django.db.models.signals import pre_save
from django.dispatch import receiver

from data_import.signal_helpers import task_signal_pre_save_cb

from . import label
from .models import UserData


@receiver(pre_save, sender=UserData)
def pre_save_cb(instance, **kwargs):
    """
    Create data retrieval task when Wild Life of Our Homes UserData's data is
    updated.
    """
    if not instance.data:
        return

    task_signal_pre_save_cb(instance=instance, source=label, **kwargs)
