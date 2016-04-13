from django import forms
from django.contrib.auth.models import User, Group
from secureshare.models import Report, UserProfile

#test

# USERS
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = UserProfile
        fields = ('password2','website', 'picture', 'siteManager')
class PasswordChangeForm(forms.Form):
    oldPassword = forms.CharField(widget=forms.PasswordInput())
    newPassword = forms.CharField(widget=forms.PasswordInput())

# REPORTS
class ReportForm(forms.ModelForm):
  file1 = forms.FileField(required=False)
  file2 = forms.FileField(required=False)
  file3 = forms.FileField(required=False)
  file4 = forms.FileField(required=False)
  file5 = forms.FileField(required=False)
  class Meta:
    model = Report
    fields = {'short_description', 'detailed_description', 'file1', 'file2', 'file3', 'file4', 'file5', 'private', 'encrypt'}
