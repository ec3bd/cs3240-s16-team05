from django.conf.urls import patterns, url
from secureshare import views

urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^auth/$', views.auth, name='auth'),
    url(r'^home/$', views.home, name='home'),
]