# gives access to variable url - it points to a function
from django.conf.urls import url 

# gives access to views.py file
from . import views 

urlpatterns = [
  url(r'^$', views.index),
]
