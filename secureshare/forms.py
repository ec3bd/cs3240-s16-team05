from django import forms
from django import forms
from django.contrib.auth.models import User
from secureshare.models import UserProfile, UploadFile

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UploadFileForm(forms.ModelForm):
  class Meta:
    model = UploadFile
    fields = '__all__'

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
<<<<<<< HEAD
        fields = ('website', 'picture')

class DocumentForm(forms.Form):
  docfile = forms.FileField(
    label='Select a file'
  )

"""
class UploadFileForm(forms.ModelForm):
  title = forms.CharField(max_length=50)
  file = forms.FileField()
  """
=======
        fields = ('website', 'picture')
>>>>>>> adb205faf6c16a56a84bedca604ad3b94429db99
