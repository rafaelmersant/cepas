(function (_) {

  angular.module('cepas.miembros', ['ngAnimate'])
    
    .factory('MiembrosService', ['$http', '$q', '$filter', function ($http, $q, $filter) {

      function getMiembros(nombres, sociedad) {
        var deferred = $q.defer();

        url = '/api/miembros/buscar/nombre-apellido/{nombreApellido}/?format=json'.replace('{nombreApellido}', nombres);

        $http.get(url)
          .success(function (data) {

            console.log(sociedad)

            if (sociedad != '*') {
              data = data.filter(function (registros) {
                return registros.sociedad == sociedad;
              });
            }

console.log(data);
            if(data.length > 0) {
              deferred.resolve(data);
            } else {
              deferred.reject();
            }
            
          })
          .error(function (data) {
            deferred.resolve(data);
          });
          
        return deferred.promise;
      }

      return {
        getMiembros: getMiembros
      };

    }])

    //****************************************************
    //                                                   *
    //CONTROLLERS                                        *
    //                                                   *
    //****************************************************
    .controller('MiembrosCtrl', ['$scope', '$filter', 'MiembrosService', function ($scope, $filter, MiembrosService) {

      //Inicializar variables
      $scope.sociedad = '*';

      //Buscar miembro
      $scope.buscarMiembro = function($event) {
        $event.preventDefault();
        $scope.miembros = []; 

      	try {
          if($event.type == 'click' || $event.keyCode == 13) {
  	        MiembrosService.getMiembros($scope.nombres, $scope.sociedad).then(function (data) {

  	          $scope.miembros = data;
              console.log(data)
  	        },
            function (error) {
              alert('No se pudo encontrar lo que buscaba.-');
            });
          } 
      	} catch (e) {
      		alert(e);
      	}
      }

    }]);

})(_);