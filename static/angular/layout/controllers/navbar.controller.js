(function() {
    'use strict';
    
    angular
        .module('orl.layout.controllers')
        .controller('NavbarCtrl', function() { // Don't forget to add Authentication service dependency when it's done...
            var vm = this;
            
            vm.accountOptions = false;
            
            /**
             * Log the user out
             */
            vm.logout = function() {
                // To do...
            };
            
            /**
             * Tooggles vm.accountOptions to show/hide the user options menu
             */
            vm.toggleAccountOptions = function() {
                vm.accountOptions = vm.accountOptions === false ? true : false;
            }
        });
})();