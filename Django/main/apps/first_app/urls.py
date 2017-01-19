# gives access to variable url - it points to a function
from django.conf.urls import url 

# gives access to views.py file
from . import views 

urlpatterns = [

  # COMMA after each URL METHOD

  # url method uses RegEx to match route, then runs method
  url(r'^$', views.index),
  # eventually use named routes name='index'
  url(r'^users$', views.show),
  url(r'^new_user$', views.create)
]
