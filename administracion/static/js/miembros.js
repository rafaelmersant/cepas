(function (_) {

  angular.module('cepas.miembros', ['ngAnimate'])
    
    .factory('MiembrosService', ['$http', '$q', '$filter', function ($http, $q, $filter) {

      function getMiembros(miembro) {
        var deferred = $q.defer();

        if(miembro == undefined || miembro == '') {
        	url = '/api/miembros/buscar/nombre-apellido/?format=json';
        } else {
        	url = '/api/miembros/buscar/nombre-apellido/{nombreApellido}/?format=json'.replace('{nombreApellido}', miembro);
        }

        $http.get(url)
          .success(function (data) {

            if(data.length > 0) {
              deferred.resolve(data);
            } else {
              deferred.reject();
            }
            
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

      //Buscar miembro
      $scope.buscarMiembro = function($event) {
        $event.preventDefault();

      	try {
          if($event.type == 'click' || $event.keyCode == 13) {
  	        MiembrosService.getMiembros($scope.miembro).then(function (data) {

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