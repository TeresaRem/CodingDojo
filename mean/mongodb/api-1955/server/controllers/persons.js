var mongoose = require('mongoose');
var Person = mongoose.model('Person');

module.exports = {
  index: function(req, res) {
    Person.find({}, function(err, persons) {
      res.json(persons);
    })
  },
  create: function(req, res) {
    var name = req.params.name
    var person = new Person({name: name});
    person.save(function(err) {
      if(err) {
        console.log('something went wrong');
      } else {
        console.log('successfully added a person!');
        res.redirect('/');
      }
    })
  },
  show: function(req, res) {
    console.log(req.params)
    var name = req.params.name
    Person.find({name:name}, function(err, persons) {
      if(err) {
        console.log('something went wrong');
      } else { 
        console.log('successfully got the person!');
        res.json(persons);
      }
    })
  },
  destroy: function(req, res) {
    console.log(req.params)
    var name = req.params.name
    Person.remove({name:name}, function(err) {
      if(err) {
        console.log('something went wrong');
      } else{
        res.redirect("/");
      }
    });
  }
}