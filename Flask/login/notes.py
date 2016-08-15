# basic encryption notes

import md5 # do this at the top of your file where you import modules

@app.route('/users/create', methods=['POST'])
def create_user():
     username = request.form['username']
     email = request.form['email']
     password = md5.new(request.form['password']).hexdigest();
     insert_query = '''INSERT INTO users (username, email, password, created_at, updated_at) 
     VALUES (:username,:email, :password, NOW(), NOW())'''
     query_data = { 'username': username, 'email': email, 'password': password }
     mysql.query_db(insert_query, query_data)

# on user login
password = md5.new(request.form['password']).hexdigest()
email = request.form['email']
user_query = "SELECT * FROM users where users.email = :email AND users.password = :password"
query_data = { 'email': email, 'password': password}
user = mysql.query_db(user_query, query_data)
# do the necessary logic to login if the user exists, otherwise redirect to login page with error message<br>

# salt

import os, binascii # include this at the top of your file
salt = binascii.b2a_hex(os.urandom(15))

username = request.form['username']
email = request.form['email']
password = request.form['password']
salt =  binascii.b2a_hex(os.urandom(15))
encrypted_pw = md5.new(password + salt).hexdigest()
insert_query = '''INSERT INTO users (username, email, password, salt, created_at, updated_at) 
     VALUES (:username, :email, :encrypted_pw, :salt, NOW(), NOW())'''
query_data = { 'username': username, 'email': email, 'encrypted_pw': encrypted_pw, 'salt': salt}
mysql.query_db(insert_query, query_data)

# check it out 
email = request.form['email']
password = request.form['password']
user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
query_data = {'email': email}
user = mysql.query_db(user_query, query_data)
if user[0]:
 encrypted_password = md5.new(password + user[0]['salt']).hexdigest();
 if user[0]['password'] == encrypted_password:
  # this means we have a successful login!
 else:
     # invalid password!
else:
  # invalid email!
