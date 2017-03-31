__author__ = 'hadoop'
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^index/',views.index,name='index'),
    url(r'^register/$', views.userRegister, name='register'),
    url(r'^login/$',views.userLogin,name='login'),
    url(r'^logout/$', views.userLogout, name='logout'),

]