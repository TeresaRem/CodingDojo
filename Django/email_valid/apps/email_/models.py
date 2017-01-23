from __future__ import unicode_literals

from django.db import models

# regex
import re

class EmailManager(models.Manager):
  def test(self, postData):
    EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
    print postData
    if len(postData['email']) < 1:
      return "Please enter an email!"
    elif not EMAIL_REGEX.match(postData['email']):
      return "Email is not valid! Try again."
    else:
      Email.objects.create(email=postData['email'])
      return True

# Create your models here.
class Email(models.Model):
  email = models.CharField(max_length=100)
  created_at = models.DateTimeField(auto_now_add=True)
  objects = EmailManager()

