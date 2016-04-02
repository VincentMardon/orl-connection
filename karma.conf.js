module.exports = function(config) {
    config.set({
        frameworks: ['jasmine'],
        browsers: ['PhantomJS', 'PhantomJS_custom'],
        customLaunchers: {
            'PhantomJS_custom': {
                base: 'PhantomJS',
                options: {
                    windowName: 'test',
                    settings: {
                        webSecurityEnabled: false
                    },
                },
                flags: ['--load-images=true'],
                debug: true
            }
        },
        phantomJSLauncher: {
            exitOnResourceError: true
        },
        files: [
            'static/bower_components/angular/angular.min.js',
            'static/bower_components/angular-mocks/angular-mocks.js',
            'static/angular/tests/**/*.js'
        ]
    })
}