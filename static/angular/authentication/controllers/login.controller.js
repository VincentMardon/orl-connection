/**
 * LoginController
 * @namespace orl.autentication.controllers
 */
(function() {
    'use strict';
    
    angular
        .module('orl.authentication.controllers')
        
        /**
         * @namespace LoginController
         */
        .controller('LoginController', function($location, $templateCache, Authentication) {
            var vm = this;
            
            vm.login = login;
            
            activate();
            
            /**
             * @name activate
             * @desc Actions to be performed when this controller is instantiated
             * @memberOf orl.authentication.controllers.LoginController
             */
            function activate() {
                // If the user is authenticated, they should not be here.
                if (Authentication.isAuthenticated()) {
                    $location.url('/');
                }
            }
            
            /**
             * @name login
             * @desc Log the user in
             * @memberOf orl.authentication.controllers.LoginController
             */
            function login() {
                Authentication.login(vm.email, vm.password);
            }
        });
})();