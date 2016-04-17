/**
 * NavbarController
 * @namespace orl.layout.controllers
 */
(function() {
    'use strict';
    
    angular
        .module('orl.layout.controllers')
        
        /**
         * @namespace NavbarController
         */
        .controller('NavbarController', function($timeout, Authentication) {
            var vm = this;
            
            vm.accountOptions = false;
            
            vm.logout = logout;
            vm.checkAccountOptions = checkAccountOptions;
            vm.toggleAccountOptions = toggleAccountOptions
            
            ////////////////////////////////////
            
            /**
             * @name logout
             * @desc Log the user out
             * @memberOf orl.layout.controllers.NavbarController
             */
            function logout() {
                Authentication.logout();
            };
            
            /**
             * @name checkAccountOptions
             * @desc Call vm.toggleAccountOptions if vm.accountOptions is true
             * @memberOf orl.layout.controllers.NavbarController
             */
            function checkAccountOptions() {
                if (vm.accountOptions) {
                    vm.toggleAccountOptions();
                }
            }
            
            /**
             * @name toggleAccountOptions
             * @desc Tooggles vm.accountOptions to show/hide the user options menu
             * @memberOf orl.layout.controllers.NavbarController
             */
            function toggleAccountOptions() {
                $timeout(function() {
                    vm.accountOptions = vm.accountOptions === false ? true : false;
                }, 200);
            }
        });
})();