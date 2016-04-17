(function() {
    'use strict';
    
    angular
        .module('orlApp', [
            'ngAria',
            'ngMessages',
            'orl.config',
            'orl.routes',
            'orl.templates',
            'orl.utils',
            'orl.layout',
            'orl.authentication',
        ]);
    
    angular
        .module('orl.config', []);
    
    angular
        .module('orl.routes', ['ngRoute']);
    
    angular
        .module('orl.templates', []);
    
    /**
     * desc Update xsrf $http headers to align with Django's defaults
     */
   angular
        .module('orlApp')
        .run(function($http) {
            $http.defaults.xsrfHeaderName = 'X-CSRFToken';
            $http.defaults.xsrfCookieName = 'csrftoken';
        });
})();