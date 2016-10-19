// controller for creating a new entry
app.controller('newController', ['$scope','friendsFactory','$location', function($scope, friendsFactory,$location) {
  $scope.create = function(){
    // call create method in factory
    friendsFactory.create($scope.friend, function(data) {
      console.log(data);
      // redirect to index page
      $location.url('/')
    });
    $scope.friend = {};
   };
}]); 