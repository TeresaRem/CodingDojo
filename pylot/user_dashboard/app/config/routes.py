from system.core.router import routes

# GET routes
routes['default_controller'] = 'Users'
routes['/login'] = 'Users#login'
routes['/register'] = 'Users#register'
routes['/dashboard'] = 'Users#dashboard'
routes['/users/show/<id>'] = 'Users#show'
routes['/dashboard/admin'] = 'Users#admin'
routes['/users/new'] = 'Users#new'
routes['/users/edit/<id>'] = 'Users#edit'
routes['/users/delete/<id>'] = 'Users#delete'
routes['/users/destroy/<id>'] = 'Users#destroy'
routes['/logout'] = 'Users#logout'

# POST routes
routes['POST']['/process_login'] = 'Users#proccess_login'
routes['POST']['/process_register'] = 'Users#process_register'
routes['POST']['/users/new_user'] = 'Users#new_user'
routes['POST']['/users/edit_user'] = 'Users#edit_user'
routes['POST']['/users/edit_user_admin'] = 'Users#edit_user_admin'
