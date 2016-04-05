(function() {
    'use strict';
    
    angular
        .module('orl.layout', [
            'orl.layout.controllers',
            'orl.layout.services'
        ]);
    
    angular
        .module('orl.layout.controllers', ['ngMessages']);
    
    angular
        .module('orl.layout.services', []);
})();