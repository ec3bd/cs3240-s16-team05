from django.conf.urls import patterns, url
from secureshare import views

urlpatterns = [
    url(r'^$', views.user_login, name='login'),
    url(r'^auth/$', views.user_login, name='auth'),
    url(r'^register/$', views.register, name='register'),
    url(r'^home/$', views.home, name='home'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
]