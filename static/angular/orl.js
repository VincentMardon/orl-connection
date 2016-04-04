(function() {
    'use strict';
    
    angular
        .module('orl', [
            'orl.config',
            'orl.routes',
            'orl.templates',
            'orl.layout',
            'orl.authentication',
        ]);
    
    angular
        .module('orl.config', []);
    
    angular
        .module('orl.routes', ['ngRoute']);
    
    angular
        .module('orl.templates', []);
    
    angular
        .module('orl.layout', []);
    
    angular
        .module('orl.authentication', []);
    
    /**
     * desc Update xsrf $http headers to align with Django's defaults
     */
   angular
        .module('orl')
        .run(function($http) {
            $http.defaults.xsrfHeaderName = 'X-CSRFToken';
            $http.defaults.xsrfCookieName = 'csrftoken';
        });
})();