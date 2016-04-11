from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group

# USERS
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    siteManager = models.BooleanField(default=False)
    def __unicode__(self):
      return self.user.username

# MESSAGES
class Message(models.Model):
  sender = models.ForeignKey(User, related_name="sender")
  receiver = models.ForeignKey(User, related_name="receiver")
  content = models.TextField()
  created_at = models.TextField()
  encrypt = models.BooleanField(default=False)
  read = models.BooleanField(default=False)

# REPORTS
class Report(models.Model):
  owner = models.ForeignKey(User, related_name="owner")
  created_at = models.TextField()
  short_description = models.CharField(max_length=200)
  detailed_description = models.TextField()
  upload_path = 'files/' + '%Y%m%d'
  file1 = models.FileField(upload_to=upload_path, null=True)
  file2 = models.FileField(upload_to=upload_path, null=True)
  file3 = models.FileField(upload_to=upload_path, null=True)
  file4 = models.FileField(upload_to=upload_path, null=True)
  file5 = models.FileField(upload_to=upload_path, null=True)
  private = models.BooleanField(default=False)
  encrypt = models.BooleanField(default=False)
  # collection of user permissions
  auth_users = models.ManyToManyField(User)
  # collection of group permissions
  auth_groups = models.ManyToManyField(Group)
  # collection of tags  
# class Tag(models.Model):
#   word = models.CharField(max_length=35)


class GroupPage(models.Model):
    group = models.OneToOneField(Group)
    url = models.URLField(blank=True)
    #add a list of reports associated with that group
    def __unicode__(self):
        return self.group.name
