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
            'test/**/*.js'
        ]
    })
}