console.log("routes");
var friends = require('../controllers/friends.js');

module.exports = function(app){
  app.get('/',friends.index);
  app.get('/friends', friends.index);
  app.get('/friends/:id', friends.show);
  app.post('/friends', friends.create);
  app.post('/friends/:id/edit', friends.update);
  app.post('/friends/:id/destroy', friends.delete);
}
