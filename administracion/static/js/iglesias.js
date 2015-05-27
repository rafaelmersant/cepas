(function (_) {

  angular.module('cepas.iglesias', ['ngAnimate'])
    
    .factory('IglesiasService', ['$http', '$q', '$filter', function ($http, $q, $filter) {

      function getIglesias(titulo_conciliar, titulo_local) {
        var deferred = $q.defer();

        if((nombres == undefined) && sociedad == undefined) {
        	url = '/api/miembros/buscar/nombre-apellido/?format=json';
        }

        if(sociedad == "undefined") {
          url = '/api/miembros/buscar/nombre-apellido/{nombreApellido}/?format=json'.replace('{nombreApellido}', nombres);
        } else {
        	url = '/api/miembros/buscar/nombre-apellido/{nombreApellido}/{sociedad}/?format=json'
                  .replace('{nombreApellido}', nombres)
                  .replace('{sociedad}', sociedad);
        }

        $http.get(url)
          .success(function (data) {

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
        getIglesias: getIglesias
      };

    }])

    //****************************************************
    //                                                   *
    //CONTROLLERS                                        *
    //                                                   *
    //****************************************************
    .controller('IglesiasCtrl', ['$scope', '$filter', 'IglesiasService', function ($scope, $filter, IglesiasService) {

      //Inicializar variables
      $scope.sociedad = 'undefined';
      
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