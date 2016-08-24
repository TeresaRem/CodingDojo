from system.core.model import Model

class Message(Model):
    def __init__(self):
        super(Message, self).__init__()

    def get_messages(self,id):
        query = '''SELECT user_id,author_id,first_name,last_name,messages.created_at,message 
                    FROM messages JOIN users ON users.id = messages.user_id 
                    WHERE user_id=:id'''
        data = {'id': id}
        return self.db.query_db(query, data)

    def add_message(self,data):
        sql = "INSERT INTO messages (message, created_at, user_id, author_id) values(:message, NOW(), :id, :author_id)"
        self.db.query_db(sql, data)
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