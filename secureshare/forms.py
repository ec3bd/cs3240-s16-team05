from django import forms
from django.contrib.auth.models import User, Group
from secureshare.models import Report, UserProfile, UploadFile

# USERS
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture', 'siteManager')

# REPORTS
class ReportForm(forms.ModelForm):
  class Meta:
    model = Report
    fields = {'short_description', 'detailed_description', 'private'}
class UploadFileForm(forms.ModelForm):
  class Meta:
    model = UploadFile
    fields = '__all__'
class DocumentForm(forms.Form):
  docfile = forms.FileField(label='Select a file')

class UploadFileForm(forms.Form):
  title = forms.CharField(max_length=50)
  file = forms.FileField()
