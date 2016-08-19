"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('User')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
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

    def success(self):
        return self.load_view('success.html')

    def register(self):
        data = {
             "first_name" : request.form['first_name'],
             "last_name" : request.form['last_name'],
             "email" : request.form['email'],
             "password" : request.form['password'],
             "confirm" : request.form['confirm']
        }
        # call create_user method from model and write some logic based on the returned value
        # notice how we passed the user_info to our model method
        create_status = self.models['User'].create_user(data)
        if create_status['status'] == True:
            # the user should have been created in the model
            # we can set the newly-created users id and name to session
            session['id'] = create_status['user']['id'] 
            session['first_name'] = create_status['user']['first_name']
            # we can redirect to the users profile page here
            return redirect('/success')
        else:
            # set flashed error messages here from the error messages we returned from the Model
            for message in create_status['errors']:
                flash(message, 'regis_errors')
            # redirect to the method that renders the form
            return redirect('/')
        
    def login(self):
        data = request.form
        user = self.models['User'].login_user(data)
        if not user:
            flash("Your login information is incorrect. Please try again.")
            return redirect('/')
        session['id'] = user['id']
        session['first_name'] = user['first_name']
        return redirect('/success')

    def logout(self):
        session.clear()
        return redirect('/')