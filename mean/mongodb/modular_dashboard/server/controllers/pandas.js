var mongoose = require('mongoose');
var Panda = mongoose.model('Panda');

module.exports = {
  index: function(req, res) {
    Panda.find({}, function(err, pandas) {
      res.render('index', {pandas: pandas});
    })
  },
  show: function(req, res) {
    var id = req.params.id
    Panda.find({_id:id}, function(err, pandas) {
      if(err) {
        console.log('something went wrong');
      } else { 
        console.log('successfully got the panda!');
        res.render('show',{pandas: pandas});
      }
    })
  },
  edit: function(req, res) {
    var id = req.params.id
    Panda.find({_id:id}, function(err, pandas) {
      if(err) {
        console.log('something went wrong');
      } else { 
        console.log('successfully got the panda!');
        res.render('edit',{pandas: pandas[0]});
      }
    })
  },
  create: function(req, res) {
    console.log("POST DATA", req.body);
    var panda = new Panda({name: req.body.name, age: req.body.age});
    panda.save(function(err) {
      if(err) {
        console.log('something went wrong');
      } else {
        console.log('successfully added a panda!');
        res.redirect('/');
      }
    })
  },
  update: function(req, res) {
    var id = req.params.id
    Panda.find({_id:id}, function(err, pandas) {
      if(err) {
        console.log('something went wrong');
      } else { 
        // update
        Panda.update({_id:id},{name: req.body.name, age: req.body.age}, function(err){
          console.log('something went wrong');
          res.redirect("/");
        });
      }
    });
  },
  destroy: function(req, res) {
    var id = req.params.id
    Panda.remove({_id:id}, function(err) {
      if(err) {
        console.log('something went wrong');
      } else{
        res.redirect("/");
      }
    });
  }
}