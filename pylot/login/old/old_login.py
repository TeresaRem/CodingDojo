    def add_user(self, data):

        EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')
        errors = []

        # validation
        # if not data['first_name']:
        #     errors.append('First name cannot be blank')
        # elif len(data['first_name']) < 2:
        #     errors.append('First name must be at least 2 characters long')
        # if not data['last_name']:
        #     errors.append('Last name cannot be blank')
        # elif len(data['first_name']) < 2:
        #     errors.append('Last name must be at least 2 characters long')
        # if not data['email']:
        #     errors.append('Email cannot be blank')
        # elif not EMAIL_REGEX.match(data['email']):
        #     errors.append('Email format must be valid!')
        # if not data['password']:
        #     errors.append('Password cannot be blank')
        # elif len(data['password']) < 8:
        #     errors.append('Password must be at least 8 characters long')
        # elif data['password'] != data['confirm']:
        #     errors.append('Password and confirmation must match!')
        # # If we hit errors, return them, else return True.
        # if errors:
        #     return {"status": False, "errors": errors}
        # else:
        #     password = data['password']
        #     hashed_pw = self.bcrypt.generate_password_hash(password)
        #     data['password'] = hashed_pw
        #     query = '''INSERT INTO users (first_name,last_name,email,password, created_at) 
        #                 VALUES (:first_name,:last_name,:email,:password, NOW());'''
            # users = self.db.query_db(query,data)
        password = data['password']
        hashed_pw = self.bcrypt.generate_password_hash(password)
        data['password'] = hashed_pw
        query = '''INSERT INTO users (first_name,last_name,email,password, created_at) 
                    VALUES (:first_name,:last_name,:email,:password, NOW());'''
        return self.db.query_db(query,data) # { "status": True, "user": users[0] }

    def register(self):
        data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email'],
        'password':request.form['password'],
        'confirm':request.form['confirm'],
        }
        user = self.models['User'].add_user(data)
        print "line 53:",user
        # session['id'] = user['id']
        # session['first_name'] = user['first_name']
        # if user['status'] == False:
        #     for message in user['errors']:
        #         flash(message, 'registration error')
        #     return redirect('/')
        return redirect('/success')