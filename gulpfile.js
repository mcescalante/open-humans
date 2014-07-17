/*eslint-env node*/

'use strict';

var browserify = require('browserify');
var gulp = require('gulp');
var mainBowerFiles = require('main-bower-files');
var source = require('vinyl-source-stream');

var plugins = require('gulp-load-plugins')();

var paths = {
  js: './static/js/**.js',
  sass: './static/sass/**.sass',
  python: '**/*.py'
};

// Lint JavaScript code
gulp.task('lint-js', function () {
  return gulp.src(paths.js)
    .pipe(plugins.eslint())
    .pipe(plugins.eslint.format());
});

// Lint Python code
gulp.task('lint-python', function () {
  return gulp.src(paths.python)
    .pipe(plugins.shell([
      'flake8 <%= file.path %>',
      'pylint --reports=no <%= file.path %>'
    ]));
});

gulp.task('lint', ['lint-js', 'lint-python']);

// Ensure bower components are installed
gulp.task('bower-install', function () {
  return plugins.bower();
});

// Collect the main files of the installed bower components
gulp.task('bower', ['bower-install'], function () {
  return gulp.src(mainBowerFiles())
    .pipe(gulp.dest('./build/vendor'));
});

// Browserify, minify, create sourcemaps, bundle, and livereload
gulp.task('browserify', function () {
  return browserify('./static/js/index.js')
      .plugin('minifyify', {
        map: '/static/js/bundle.map.json',
        output: './build/js/bundle.map.json'
      })
      .bundle()
    .pipe(source('bundle.js'))
    .pipe(gulp.dest('./build/js'))
    .pipe(plugins.livereload());
});

// Compile sass files into CSS
gulp.task('sass', function () {
  return gulp.src(paths.sass)
    .pipe(plugins.sass())
    .pipe(gulp.dest('./build/css'))
    .pipe(plugins.livereload());
});

// Run browserify on JS changes, sass on sass changes
gulp.task('watch', function () {
  gulp.watch(paths.js, ['browserify']);
  gulp.watch(paths.sass, ['sass']);
});

gulp.task('default', ['bower', 'browserify', 'sass', 'watch']);
