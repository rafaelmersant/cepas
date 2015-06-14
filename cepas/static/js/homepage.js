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
          if($window.localStorage['modificadosCEPAS'] == undefined) {
            $window.localStorage['modificadosCEPAS'] = JSON.stringify(data);
          } else {
            var dataLocal = JSON.parse($window.localStorage['modificadosCEPAS']);
            var i = 0;
            data.forEach(function (item) {
              if(item.cantidad != dataLocal[i].cantidad & item.username == dataLocal[i].username & item.titulo_conciliar == dataLocal[i].titulo_conciliar) {
                dataLocal[i].cantidad = dataLocal[i].cantidad + '+';
                i = i + 1;
              }
            })
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