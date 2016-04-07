from django.conf.urls import include, patterns, url
from secureshare import views

urlpatterns = [
    url(r'^$', views.user_login, name='login'),
    url(r'^auth/$', views.user_login, name='auth'),
    url(r'^register/$', views.register, name='register'),
    url(r'^home/$', include('home.urls', namespace="home", app_name="home")),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^confirmation/$', views.confirmation, name='confirmation'),

    url(r'^createreport/$', views.createreport, name='createreport'),

    url(r'^managereports/$', views.managereports, name='managereports'),
    url(r'^viewreports/$', views.viewreports, name='viewreports'),

    url(r'^viewmessages/$', views.viewmessages, name='viewmessages'),
    url(r'^sendmessage/$', views.sendmessage, name='sendmessage'),
    url(r'^decryptmessage/(?P<message_pk>.*)$', views.decryptmessage, name='decryptmessage'),
    url(r'^deletemessage/(?P<message_pk>.*)$', views.deletemessage, name='deletemessage'),
    url(r'^deletesentmessages/$', views.deletesentmessages, name='deletesentmessages'),
    url(r'^deletereceivedmessages/$', views.deletereceivedmessages, name='deletereceivedmessages'),

    url(r'^managegroups/$', views.managegroups, name='managegroups'),
    url(r'^requestnewusertogroup/(?P<group_pk>.*)$', views.requestnewusertogroup, name='requestnewusertogroup'),
    url(r'^requestdeletefromgroup/(?P<group_pk>.*)$', views.requestdeletefromgroup, name='requestdeletefromgroup'),

    url(r'^creategroup/$', views.creategroup, name='creategroup'),
    url(r'^requestgroup/$', views.requestgroup, name='requestgroup'),

    url(r'^manageaccount/$', views.manageaccount, name='manageaccount'),
    url(r'^manageusersreports/$', views.manageusersreports, name='manageusersreports'),
    url(r'^grouppage/(?P<group_pk>.*)$', views.grouppage, name='grouppage'),
]
