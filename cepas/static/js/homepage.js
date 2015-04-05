(function (_) {

  angular.module('cepas.homepage', ['ngAnimate'])
    
    .factory('HomePageService', ['$http', '$q', '$filter', function ($http, $q, $filter) {

      function homepage() {
        return false;
      }

      return {
        homepage: homepage
      };

    }])

    //****************************************************
    //                                                   *
    //CONTROLLERS                                        *
    //                                                   *
    //****************************************************
    .controller('HomePageCtrl', ['$scope', '$filter', 'HomePageService', function ($scope, $filter, HomePageService) {

      $scope.saludoHome = function() {
        alert('SALUDO');
        console.log('hola');
      }


    }]);

})(_);