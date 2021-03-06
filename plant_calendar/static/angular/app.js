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
    $scope.currentStep = 1;

    $scope.submitGrowZone = function (currentStep) {
        switch(currentStep){
            case 1:
                console.log('Grow Zone Submitted');
                $scope.currentStep = 2;
                break;

            case 2:
                console.log('Crop Submitted');
                $scope.currentStep = 3;
                break;

            case 3:
                console.log('Planting per Season selected');
                // Redirect them somewhere
                break;
        }
    }

    // var filters = {
    //     harvest_start: '',
    //     harvest_end: ''
    // };
    //
    // $scope.filters = angular.copy(filters);
    //
    // $scope.testAngular = function () {
    //     console.log('TEST SUCCESSFUL');
    // };
    //
    // $scope.explorePlants = function (filters) {
    //     console.log(filters);
    //
    //     $http({
    //         method: 'GET',
    //         url: '/api/v1/plants/filtered_plants?name=tomato&harvest_start=' + filters.harvest_start
    //     }).then(function success(response) {
    //         console.log(response);
    //         $scope.plants = response.data
    //     }, function error(response) {
    //         console.log('Error')
    //     });
    //
    // };
    //
    // $scope.plant_events = [
    //     {
    //         title: 'Prune Grapevines',
    //         start: '2017-07-18',
    //         end: '2017-07-21',
    //         color: '#1bc974',
    //         textColor: '#fff'
    //     },
    //     {
    //         title: 'Plant Tomato',
    //         start: '2017-07-10',
    //         end: '2017-07-12',
    //         textColor: '#fff'
    //     }
    // ];
    //
    // $scope.retrievePlants = function () {
    //     $http({
    //         method: 'GET',
    //         url: '/api/v1/plants/?name=tomato'
    //     }).then(function success(response) {
    //         // console.log(response.data.results);
    //         $scope.plants = response.data.results;
    //     }, function error(response) {
    //         console.log('Error')
    //     });
    // };
    // $scope.retrievePlants();
    //
    // $scope.plants = [1, 2, 3, 4]
});
