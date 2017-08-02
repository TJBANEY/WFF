angular.module('PlantApp.controllers').controller('plantHome', function ($window, $route, $rootScope, $location, $scope, $http) {
    console.log('Plant Home Init');

    $scope.explorePlants = function(){
      console.log('Exploring');
    };

    $window.plant_events = [
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
            color: '#13d640',
            textColor: '#fff'
        }
    ]
});
