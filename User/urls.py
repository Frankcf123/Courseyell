__author__ = 'hadoop'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/',views.index,name='index'),
]