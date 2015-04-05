(function () {

	angular.module('cepas.menu', ['ngAnimate'])
		.controller('MenuController', ['$scope', '$location', function($scope, $location) {

		    $scope.ShowSubMenu = function(valor) {
		    	$scope.SubMenu = valor;
		    }

		}]);
})();
