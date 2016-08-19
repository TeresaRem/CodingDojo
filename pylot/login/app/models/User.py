""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import re
import bcrypt 


class User(Model):
    def __init__(self):
        super(User, self).__init__()


    def add_user(self, data):

        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        return self.db.query_db(query,data) # { "status": True, "user": users[0] }

    def create_user(self, data):
        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []
        # Some basic validation
        # add email check from db for existing email
        if not data['first_name']:
            errors.append('First Name cannot be blank')
        elif len(data['first_name']) < 2:
            errors.append('First name must be at least 2 characters long')
        elif not data['first_name'].isalpha():
            errors.append('First name must be letters only')
        if not data['last_name']:
            errors.append('Last name cannot be blank')
        elif len(data['last_name']) < 2:
            errors.append('Last name must be at least 2 characters long')
        elif not data['last_name'].isalpha():
            errors.append('Last name must be letters only')
        if not data['email']:
            errors.append('Email cannot be blank')
        elif not EMAIL_REGEX.match(data['email']):
            errors.append('Email format must be valid!')
        if not data['password']:
            errors.append('Password cannot be blank')
        elif len(data['password']) < 8:
            errors.append('Password must be at least 8 characters long')
        elif data['password'] != data['confirm']:
            errors.append('Password and confirmation must match!')
        # If we hit errors, return them, else return True.
        if errors:
            return {"status": False, "errors": errors}
        else:
            # check if email already in db
            user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
            user_data = {'email': data['email']}
            user = self.db.get_one(user_query, user_data)
            if user:
                errors.append('Email is already in the system!')
                return {"status": False, "errors": errors}
            # insert user
            password = data['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            data['password'] = hashed_pw
            query = '''INSERT INTO users (first_name,last_name,email,password, created_at) 
                        VALUES (:first_name,:last_name,:email,:password, NOW());'''
            self.db.query_db(query,data)
            # Then retrieve the last inserted user.
            get_user_query = "SELECT * FROM users ORDER BY id DESC LIMIT 1"
            users = self.db.query_db(get_user_query)
            return { "status": True, "user": users[0] }

    def login_user(self, data):
        password = data['password']
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        user_data = {'email': data['email']}
        # same as query_db() but returns one result
        user = self.db.get_one(user_query, user_data)
        if user:
           # check_password_hash() compares encrypted password in DB to one provided by user logging in
            if self.bcrypt.check_password_hash(user.password, password):
                return user
        # Whether we did not find the email, or if the password did not match, either way return False
        return False


    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """