#import necessary tools from flask
from flask import Flask, render_template, redirect, request, session
# import our connector doc
from mysqlconnection import MySQLConnector
app = Flask(__name__)

app.secret_key="magicalunicorns"

mysql = MySQLConnector(app, "zoo")

"""GET routes"""
#we should have a get route for every template we wish to render. destroy routes will typically be get routes, too.

@app.route('/')
def index():
    # select all animals to display in table
    query = "SELECT * FROM animals"
    animals = mysql.query_db(query)
    # pass animals to front end
    return render_template("index.html", animals=animals)

@app.route('/show/<id>')
def show(id):
    # select one animal for individual display of details
    print "server.py line 18: animal id:", id
    query = "SELECT * FROM animals WHERE id=:id"
    values = {
        "id": id
    }
    animal = mysql.query_db(query, values)
    print animal
    # pass animal data to template
    return render_template("show.html", animal=animal[0])

@app.route('/edit/<id>')
def edit(id):
    print "server.py line 18: animal id:", id
    # date is formatted in such a way as to work for auto-filling a date input in html template
    query = "SELECT species, weight, DATE_FORMAT(DOB, '%Y-%m-%d') AS DOB, food, location FROM animals WHERE id=:id"
    values = {
        "id": id
    }
    animal = mysql.query_db(query, values)
    print "edit animal page, result:", animal
    # pass animal data to front end to auto-fill form
    return render_template("edit.html", animal=animal[0])

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/delete/<id>')
def delete(id):
    print "this is my animal's id on line 44 in server.py:", id
    #select animal data to pass to front end, this is only necessary if I want to display that data, otherwise, simply pass id to template to be used in url if user confirms delete
    query = "SELECT * FROM animals WHERE id=:id"
    values = {
        "id": id
    }
    animal = mysql.query_db(query, values)
    return render_template("delete.html", animal=animal[0])

@app.route('/destroy/<id>')
def destroy(id):
    # remove animal from db is user confirms removal
    query = "DELETE FROM animals WHERE id=:id"
    values = {
        "id": id
    }
    mysql.query_db(query, values)
    return redirect('/')

"""POST routes"""
#we should have a post route for every form we submit

@app.route('/animal/add', methods=['POST'])
def add_animal():
    print request.form
    # add validations
    query = "INSERT INTO animals (species, weight, DOB, food, location, created_at) VALUES (:species, :weight, :dob, :food, :location, NOW())"
    values = {
        "species": request.form['species'],
        "weight": request.form['weight'],
        "dob": request.form['dob'],
        "food": request.form['food'],
        "location": request.form['loc']
    }
    mysql.query_db(query, values)
    return redirect('/')

@app.route('/animal/edit/<id>', methods=['POST'])
def edit_animal(id):
    print request.form
    # add validations
    query = "UPDATE animals SET species=:species, weight=:weight, DOB=:dob, food=:food, location=:location, updated_at=NOW()"
    values = {
        "species": request.form['species'],
        "weight": request.form['weight'],
        "dob": request.form['dob'],
        "food": request.form['food'],
        "location": request.form['loc']
    }
    mysql.query_db(query, values)
    return redirect('/')

app.run(debug=True)
