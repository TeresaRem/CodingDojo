console.log('friends model');
var mongoose = require('mongoose');

var FriendSchema = new mongoose.Schema({
 first: String,
 last: String,
 birth: Date
})
var Friend = mongoose.model('Friend', FriendSchema); 