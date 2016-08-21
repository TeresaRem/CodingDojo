from system.core.controller import *

class Products(Controller):
    def __init__(self, action):
        super(Products, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('Product')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
# GET ROUTES
    def index(self):
        """
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_users()
        
        self.models['WelcomeModel'].add_message()
        # messages = self.models['WelcomeModel'].grab_messages()
        # user = self.models['WelcomeModel'].get_user()
        # to pass information on to a view it's the same as it was with Flask
        
        # return self.load_view('index.html', messages=messages, user=user)
        """
        products=self.models['Product'].get_products()
        return self.load_view('index.html', products=products)

    def new(self):
        return self.load_view('new.html')

    def edit(self, id):
        product=self.models['Product'].get_product(id)
        return self.load_view('edit.html', product=product)

    def show(self, id):
        product=self.models['Product'].get_product(id)
        return self.load_view('show.html', product=product)

# POST ROUTES

    def create(self):
        data = {
            'name' : request.form['name'],
            'description' : request.form['description'],
            'price' : request.form['price']
        }
        self.models['Product'].add_product(data)
        return redirect('/')

    def destroy(self, id):
        self.models['Product'].destroy_product(id)
        return redirect('/')

    def update(self, id):
        data = {
            'id' : id,
            'name' : request.form['name'],
            'description' : request.form['description'],
            'price' : request.form['price']
        }
        product=self.models['Product'].update_product(data)
        return redirect('/')