from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^ninjas$', views.index),
    url(r'^ninjas/(?P<color>\w+)$', views.color),
]
