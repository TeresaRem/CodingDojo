from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    query = "SELECT * FROM friends"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', all_friends=friends) # pass data to our template

@app.route('/friends', methods=['POST'])
def create():
    query = '''INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) 
            VALUES (:first_name, :last_name, :occupation, NOW(), NOW())'''
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    mysql.query_db(query, data)
    return redirect('/')


@app.route('/friends/<id>') # this is somewhat redundant
def show(id):
    id = id
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0], id=id)

@app.route('/friends/<id>', methods=['POST'])
def update(id):
    id = id
    query = '''UPDATE friends 
             SET first_name = :first_name, last_name = :last_name, occupation = :occupation 
             WHERE id = :id'''
    data = {
             'first_name': request.form['first_name'], 
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation'],
             'id': id
           }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/friends/<id>/edit')
def edit(id):
    query = "SELECT * FROM friends WHERE id = :specific_id"
    data = {'specific_id': id}
    friends = mysql.query_db(query, data)
    return render_template('index.html', one_friend=friends[0], id=id)

@app.route('/friends/<id>/delete') # assignment states methods=['POST']
def delete(id):
    query = "DELETE FROM friends WHERE id = :id"
    data = {'id': id}
    mysql.query_db(query, data)
    return redirect('/')


app.run(debug=True)
