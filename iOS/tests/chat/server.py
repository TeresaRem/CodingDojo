from flask import Flask, render_template
from mysqlconnection import MySQLConnector
from flask_socketio import SocketIO
from flask_socketio import send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

if __name__ == '__main__':
    socketio.run(app)

@socketio.on('message')
def handle_message(message):
    send(message)

# send for unnamed event
@socketio.on('json')
def handle_json(json):
    send(json, json=True)

''' FOR NAMED EVENT USE EMIT
@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', json)
'''

'''
@socketio.on('json')
def handle_json(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))

@socketio.on('my event')
def handle_my_custom_event(arg1, arg2, arg3):
    print('received args: ' + arg1 + arg2 + arg3)


To send an event with multiple arguments, send a tuple:

@socketio.on('my event')
def handle_my_custom_event(json):
    emit('my response', ('foo', 'bar', json), namespace='/chat')


'''

''' ROOMS

from flask_socketio import join_room, leave_room

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    send(username + ' has entered the room.', room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)


'''
