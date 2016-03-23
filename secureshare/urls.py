from django.conf.urls import patterns, url
from secureshare import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]