from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()

    def get_messages(self,id):
        query = '''SELECT user_id,wall_id,first_name,last_name,messages.created_at,message,messages.id 
                    FROM messages JOIN users ON users.id = messages.user_id 
                    WHERE wall_id=:id
                    ORDER BY messages.created_at DESC'''
        data = {'id': id}
        return self.db.query_db(query, data)

    def add_message(self,data):
        print data
        sql = "INSERT INTO messages (message, created_at, user_id, wall_id) values(:message, NOW(), :id, :wall_id)"
        self.db.query_db(sql, data)
        return True


    def get_comments(self,id):
        query = '''SELECT first_name,last_name,messages.id as message_id,messages.user_id,comments.comment,comments.created_at,comments.user_id,messages.wall_id,comments.id FROM users
                    JOIN messages ON users.id=messages.user_id
                    JOIN comments ON messages.id=comments.message_id'''
        data = {'id': id}
        return self.db.query_db(query, data)

    def add_comment(self,data):
        print data
        sql = "INSERT INTO comments (comment, created_at, user_id, message_id, wall_id) values(:comment, NOW(), :id, :message_id, :wall_id)"
        self.db.query_db(sql, data)
        return True

    def destroy_message(self,message_id):
        query_comments = "DELETE FROM comments where message_id = :id LIMIT 1"
        data = {"id" : message_id }
        self.db.query_db(query_comments,data)
        query_message = "DELETE FROM messages where id = :id LIMIT 1"
        self.db.query_db(query_message,data)
        return True

    def destroy_comment(self,comment_id):
        query = "DELETE FROM comments where id = :id LIMIT 1"
        data = {"id" : comment_id }
        self.db.query_db(query,data)
        return True

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