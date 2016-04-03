(function() {
    'use strict';
    
    angular
        .module('orl.routes')
        .config(function($routeProvider) {
            $routeProvider
                .when('/login', {
                    controller: 'LoginCtrl',
                    controllerAs: 'vm',
                    templateUrl: 'static/templates/authentication/login.html'
                })
                .when('/register', {
                    controller: 'RegisterCtrl',
                    controllerAs: 'vm',
                    templateUrl: 'static/templates/authentication/register.html'
                })
                .otherwise('/');
        });
})();