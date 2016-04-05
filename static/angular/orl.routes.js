(function() {
    'use strict';
    
    angular
        .module('orl.routes')
        .config(function($routeProvider) {
            $routeProvider
                .when('/login', {
                    controller: 'LoginController',
                    controllerAs: 'vm',
                    templateUrl: 'static/templates/authentication/login.html'
                })
                .when('/register', {
                    controller: 'RegisterController',
                    controllerAs: 'vm',
                    templateUrl: 'static/templates/authentication/register.html'
                })
                .otherwise('/');
        });
})();