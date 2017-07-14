/* eslint no-alert: 0 */

'use strict';

var app = angular.module('PlantApp', [
    'ngRoute',
    'PlantApp.controllers'
]);

app.run(function ($http, $rootScope, $window, $location, $route) {
    console.log('App Running');
});

angular.module('PlantApp.controllers', []);

// this allows our ajax requests to work with django by providing the security token
app.config(['$httpProvider', function ($httpProvider) {
    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
}]);

// app.config(function ($routeProvider) {
//     $routeProvider.when('/', {
//         templateUrl: 'views/calendar.html',
//         reloadOnSearch: false,
//         controller: 'plantHome'
//     });
// });

angular.module('PlantApp.controllers').controller('plantHome', function ($scope, $http) {
    console.log('Plant Home Init');

    $scope.angular_test_two = 'SUCCESSFUL';

    $scope.testAngular = function(){
        console.log('TEST SUCCESSFUL');
    }
});
