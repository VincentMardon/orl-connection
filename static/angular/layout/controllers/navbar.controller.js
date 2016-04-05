/**
 * NavbarCtrl
 * @namespace orl.layout.controllers
 */
(function() {
    'use strict';
    
    angular
        .module('orl.layout.controllers')
        
        /**
         * @namespace NavbarController
         */
        .controller('NavbarController', function(Authentication) {
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
             * @name toggleAccountOptions
             * @desc Tooggles vm.accountOptions to show/hide the user options menu
             * @memberOf orl.layout.controllers.NavbarController
             */
            vm.toggleAccountOptions = function() {
                vm.accountOptions = vm.accountOptions === false ? true : false;
            }
        });
})();