# gives access to variable url - it points to a function
from django.conf.urls import url 

# gives access to views.py file
from . import views 

urlpatterns = [
  # url method uses RegEx to match route, then runs method
  url(r'^$', views.index),
  # need comma after each url method 
  # eventually use named routes name='index'
  url(r'^users$', views.show)
]
