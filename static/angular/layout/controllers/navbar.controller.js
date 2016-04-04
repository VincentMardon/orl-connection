/**
 * NavbarCtrl
 * @namespace orl.layout.controllers
 */
(function() {
    'use strict';
    
    angular
        .module('orl.layout.controllers')
        
        /**
         * @namespace NavbarCtrl
         */
        .controller('NavbarCtrl', function(Authentication) {
            var vm = this;
            
            vm.accountOptions = false;
            
            /**
             * @name logout
             * @desc Log the user out
             * @memberOf orl.layout.controllers.NavbarCtrl
             */
            vm.logout = function() {
                Authentication.logout();
            };
            
            /**
             * @name toggleAccountOptions
             * @desc Tooggles vm.accountOptions to show/hide the user options menu
             * @memberOf orl.layout.controllers.NavbarCtrl
             */
            vm.toggleAccountOptions = function() {
                vm.accountOptions = vm.accountOptions === false ? true : false;
            }
        });
})();