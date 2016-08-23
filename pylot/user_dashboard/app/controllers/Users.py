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
        self.load_model('Message')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """

    def index(self):
        session['id'] = 5
        return self.load_view('index.html')

    def login(self):
        return self.load_view('login.html')

    def register(self):
        return self.load_view('register.html')

    def dashboard(self):
        users = self.models['User'].get_users()
        return self.load_view('dashboard.html',users=users)

    def show(self,id):
        user = self.models['User'].get_user(id)
        return self.load_view('show.html',user=user[0])

    def edit(self):
        user = self.models['User'].get_user(session['id'])
        return self.load_view('edit.html',user=user[0])

    def admin(self,id):
        return self.load_view('dashboard_admin.html',id=id)

    def new(self):
        return self.load_view('new.html')

    def admin_edit(self,id):
        return self.load_view('edit_admin.html',id=id)

    def logout(self):
        session.clear()
        return redirect('/')

    def proccess_login(self):
        return redirect('/dashboard')

    def process_register(self):
        data = {
            'email': request.form['email'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'password': request.form['password']
        }
        valid = self.models['User'].create_user(data)
        if valid == True:
            # fix how to set session['id']
            # user = self.models['User'].get_user(data)
            # session['id'] = user[0]
            return redirect('/dashboard')
        else:
            return redirect('/register')

    def edit_user(self):
        data = {'id':session['id'],
                'update': request.form['update']
                }
        if request.form['update'] == 'email':
            data['email'] = request.form['email']
            data['first_name'] = request.form['first_name']
            data['last_name'] = request.form['last_name']
            print "line 88, build data",data
        elif request.form['update'] == 'password':
            data['password'] = request.form['password']
        elif request.form['update'] == 'description':
            data['description'] = request.form['description']
        # breaks here
        user = self.models['User'].update_user(data)
        return redirect('/dashboard')



