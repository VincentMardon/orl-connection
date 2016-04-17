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
            
            /**
             * @name logout
             * @desc Log the user out
             * @memberOf orl.layout.controllers.NavbarController
             */
            vm.logout = function() {
                Authentication.logout();
            };
            
            /**
             * @name checkAccountOptions
             * @desc Call vm.toggleAccountOptions if vm.accountOptions is true
             * @memberOf orl.layout.controllers.NavbarController
             */
            vm.checkAccountOptions = function() {
                if (vm.accountOptions) {
                    vm.toggleAccountOptions();
                }
            }
            
            /**
             * @name toggleAccountOptions
             * @desc Tooggles vm.accountOptions to show/hide the user options menu
             * @memberOf orl.layout.controllers.NavbarController
             */
            vm.toggleAccountOptions = function() {
                $timeout(function() {
                    vm.accountOptions = vm.accountOptions === false ? true : false;
                }, 200);
            }
        });
})();