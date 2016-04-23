from django.conf.urls import include, patterns, url
from secureshare import views

urlpatterns = [
    url(r'^$', views.userlogin, name='login'),
    url(r'^auth/$', views.userlogin, name='auth'),
    url(r'^register/$', views.register, name='register'),
    # url(r'^home/$', include('home.urls', namespace="home", app_name="home")),
    url(r'^home/', views.home, name='home'),
    url(r'^login/$', views.userlogin, name='login'),
    url(r'^fdalogin/$', views.fdalogin, name='fdalogin'),
    url(r'^logout/$', views.userlogout, name='logout'),

    url(r'^createreport/$', views.createreport, name='createreport'),
    url(r'^fda_reports/$', views.fda_reports, name='fda_reports'),
    url(r'^managereports/$', views.managereports, name='managereports'),
    url(r'^requestnewusertoreport/(?P<report_pk>.*)$', views.requestnewusertoreport, name='requestnewusertoreport'),

    url(r'^reportpage/(?P<report_pk>.*)$', views.reportpage, name='reportpage'),
    url(r'^requestdeletereport/(?P<report_pk>.*)$', views.requestdeletereport, name='requestdeletereport'),
    url(r'^requesteditreport/(?P<report_pk>.*)$', views.requesteditreport, name='requesteditreport'),

    url(r'^searchreports/$', views.searchreports, name='searchreports'),

    url(r'^managefolders/$', views.managefolders, name='managefolders'),
    url(r'^requestcreatefolder/$', views.requestcreatefolder, name='requestcreatefolder'),
    url(r'^requestaddtofolder/(?P<report_pk>.*)$', views.requestaddtofolder, name='requestaddtofolder'),
    url(r'^requestdeletefolder/(?P<folder_pk>.*)$', views.requestdeletefolder, name='requestdeletefolder'),
    url(r'^requestremovefromfolder/(?P<folder_pk>.*)/(?P<report_pk>.*)$', views.requestremovefromfolder, name='requestremovefromfolder'),

    url(r'^viewreports/$', views.viewreports, name='viewreports'),
    # url(r'^requestfiledownload/(?P<report_pk>.*)$', views.requestfiledownload, name='requestfiledownload'),
    url(r'^requestfiledownload/(?P<report_pk>.*)/(?P<file_pk>.*)$', views.requestfiledownload, name='requestfiledownload'),
    # Files should not be able to be accessed via the web application, hence we provide no URL

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
    url(r'^removeuserfromgroup/(?P<group_pk>.*)/(?P<user_pk>.*)$', views.removeuserfromgroup, name='removeuserfromgroup'),

    url(r'^manageaccount/$', views.manageaccount, name='manageaccount'),
    url(r'^manageusersreports/$', views.manageusersreports, name='manageusersreports'),
    url(r'^requestedituser/(?P<user_pk>.*)$', views.requestedituser, name='requestedituser'),
    url(r'^userprofile/(?P<user_pk>.*)$', views.userprofile, name='userprofile'),
    url(r'^grouppage/(?P<group_pk>.*)$', views.grouppage, name='grouppage'),
    url(r'^deactivateuser/(?P<user_pk>.*)$', views.deactivateuser, name='deactivateuser'),
    url(r'^activateuser/(?P<user_pk>.*)$', views.activateuser, name='activateuser'),
    url(r'^searchusers/$', views.searchusers, name='searchusers'),

    url(r'^fdalogin/$', views.fdalogin, name='fdalogin'),
    url(r'^fdaviewreports/$', views.fdaviewreports, name='fdaviewreports'),
    url(r'^fdadisplayreport/$', views.fdadisplayreport, name='fdadisplayreport'),

]
