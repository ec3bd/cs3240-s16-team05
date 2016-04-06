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

# REPORTS
class Report(models.Model):
  owner = models.ForeignKey(User, related_name="owner")
  created_at = models.TextField()
  short_description = models.CharField(max_length=200)
  detailed_description = models.TextField()
  # collection of files here
  private = models.BooleanField(default=False)
  # collection of user permissions
  # collection of group permissions
  # collection of tags  
# class Tag(models.Model):
#   word = models.CharField(max_length=35)
class UploadFile(models.Model):
  file = models.FileField(upload_to='files/%Y/%m/%d')
class Document(models.Model):
  docfile = models.FileField(upload_to='documents/%Y/%m/%d')
