from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
<<<<<<< HEAD
        return self.user.username

class UploadFile(models.Model):
  file = models.FileField(upload_to='files/%Y/%m/%d')

class Document(models.Model):
  docfile = models.FileField(upload_to='documents/%Y/%m/%d')
=======
        return self.user

class Message(models.Model):
	sender = models.ForeignKey(User, related_name="sender")
	receiver = models.ForeignKey(User, related_name="receiver")
	content = models.TextField()
	created_at = models.TimeField()
>>>>>>> adb205faf6c16a56a84bedca604ad3b94429db99
