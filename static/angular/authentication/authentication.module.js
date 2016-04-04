(function() {
    'use strict';
    
    angular
        .module('orl.authentication', [
            'orl.authentication.controllers',
            'orl.authentication.services',
        ]);
    
    angular
        .module('orl.authentication.controllers', []);
    
    angular
        .module('orl.authentication.services', ['ngCookies']);
})();