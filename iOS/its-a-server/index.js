"use strict";

var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

var client_list = []
var users = []

app.get('/', function(req, res){
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  var user = new User(socket.id,socket);
  client_list.push(socket.id);
  // console.log(io)
  users.push(user)
  // console.log("this is user "+user.name,user.socket)
  io.emit('chat message', socket.id+" connected!");
  io.emit('total users', "Total Users Connected: "+io.engine.clientsCount)
  console.log("number of clients: "+io.engine.clientsCount)

  socket.on('disconnect', function() {
    console.log('User disconnected!');
    for(var i = 0; i<users.length;i++){
      if (users[i].socket.id == socket.id){
            io.emit('chat message', users[i].name+" disconnected!");
      }
    }
    client_list.splice(i,1);
    users.splice(i,1);
    io.emit('total users', "Total Users Connected: "+io.engine.clientsCount);
  });

  socket.on('chat message', function(msg){
    console.log(client_list)
    console.log(users)
    for(var i = 0; i<users.length;i++){
      if (users[i].socket.id == socket.id){
        console.log(users[i].name)
        console.log(msg)
        io.emit('chat message', users[i].name+": ");
        io.emit('chat message', msg);
      }
    }
  });

  socket.on('username', function(name){
    for(var i = 0; i<users.length;i++){
      if (users[i].socket.id == socket.id){
        console.log("username change")        
        io.emit('total users', users[i].name+" is now "+name);
        users[i].name = name;
      }
    }
  });

});

http.listen(8080, function(){
   console.log('listening on *:8080');
});

class User {
  constructor(name, socket) {
    this.name = name;
    this.socket = socket;
  }
}
