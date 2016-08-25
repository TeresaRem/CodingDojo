
from system.core.controller import *
from flask import flash

class Users(Controller):
    def __init__(self, action):
        super(Users, self).__init__(action)
        self.load_model('User')
        self.load_model('Message')
        self.db = self._app.db

    def index(self):
        session['id'] = 5
        session['user_level'] = 'admin'
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
        messages = self.models['Message'].get_messages(id)
        comments = self.models['Message'].get_comments(id)
        return self.load_view('show.html',user=user[0],messages=messages,comments=comments)

    def admin(self):
        # add id
        users = self.models['User'].get_users()
        return self.load_view('dashboard.html',users=users,admin=True)

    def new(self):
        return self.load_view('new.html')

    def edit(self,id):
        user = self.models['User'].get_user(id)
        return self.load_view('edit.html',user=user[0])

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


    ''' obsoleted routes ''' 
    # def edit_user(self):
    #     data = {'id':session['id'],
    #             'update': request.form['update']
    #             }
    #     if request.form['update'] == 'email':
    #         data['email'] = request.form['email']
    #         data['first_name'] = request.form['first_name']
    #         data['last_name'] = request.form['last_name']
    #     elif request.form['update'] == 'password':
    #         data['password'] = request.form['password']
    #     elif request.form['update'] == 'description':
    #         data['description'] = request.form['description']
    #     # breaks here
    #     user = self.models['User'].update_user(data)
    #     return redirect('/dashboard')

    # def edit_user_admin(self):
    #     data = {'id':request.form['id'],
    #             'update': request.form['update']
    #             }
    #     if request.form['update'] == 'email':
    #         data['email'] = request.form['email']
    #         data['first_name'] = request.form['first_name']
    #         data['last_name'] = request.form['last_name']
    #         data['user_level'] = request.form['user_level']
    #     elif request.form['update'] == 'password':
    #         data['password'] = request.form['password']
    #     elif request.form['update'] == 'description':
    #         data['description'] = request.form['description']
    #     # breaks here
    #     user = self.models['User'].update_user(data)
    #     return redirect('/dashboard')

    def new_user(self):
        data = {
            'email': request.form['email'],
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'password': request.form['password']
        }
        valid = self.models['User'].create_user(data)
        if valid == True:
            return redirect('/dashboard')
        else:
            return redirect('/users/new')

    def delete(self,id):
        user = self.models['User'].get_user(id)
        return self.load_view('delete.html',user=user[0])

    def destroy(self,id):
        data = {"id":id}
        user = self.models['User'].destroy_user(id)
        # add flash
        return redirect('/dashboard')

    def edit_information(self):
        # add flash
        user = self.models['User'].update_user(request.form)
        return redirect('users/show/{}'.format(request.form['id']))

    def edit_password(self):
        # add flash
        user = self.models['User'].update_user(request.form)
        return redirect('users/show/{}'.format(request.form['id']))

    def edit_description(self):
        # add flash
        user = self.models['User'].update_user(request.form)
        return redirect('users/show/{}'.format(request.form['id']))

    def new_message(self):
        message = self.models['Message'].add_message(request.form)
        return redirect('users/show/{}'.format(request.form['wall_id']))

    def new_comment(self):
        comment = self.models['Message'].add_comment(request.form)
        return redirect('users/show/{}'.format(request.form['wall_id']))

    def delete_message(self,message_id):
        message = self.models['Message'].destroy_message(message_id)
        # add flash
        # fix, return to user's wall
        return redirect('/dashboard')

    def delete_comment(self,comment_id):
        comment = self.models['Message'].destroy_comment(comment_id)
        # add flash
        # fix, return to user's wall
        return redirect('/dashboard')
        