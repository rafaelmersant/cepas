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
    .controller('HomePageCtrl', ['$scope', '$filter', '$window', 'HomePageService', 
                                  function ($scope, $filter, $window, HomePageService) {

      $scope.saludoHome = function() {
        alert('SALUDO');
        console.log('hola');
      }

      $scope.GetDigitadores = function() {
        HomePageService.getDigitadores().then(function (data) {
          if($window.LocalStorage['modificadosCEPAS'] == undefined) {
            $window.LocalStorage['modificadosCEPAS'] = JSON.stringify(data);
          } else {
            var dataLocal = JSON.parse($window.LocalStorage['modificadosCEPAS']);
            console.log(dataLocal);
          }

          $scope.registros = data;
          console.log(data);
        });
      }

      $scope.GetDigitadoresCreados = function() {
        HomePageService.getDigitadoresCreados().then(function (data) {
          $scope.registrosCreados = data;
        });
      }

    }]);

})(_);