(function() {
    'use strict';
    
    /**
     * @desc Enable HTML5 routing
     */
    angular
        .module('orl.config')
        .config(function($locationProvider) {
            $locationProvider.html5Mode(true);
            $locationProvider.hashPrefix('!');
        });
})();