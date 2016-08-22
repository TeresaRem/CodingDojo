"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

"""
    This is where you define routes
    
    Start by defining the default controller
    Pylot will look for the index method in the default controller to handle the base route

    Pylot will also automatically generate routes that resemble: '/controller/method/parameters'
    For example if you had a products controller with an add method that took one parameter 
    named id the automatically generated url would be '/products/add/<id>'
    The automatically generated routes respond to all of the http verbs (GET, POST, PUT, PATCH, DELETE)
"""
routes['default_controller'] = 'Users'

routes['/login'] = 'Users#login'
routes['POST']['/process_login'] = 'Users#proccess_login'

routes['/register'] = 'Users#register'
routes['POST']['/proccess_register'] = 'Users#process_register'

# user features
routes['/dashboard'] = 'Users#dashboard'
routes['/users/show/<id>'] = 'Users#show'
routes['/users/edit'] = 'Users#edit'

# admin features
routes['/dashboard/admin'] = 'Users#admin'
routes['/users/new'] = 'Users#new'
routes['POST']['/users/new_user'] = 'Users#new_user'
routes['/users/edit/<id>'] = 'Users#admin_edit'
routes['POST']['/users/edit_user'] = 'Users#edit_user'


"""
    You can add routes and specify their handlers as follows:

    routes['VERB']['/URL/GOES/HERE'] = 'Controller#method'

    Note the '#' symbol to specify the controller method to use.
    Note the preceding slash in the url.
    Note that the http verb must be specified in ALL CAPS.
    
    If the http verb is not provided pylot will assume that you want the 'GET' verb.

    You can also use route parameters by using the angled brackets like so:
    routes['PUT']['/users/<int:id>'] = 'users#update'

    Note that the parameter can have a specified type (int, string, float, path). 
    If the type is not specified it will default to string

    Here is an example of the restful routes for users:

    routes['GET']['/users'] = 'users#index'
    routes['GET']['/users/new'] = 'users#new'
    routes['POST']['/users'] = 'users#create'
    routes['GET']['/users/<int:id>'] = 'users#show'
    routes['GET']['/users/<int:id>/edit' = 'users#edit'
    routes['PATCH']['/users/<int:id>'] = 'users#update'
    routes['DELETE']['/users/<int:id>'] = 'users#destroy'
"""
