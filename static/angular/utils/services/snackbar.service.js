/**
 * Snackbar
 * @namespace orl.utils.services
 */
(function($, _) {
    angular
        .module('orl.utils.services')
        
        /*
         * @namespace Snackbar
         */
        .factory('Snackbar', function() {
            var SnackBar = {
                error: error,
                show: show,
            };
            
            return Snackbar;
            
            ///////////////////////
            
            /**
             * @name = _snackbar
             * @desc Display a snackbar
             * @param {string} content The content of the snackbar
             * @param {Object} options Options for displaying the snackbar
             * @memberOf orl.utils.services.Snackbar
             */
            function _snackbar(content, options) {
                options = _.extend({timeout: 3000}, options);
                options.content = content;
                
                $.snackbar(options);
            }
            
            /**
             * @name error
             * @desc Display an error snackbar
             * @param {string} content The content of the snackbar
             * @param {Object} options Options for displaying the snackbar
             * @memberOf orl.utils.services.Snackbar
             */
            function error(content, options) {
                _snackbar('Erreur : ' + content, options);
            }
            
            /**
             * @name show
             * @desc Display a standard snackbar
             * @param {string} content The content of the snackbar
             * @param {Object} options Options for displaying the snackbar
             * @memberOf orl.utils.services.Snackbar
             */
            function show(content, options) {
                _snackbar(content, options)
            }
        });
})($, _);