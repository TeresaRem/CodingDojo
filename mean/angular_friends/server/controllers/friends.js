console.log('friends controller');

var mongoose = require('mongoose');
var Friend = mongoose.model('Friend');

module.exports = {
  index: function(req, res) {
    Friend.find({}, function(err, friends) {
      res.json(friends);
    })
  },
  create: function(req, res) {
    console.log('create controller active')
    var first = req.body.first;
    var last = req.body.last;
    var birth = req.body.birth;
    var friend = new Friend({first: first,last: last,birth: birth});
    friend.save(function(err) {
      if(err) {
        console.log('something went wrong');
      } else {
        console.log('successfully added a friend!');
        res.json(friend);
      }
    })
  },
  update: function(req, res) {
    console.log(req)
    Friend.findOne({_id: req.params.id}, function(err, friend) {
      if(err) {
        console.log('something went wrong');
      } else {
        friend.first = req.body.first;
        friend.last = req.body.last;
        friend.birth = req.body.birth;
        friend.save(function(err) {
          if(err) {
            console.log('something went wrong');
          } else {
            console.log(friend);
            console.log('successfully edited a friend!');
            res.json(friend);
          }
        })
      }
    });
  },
  delete: function(req, res) {
    Friend.remove({_id:req.params.id}, function(err, data) {
      if(err) {
        console.log('something went wrong');
      } else{
        res.json(data);
      }
    });
  },
  show: function(req, res) {
    console.log(req.params.id);
    Friend.findOne({_id:req.params.id}, function(err, friend) {
      if(err) {
        console.log('something went wrong');
      } else { 
        console.log('successfully got the friend!');
        console.log(friend);
        res.json(friend);
      }
    })
  }
}

// function FriendsController(){
//   this.index = function(req,res){
//     //your code here
//     res.json({placeholder:'index'});
//   };
//   this.create = function(req,res){
//     //your code here
//     res.json({placeholder:'create'});
//   };
//   this.update = function(req,res){
//     //your code here
//     res.json({placeholder:'update'});
//   };
//   this.delete = function(req,res){
//     //your code here
//     res.json({placeholder:'delete'});
//   };
//   this.show = function(req,res){
//     //your code here
//     res.json({placeholder:'show'});
//   };
// }
// module.exports = new FriendsController(); // what does this export?
