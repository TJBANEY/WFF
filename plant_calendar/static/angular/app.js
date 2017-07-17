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

angular.module('PlantApp.controllers').controller('plantHome', function ($window, $scope, $http) {
    console.log('Plant Home Init');

    $scope.angular_test_two = 'SUCCESSFUL';

    $scope.testAngular = function(){
        console.log('TEST SUCCESSFUL');
    };

    $scope.plant_events = [
        {
            title: 'Prune Grapevines',
            start: '2017-07-18',
            end: '2017-07-21',
            color: '#1bc974',
            textColor: '#fff'
        },
        {
            title: 'Plant Tomato',
            start: '2017-07-10',
            end: '2017-07-12',
            textColor: '#fff'
        }
    ]
});
