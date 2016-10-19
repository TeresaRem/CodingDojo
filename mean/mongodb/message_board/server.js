var express = require("express");
var path = require("path");
var app = express();
var mongoose = require('mongoose');
var bodyParser = require('body-parser');

mongoose.Promise = global.Promise;
mongoose.connect('mongodb://localhost/message_board');

var Schema = mongoose.Schema;

var MessageSchema = new mongoose.Schema({
 name: {type:String,required:true,minlength:4}, 
 message: {type:String,required:true},
 comments: [{type:Schema.Types.ObjectId, ref: 'Comment'}]
});

var CommentSchema = new mongoose.Schema({
 _post: {type: Schema.Types.ObjectId, ref: 'Message'},
 name: { type: String, required: true, minlength:4 }, 
 text: { type: String, required: true } 
});

var Message = mongoose.model('Message', MessageSchema); 
var Comment = mongoose.model('Comment', CommentSchema); 


app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "./static")));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

//
//      GET ROUTES
//

app.get('/', function(req, res) {
    Message.find({}, function(err, posts) {
    if(err) {
      console.log('something went wrong');
      console.log(err);
      res.render("index",{title: 'you have errors!', errors: err});
    } else { 
      console.log('successfully got all posts!');
    }
    })
    .populate('comments')
    .exec(function(err, posts) {
      if(err) {
        console.log('something went wrong');
        console.log(err);
      } else {
      res.render('index', {posts: posts});
      }
    });
});

//
//      POST ROUTES
//

// add message to db
app.post('/messages', function(req, res) {
  console.log("POST DATA", req.body);
  var message = new Message({name: req.body.name, message: req.body.message});
  message.save(function(err) {
    if(err) {
      console.log('something went wrong');
    } else {
      console.log('successfully added a message!');
      res.redirect('/');
    }
  })
})
// add comment to db
app.post('/comments/:id', function(req, res) {
  Message.findOne({_id: req.params.id}, function(err, post){
    console.log(req.body)
         var comment = new Comment({
            _post: post._id,
            name: req.body.name,
            // bad naming convention
            text: req.body.text
          });
         console.log("COMMENT:", comment)
         // comment._post = post._id;
         post.comments.push(comment);
         comment.save(function(err){
            if(err) { console.log(err); }
                 post.save(function(err){
                       if(err) { console.log(err); } 
                       else { res.redirect('/'); }
                 });
         });
   });
})

app.listen(8000, function() {
 console.log("listening on port 8000");
});
