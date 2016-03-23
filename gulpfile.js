'use strict';

// Gulp
// ----
var gulp = require('gulp');

// Importing Gulp dependencies
// ---------------------------
var Server = require('karma').Server;
var ngAnnotate = require('gulp-ng-annotate');
var templateCache = require('gulp-angular-templatecache');
var uglify = require('gulp-uglify');

// Common paths
// ------------
var angularWithoutTest = ['./angular/**/*.js', '!./angular/tests/**/*.js'];
var templatesSrc = ['./angular/templates/*.html'];

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
            add: true,
            single_quotes: true
        }))
        .pipe(gulp.dest('./angular/'));
});

/**
 * Concatenates and registers Angular templates in the $templateCache
 */
gulp.task('templateCache', function() {
    gulp
        .src(templatesSrc)
        .pipe(templateCache())
        .pipe(gulp.dest('./angular/templateCaches.js'));
});

/**
 * Watching files
 */
gulp.task('watch', function() {
    gulp.watch(angularWithoutTest, ['annotate']);
    gulp.watch(templatesSrc, ['templateCache']);
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
    'watch'
]);


// Production task
// ---------------

/**
 * To use the production tasks, make sure you're exited gulp
 * then put the `gulp prod` command line to launch these tasks
 */
gulp.task('prod', function() {
    gulp.src(angularWithoutTest)
        .pipe(uglify())
        .pipe(gulp.dest('./prod/angular'));
});