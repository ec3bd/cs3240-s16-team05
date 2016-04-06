from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User, Group

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)
    siteManager = models.BooleanField(default=False)
    def __unicode__(self):
      return self.user.username

class UploadFile(models.Model):
  file = models.FileField(upload_to='files/%Y/%m/%d')

class Document(models.Model):
  docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Message(models.Model):
	sender = models.ForeignKey(User, related_name="sender")
	receiver = models.ForeignKey(User, related_name="receiver")
	content = models.TextField()
	created_at = models.TextField()
	encrypt = models.BooleanField(default=False)