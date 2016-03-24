from django.conf.urls import patterns, url
from secureshare import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^register/$', views.register, name='register'),
    url(r'^authregister/$', views.authregister, name='authregister'),
    url(r'^home/$', views.home, name='home'),
]