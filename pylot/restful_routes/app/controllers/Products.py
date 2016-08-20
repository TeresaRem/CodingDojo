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
        return self.load_view('index.html')

    def new(self):
        return self.load_view('new.html')

    def edit(self, id):
        return self.load_view('edit.html',id=id)

    def show(self, id):
        return self.load_view('show.html',id=id)

# POST ROUTES

    def create(self):
        return redirect('/')

    def destroy(self):
        return redirect('/')

    def update(self):
        return redirect('/')