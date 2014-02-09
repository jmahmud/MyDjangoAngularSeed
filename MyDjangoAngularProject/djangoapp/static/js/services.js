'use strict';

/* Services */


// Demonstrate how to register services
// In this case it is a simple value service.
angular.module('myApp.services', []).value('version', '0.1');
myApp.factory('photosSvc',function($http, $log, $q){
	return{

		getPhotos : function(){

			//Create a promise using promise library
			var deferred = $q.defer();

			$http({method: 'GET', url: '/api/photos/'}).
				success(function(data, status, headers,config){
					deferred.resolve(data);
					$log.warn(data);
				}).
				error(function(data, status, headers,config){
					deferred.reject(status);
					$log.warn(status);
				});

			return deferred.promise;
		}
	};
}).factory('albumsSvc',function($http, $log, $q) {
	return {
		getAlbums: function(){

			//Create a promise using promise library
			var deferred = $q.defer();

			$http({method: 'GET', url: '/api/albums/'}).
				success(function(data, status, headers,config){
					deferred.resolve(data);
					$log.warn(data);
				}).
				error(function(data, status, headers,config){
					deferred.reject(status);
					$log.warn(status);
				});

			return deferred.promise;
		}
	};
});


