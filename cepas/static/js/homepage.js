(function (_) {

  angular.module('cepas.homepage', ['ngAnimate'])
    
    .factory('HomePageService', ['$http', '$q', '$filter', function ($http, $q, $filter) {

      function homepage() {
        return false;
      }

      function getDigitadores() {
        var deferred = $q.defer();

        $http.get('/administracion/digitadores-modificados/')
          .success(function (data) {
            deferred.resolve(data);
          });
        return deferred.promise;
      }

      function getDigitadoresCreados() {
        var deferred = $q.defer();

        $http.get('/administracion/digitadores-creados/')
          .success(function (data) {
            deferred.resolve(data);
          });
        return deferred.promise;
      }

      return {
        homepage: homepage,
        getDigitadores: getDigitadores,
        getDigitadoresCreados: getDigitadoresCreados
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

      $scope.GetDigitadores = function() {
        HomePageService.getDigitadores().then(function (data) {
          $scope.registros = data;
        });
      }

      $scope.GetDigitadoresCreados = function() {
        HomePageService.getDigitadoresCreados().then(function (data) {
          $scope.registrosCreados = data;
        });
      }

    }]);

})(_);