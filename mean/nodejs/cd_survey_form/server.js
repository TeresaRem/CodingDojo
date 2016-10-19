// Load the express module
var express = require("express");
//require path module
var path = require("path");
// require body-parser
var bodyParser = require('body-parser');
// invoke var express and store the resulting application in var app
var app = express();
 
app.use(bodyParser.urlencoded());
// static content 
app.use(express.static(path.join(__dirname, "./static")));
// setting up ejs and our views folder
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

//we're going to have /routes/index.js handle all of our routing
var route = require('./routes/index.js')(app);
// tell your server which port to run on
app.listen(3000, function() {
 console.log("listening on port 3000!");
})