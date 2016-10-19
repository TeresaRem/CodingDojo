console.log('Loaded Friends Factory');
app.factory('friendsFactory', ['$http', function($http) {
  var friends = [];
  var friend = {};
  var factory = {};
    // use form info to create a friend
    factory.create = function(newfriend,callback){
      console.log('create friend in factory');
      $http.post('/friends', newfriend).then(function(returned_data){
        console.log(returned_data.data);
        if (typeof(callback) == 'function'){
          callback(returned_data.data);
        }
      });
    };
    // use id and form info to update
    factory.update = function(id,friend,callback){
      console.log(friend);
      $http.post(`/friends/${id}/edit`,friend).then(function(returned_data){
        callback(returned_data.data);
      });
    };
    // get all friends
    factory.index = function(callback){
      $http.get('/friends').then(function(returned_data){
        friends = returned_data.data;
        callback(friends);
      });
    };
    // delete a friend via ID
    factory.delete = function(id,callback){
      $http.post(`/friends/${id}/destroy`).then(function(returned_data){
        friends = returned_data.data;
        callback(friends);
      });
    };
    // get a single friend via ID
    factory.show = function(id,callback){
      $http.get(`/friends/${id}`).then(function(returned_data){
        friend = returned_data.data;
        callback(friend);
      });
    };
    // what is this used for??????
    factory.getFriends = function(callback){
      callback(friends);
    };
    // what is this used for??????
    factory.getFriend = function(callback){
        callback(friend);
    };
  return factory;
}]);
