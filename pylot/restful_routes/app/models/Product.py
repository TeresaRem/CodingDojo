from system.core.model import Model

class Product(Model):
    def __init__(self):
        super(Product, self).__init__()
    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database
    """

    def get_products(self):
        query = "SELECT * from products"
        return self.db.query_db(query)

    def get_product(self, id):
        query = "SELECT * from products where id = :id"
        data = {'id': id}
        return self.db.get_one(query, data)

    def add_product(self, data):
        sql = "INSERT into products (name, description, price) values(:name, :description, :price)"
        self.db.query_db(sql, data)
        return True
    
    def update_product(self, data):
        query = '''UPDATE products 
                    SET name=:name, description=:description, price=:price 
                    WHERE id = :id'''
        return self.db.query_db(query, data)

    def destroy_product(self, id):
        query = "DELETE FROM products WHERE id = :id"
        data = {'id' : id}
        return self.db.query_db(query, data)