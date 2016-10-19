var pandas = require('../controllers/pandas.js');

module.exports = function(app) {
  // get
  app.get('/', function (req, res) {
    pandas.index(req, res)
  })
  app.get('/pandas/new', function (req, res) {
    res.render("new");
  })
  app.get('/pandas/:id', function(req, res) {
    pandas.show(req, res)
  })
  app.get('/pandas/:id/edit', function(req, res) {
    pandas.edit(req, res)
  })
  // post
  app.post('/pandas', function(req, res) {
    pandas.create(req, res)
  })
  app.post('/pandas/:id', function(req, res) {
    pandas.update(req, res)
  })
  app.post('/pandas/:id/destroy', function(req, res) {
    pandas.destroy(req, res)
  })
}
