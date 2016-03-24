from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	return render(request, 'secureshare/login.html')

def auth(request):
	if request.method == 'POST':
		usernameIn = request.POST.get('inputUsername', '')
		passwordIn = request.POST.get('inputPassword', '')
		user = authenticate(username=usernameIn, password=passwordIn)
		if user is not None:
			if user.is_active:
				return home(request)
				#print("User is valid, active, and authenticated")
			else:
				print("The password is valid, but the account has been disable")
		else:
			#return render(request, 'secureshare/failed.html')
			return home(request)
	return render(request, 'secureshare/failed.html')

def register(request):
	return render(request, 'secureshare/register.html')

def authregister(request):
	if request.method == 'POST':
		usernameIn = request.POST.get('inputUsername', '')
		emailIn = request.POST.get('inputEmail', '')
		passwordIn = request.POST.get('inputPassword', '')
		user = User.objects.create_user(usernameIn, emailIn, passwordIn)
		user.save()
		return login(request)


def home(request):
	if not request.user.is_authenticated():
		return render(request, 'secureshare/failed.html')
	return render(request, 'secureshare/home.html')