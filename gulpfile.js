'use strict';

// Gulp
// ----
var gulp = require('gulp');

// Importing Gulp dependencies
// ---------------------------
var del = require('del');
var Server = require('karma').Server;
var ngAnnotate = require('gulp-ng-annotate');
var templateCache = require('gulp-angular-templatecache');
var uglify = require('gulp-uglify');
var livereload = require('gulp-livereload');
var fs = require('fs');

// Common paths
// ------------
var angularWithoutTest = ['static/angular/**/*', '!static/angular/tests/**/*'];
var templatesSrc = ['static/templates/**/*'];
var templatesAndAssetsFiles = ['static/assets/**/*', 'templates/**/*'];

// Developpement tasks
// -------------------

/** 
 * To use the developpement tasks, just put the `gulp` command line
 * and enjoy the automatic tasks!
 */

/**
 * Annotate Angular files
 */
gulp.task('annotate', function() {
    gulp
        .src(angularWithoutTest)
        .pipe(ngAnnotate({
            remove: true,
            add: true,
            single_quotes: true
        }))
        .pipe(gulp.dest('static/angular-annotated/'))
        .pipe(livereload());
});

/**
 * Concatenates and registers Angular templates in the $templateCache
 */
gulp.task('templateCache', function() {
    return gulp
        .src(templatesSrc)
        .pipe(templateCache('orl.templates.js', {
            module: 'orl.templates',
        }))
        .pipe(gulp.dest('static/angular/'))
        .pipe(livereload());
});

/**
 * Reloads browser when these files changed.
 */
gulp.task('livereload', function() {
    gulp
        .src(templatesAndAssetsFiles)
        .pipe(livereload());
});

/**
 * Watching files
 */
gulp.task('watch', function() {
    livereload.listen();
    gulp.watch(angularWithoutTest, ['annotate']);
    gulp.watch(templatesSrc, ['templateCache']);
    gulp.watch(templatesAndAssetsFiles, ['livereload']);
});

/**
 * Watch for file changes and re-run tests on each change
 */
gulp.task('tdd', function(done) {
    new Server({
        configFile: __dirname + '/karma.conf.js'
    }, done).start();
});

/**
 * Run test once and exit
 */
gulp.task('test', function(done) {
    new Server({
        configFile: __dirname + '/karma.conf.js',
        singleRun: true
    }, done).start();
});

gulp.task('default', [
    'tdd',
    'watch',
]);

// Production task
// ---------------

/**
 * To use the production tasks, make sure you exited gulp.
 * First of all, you have to clean the project with the `gulp del`
 * command line.
 */
gulp.task('del', function() {
    del('static/angular-annotated/tests');
});

/**
 * Then, put the `gulp prod` command line to launch these tasks
 */
gulp.task('prod', function() {
    gulp.src('static/angular-annotated/**/*')
        .pipe(uglify())
        .pipe(gulp.dest('static/assets/js'));
});