""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model
import bcrypt

class User(Model):
    def __init__(self):
        super(User, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """
    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self,id):
        query = "SELECT * from users where id = :id LIMIT 1"
        data = {'id':id}
        return self.db.query_db(query, data)

    def create_user(self,data):
        # make first user an admin
        sql_first = "SELECT * from users LIMIT 1"
        first_user = self.db.query_db(sql_first)
        if first_user == []:
            data['user_level'] = 'admin'
        else:
            data['user_level'] = 'normal'
        # all other users
        password = data['password']
        hashed_pw = self.bcrypt.generate_password_hash(password)
        data['password'] = hashed_pw
        sql = '''INSERT INTO users (first_name, last_name, email, password, user_level, created_at)
                 VALUES (:first_name, :last_name, :email, :password, :user_level, NOW())'''
        self.db.query_db(sql, data)
        return True

    def update_user(self,data):
        if data['update'] == 'email':
            if data['user_level']=='normal' or data['user_level']=='admin':
                query = '''UPDATE users SET email=:email, first_name=:first_name, last_name=:last_name, user_level=:user_level 
                        WHERE id=:id'''
            else:
                query = '''UPDATE users SET email=:email, first_name=:first_name, last_name=:last_name 
                        WHERE id=:id'''
        elif data['update'] == 'password':
            # update password
            password = data['password']
            hashed_pw = self.bcrypt.generate_password_hash(password)
            data['password'] = hashed_pw
            query = '''UPDATE users SET password=:password WHERE id=:id'''
        elif data['update'] == 'description':
            # update description
            query = '''UPDATE users SET description=:description WHERE id=:id'''
        return self.db.query_db(query, data)
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    def destroy_user(self, id):
        query = "DELETE FROM users where id = :id LIMIT 1"
        data = {"id" : id }
        self.db.query_db(query,data)
        return True

