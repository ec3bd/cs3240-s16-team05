from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	return render(request, 'secureshare/login.html')

def auth(request):
	if request.method == 'POST':
		username = request.POST.get('inputUsername', '')
		password = request.POST.get('inputPassword', '')
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				return home(request)
				#print("User is valid, active, and authenticated")
			else:
				print("The password is valid, but thea ccount has been disable")
		else:
			return render(request, 'secureshare/failed.html')
	return render(request, 'secureshare/failed.html')

@login_required
def home(request):
	if not request.user.is_authenticated():
		return render(request, 'secureshare/login.html', {'info': "We couldn't authenticate you. Sign in again."})
	return render(request, 'secureshare/home.html')