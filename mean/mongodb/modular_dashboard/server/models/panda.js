var mongoose = require('mongoose');

var PandaSchema = new mongoose.Schema({
 name: String,
 age: Number
})
var Panda = mongoose.model('Panda', PandaSchema); 