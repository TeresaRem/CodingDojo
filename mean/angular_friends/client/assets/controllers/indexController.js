app.controller('indexController', ['$scope','$routeParams','$location','friendsFactory', function($scope, $routeParams, $location, friendsFactory) {
  // is this the correct format for fetching all friends?
  var index = function(){
    console.log('indexController ran index function')
    friendsFactory.index(function(returnedData){
    $scope.friends = returnedData;
    });
  };
  index();

  // fetch single friend via id
  friendsFactory.show($routeParams.id, function(data) {
      console.log(data);
      $scope.friend = data;
      // $location.url('/')
    });

  // fetch single friend via id, plus send req.body data for update in backend
  $scope.update = function(){
    friend={
      first:$scope.friend.first,
      last:$scope.friend.last,
      birth:$scope.friend.birth
    }
    console.log('friend is ',friend)
    friendsFactory.update($routeParams.id,friend, function(data) {
      console.log(data);
      $scope.friend = data;
      // this redirect doesn't work...
      $location.url('#/')
    });
  };
  $scope.delete = function(id){
    friendsFactory.delete(id, function(data) {
      console.log(data);
      $scope.friend = data;
      index();
      // $location.url('/')
    });
  };

}]); 
