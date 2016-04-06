(function(){angular.module("orl.templates").run(["$templateCache", function($templateCache) {$templateCache.put("static/templates/authentication","null");
$templateCache.put("static/templates/layout","null");
$templateCache.put("static/templates/authentication/login.html","<h1>Connexion</h1><br />\n\n<form name=\"login\" class=\"login-form\" role=\"form\" ng-submit=\"vm.login()\" novalidate>\n    <div class=\"form-group\">\n        <label for=\"login__email\">Email</label>\n        <input type=\"email\" name=\"email\" class=\"form-text\" id=\"login__email\" ng-model=\"vm.email\" ng-model-options=\"{ updateOn: blur }\" maxlength=\"320\" placeholder=\"ex. john@email.com\" required />\n        \n        <div ng-messages=\"login.email.$error\" role=\"alert\">\n            <div ng-message=\"required\" class=\"error-message\" ng-show=\"login.email.$touched\">\n                Vous n\'avez pas saisi votre email.\n            </div>\n            \n            <div ng-message=\"email\" class=\"error-message\" ng-show=\"login.email.$touched\">\n                L\'email que vous avez saisi est invalide.\n            </div>\n        </div>\n    </div>\n    \n    <div class=\"form-group\">\n        <label for=\"login__password\">\n            Mot de passe\n            <input type=\"password\" name=\"password\" class=\"form-text\" id=\"login__password\" ng-model=\"vm.password\" maxlength=\"100\" placeholder=\"ex. @Mot_2_Passe*\" required />\n        </label>\n        \n        <div ng-messages=\"login.password.$error\" alert=\"alert\" ng-show=\"login.password.$touched\">\n            <div ng-message=\"required\" class=\"error-message\">Vous n\'avez pas saisi votre mot de passe.</div>\n        </div>\n    </div><br />\n    \n    <div class=\"form-group\">\n        <button class=\"btn\" type=\"submit\" ng-disabled=\"login.email.$dirty && login.email.$invalid || login.password.$dirty && login.password.$invalid\">Me connecter</button>\n    </div>\n</form>");
$templateCache.put("static/templates/authentication/register.html","");
$templateCache.put("static/templates/layout/index.html","");}]);})();