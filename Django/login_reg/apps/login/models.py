from __future__ import unicode_literals

from django.db import models
import re, bcrypt

# Create your models here.
class UserManager(models.Manager):

  def login(self, postData):
    messages = []
    if len(postData['email']) < 1:
      messages.append("email must not be blank!")
    if len(postData['password']) < 1:
      messages.append("password must not be blank!")
    if not messages:
      # query db to check password
      user = User.objects.all().get(email=postData['email'])
      # check input against hashed password
      hashed = user.password
      password = postData['password']
      if bcrypt.checkpw(password.encode(), hashed.encode()):
        return None
      else:
        messages.append("password is incorrect!")
    return messages

  def register(self, postData):
    print "inside register"
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    messages = []
    if len(postData['first']) < 1:
      messages.append("first name must not be blank!")
    if len(postData['first']) < 2:
      messages.append("first name must be at least 2 characters!")
    if len(postData['last']) < 1:
      messages.append("last name must not be blank!")
    if len(postData['last']) < 2:
      messages.append("last name must be at least 2 characters!")
    if len(postData['email']) < 1:
      messages.append("email must not be blank!")
    if not EMAIL_REGEX.match(postData['email']):
      messages.append("email must be valid!")
    if len(postData['password']) < 1:
      messages.append("password must not be blank!")
    if len(postData['password']) < 8:
      messages.append("password must be at least 8 characters!")
    if postData['password'] != postData['confirm']:
      messages.append("passwords must match!")
    # query db for email check
    user_list = User.objects.filter(email=postData['email'])
    for user in user_list:
      print user.email
    if user_list:
      messages.append("email is already in the system!")
    if not messages:
      print "no messages"
      password = postData['password']
      pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
      print "create user"
      User.objects.create(first=postData['first'],last=postData['last'],email=postData['email'],password=pw_hash)
      print User.objects.all()
      return None
    return messages

class User(models.Model):
  first = models.CharField(max_length=45)
  last = models.CharField(max_length=45)
  email = models.EmailField()
  password = models.CharField(max_length=255)
  created_at = models.DateTimeField(auto_now_add = True)
  updated_at = models.DateTimeField(auto_now = True)
  objects = UserManager()

# Show validation error messages if validations fail the following tests
# First Name - Required; No fewer than 2 characters; letters only
# Last Name - Required; No fewer than 2 characters; letters only
# Email - Required; Valid Format
# Password - Required; No fewer than 8 characters in length; matches Password Confirmation
# Use Bcrypt to encrypt your users passwords
