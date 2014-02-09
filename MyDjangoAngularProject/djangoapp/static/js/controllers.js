'use strict';

/* Controllers */

// angular.module('myApp.controllers', []).
//   controller('MyCtrl1', [function($scope,photosSvc) {
//   	$scope.photos = photosSvc.photos2;

//   }])
//   .controller('MyCtrl2', [function() {

//   }]);

myApp.controller('MyCtrl1',
	function MyCtrl1($scope, photosSvc){
		
		photosSvc.getPhotos().then(function(photos){
			$scope.photos = photos;
		});
	}
);

myApp.controller('MyCtrl2',
	function MyCtrl2($scope, albumsSvc){
		
		albumsSvc.getAlbums().then(function(albums){
			$scope.albums = albums;
			console.log(albums)
		});	
	}
);