//////////////////////////////////////////////////////////
//                      Requires                        //
//////////////////////////////////////////////////////////
var bodyParser      = require("body-parser"),
    express         = require("express"),
    path            = require("path"),
    app             = express();

//Body Parser && Static Folder
app.use(bodyParser.json());
app.use(express.static(__dirname + "/client"));

//Routes require
require('./server/config/mongoose.js');
require('./server/config/routes.js')(app)

////////////////////////////////////////////////////////////
//                     Listen to Port                     //
////////////////////////////////////////////////////////////
app.listen(8000, function() {
    console.log("Hey, Listen! (Full Mean Demo: 8000)");
})
