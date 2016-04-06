/**
 * Authentication
 * @namespace orl.authentication.services
 */
(function() {
    'use strict';
    
    angular
        .module('orl.authentication.services')
        
        /**
         * @namespace Authentication
         * @returns {Factory}
         */
        .factory('Authentication', function($cookies, $http) {
            /**
             * @name Authentication
             * @desc The factory to be returned
             */
            var Authentication = {
                getAuthenticatedAccount: getAuthenticatedAccount,
                isAuthenticated: isAuthenticated,
                login: login,
                logout: logout,
                register: register,
                setAuthenticatedAccount: setAuthenticatedAccount,
                unauthenticate: unauthenticate
            };
            
            return Authentication;
            
            //////////////////////
            
            /**
             * @name register
             * @desc Try to register a new user.
             * @param {string} username The username entered by the user.
             * @param {string} email The email entered by the user.
             * @param {string} year The year of birth entered by the user.
             * @param {string} month The month of birth entered by the user.
             * @param {string} day The day of birth entered by the user.
             * @param {string} password The password entered by the user.
             * @param {string} confirmPassword The password confirmation entered by the user.
             * @returns {Promise}
             * @memberOf orl.authentication.services.Authentication
             */
            function register(username, email, year, month, day, password, confirmPassword) {
                if (password !== confirmPassword) {
                    // awesome stuff...
                }
                
                return $http.post('/orl-rest-api/accounts/', {
                    username: username,
                    email: email,
                    date_of_birth: year + '-' + month + '-' + day,
                    password: password
                }).then(registerSuccessFn, registerErrorFn);
                
                /**
                 * @name registerSuccesFn
                 * @desc Log the new user in.
                 */
                function registerSuccessFn(data, status, headers, config) {
                    Authentication.login(email, password);
                }
                
                /**
                 * @name registerErrorFn
                 * @desc Log "Epic failure!" in the console.
                 */
                function registerErrorFn(data, status, headers, config) {
                    console.error('Epic failure!');
                }
            }
            
            /**
             * @name login
             * @desc Try to log in with email `email` and password `password`.
             * @param {string} email The email entered by the user.
             * @param {string} password The password entered by the user.
             * @returns {Promise}
             * @memberOf orl.authentication.services.Authentication
             */
            function login(email, password) {
                return $http.post('/orl-rest-api/auth/login/', {
                    email: email,
                    password: password,
                }).then(loginSuccessFn, loginErrorFn);
                
                /**
                 * @name loginSuccessFn 
                 * @desc Set the authenticated account and redirect to index
                 */
                function loginSuccessFn(data, status, headers, config) {
                    Authentication.setAuthenticatedAccount(data.data);
                    
                    window.location = '/';
                }
                
                /**
                 * @name loginErrorFn
                 * @desc Log "Epic failure!" to the console
                 */
                function loginErrorFn(data, status, headers, config) {
                    console.error('Epic failure!');
                    return data
                }
            }
            
            /**
             * @name logout
             * @desc Try to log out
             * @returns {Promise}
             * @memberOf orl.authentication.services.Authentication
             */
            function logout() {
                return $http.post('/orl-rest-api/auth/logout/')
                    .then(logoutSuccessFn, logoutErrorFn);
                
                /**
                 * @name logoutSuccessFn
                 * @desc Unauthenticate and redirect to index with page reload
                 */
                function logoutSuccessFn(data, status, headers, config) {
                    Authentication.unauthenticate();
                    
                    window.location = '/';
                }
                
                /**
                 * @name logoutErrorFn
                 * @desc Log "Epic failure!" to the console
                 */
                function logoutErrorFn(data, status, headers, config) {
                    console.error('Epic failure!');
                }
            }
            
            /**
             * @name getAuthenticatedAccount
             * @desc Return the currently authenticated account
             * @returns {object|undefined} Account if authenticated, else undefined
             * @memberOf orl.authentication.services.Authentication
             */
            function getAuthenticatedAccount() {
                if (!$cookies.get('authenticatedAccount')) {
                    return
                }
                
                return JSON.parse($cookies.get('authenticatedAccount'));
            }
            
            /**
             * @name isAuthenticated
             * @desc Check if the current user is authenticated
             * @return {boolean} True is the user is authenticated, else false
             * @memberOf orl.authentication.services.Authentication
             */
            function isAuthenticated() {
                return $cookies.get('authenticatedAccount') != undefined;
            }
            
            /**
             * @name setAuthenticatedAccount
             * @desc Stringify the account object and store it in a cookie
             * @return {undefined}
             * @memberOf orl.authentication.services.Authentication
             */
            function setAuthenticatedAccount(account) {
                $cookies.put('authenticatedAccount', JSON.stringify(account));
            }
            
            /**
             * @name unauthenticate
             * @desc Delete the cookie where the user object is stored
             * @return {undefined}
             * @memberOf orl.authentication.services.Authentication
             */
            function unauthenticate() {
                $cookies.remove('authenticatedAccount');
            }
        });
})();