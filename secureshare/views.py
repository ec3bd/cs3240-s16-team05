from django.shortcuts import render, render_to_response
<<<<<<< HEAD
=======
from secureshare.models import UserProfile
from django.contrib.auth.models import User
from secureshare.models import Message
>>>>>>> c5da34a21763640b54087e27c7ab50be057b0521
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from secureshare.models import User, Document, UploadFile, Message
from secureshare.forms import UserForm, UserProfileForm, UploadFileForm, DocumentForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
import datetime

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('secureshare.views.home'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'secureshare/home.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )
    
def handle_uploaded_file(f):
  with open('write_file.txt', 'wb+') as dest:
    for chunk in f.chunks():
      destination.write(chunk)


def upload_file(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      inst = UploadFileForm(file_field=request.FILES['file'])
      inst.save()
      return HttpResponseRedirect('/success/url/')
  else:
    form = UploadFileForm()
  return render(request, 'upload.html', {'form': form})

def user_login(request):

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/secureshare/home/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'secureshare/failed.html')

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        if(request.user.is_authenticated()):
            return HttpResponseRedirect('/secureshare/home/')

        return render(request, 'secureshare/login.html', {})

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            return render(request, 'secureshare/failed.html')
            #print(user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'secureshare/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def authregister(request):
	if request.method == 'POST':
		usernameIn = request.POST.get('inputUsername', '')
		emailIn = request.POST.get('inputEmail', '')
		passwordIn = request.POST.get('inputPassword', '')
		user = User.objects.create_user(usernameIn, emailIn, passwordIn)
		user.save()
		return login(request)


def upload(request):
  if request.method == 'POST':
    form = UploadFileForm(request.POST, request.FILES)
    if form.is_valid():
      new_file = UploadFile(file = request.FILES['file'])
      new_file.save()
      return HttpResponseRedirect(reverse('main:upload'))
  else:
    form = UploadFileForm()

  data = {'form': form}
  return render_to_response('secureshare/upload.html', data, context_instance=RequestContext(request))

def confirmation(request):
	return render(request, 'secureshare/confirmation.html/')

def home(request):
	if not request.user.is_authenticated():
		return render(request, 'secureshare/failed.html')
	return render(request, 'secureshare/home.html', {'siteManager': UserProfile.objects.get(user_id=request.user.id).siteManager})

"""
# Use the login_required() decorator to ensure only those logged in can access the view.
"""
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/secureshare/')


def createreport(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    return render(request, 'secureshare/create-report.html')


def managereports(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed')
    return render(request, 'secureshare/manage-reports.html')


def viewreports(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed')
    return render(request, 'secureshare/view-reports.html')


def viewmessages(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    messageList = Message.objects.all()
    # Inbox/outbox
    messageIn = []
    messageOut = []
    for message in messageList:
        if message.receiver == request.user:
            messageIn.append(message)
        elif message.sender == request.user:
            messageOut.append(message)
    #return render(request, 'secureshare/view-messages.html', {'messageList': messageList, 'messageIn': messageIn, 'messageOut': messageOut,})
    return render(request, 'secureshare/view-messages.html', {'messageIn': messageIn, 'messageOut': messageOut,})
def sendmessage(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed')
    if request.method == 'POST':
        recepient = request.POST.get('recepient')
        message = request.POST.get('message')
        user = request.user
        if user.is_active:
            # Check if recepient exists
            listUser = User.objects.filter(username=recepient)
            if len(listUser) == 0:
                return render(request, 'secureshare/view-messages.html', {'message': "That user doesn't exist."})
            recepientUser = User.objects.filter(username=recepient)[0]

            # Save to database
            t = datetime.datetime.now()
            msg = Message(sender=user, receiver=recepientUser, content=message, created_at=t)
            msg.save()

            return HttpResponseRedirect('/secureshare/viewmessages/')
        else:
            return render(request, 'secureshare/failed')
    else:
        if(request.user.is_authenticated()):
            return HttpResponseRedirect('/secureshare/home/')
        return render(request, 'secureshare/login.html')

def managegroups(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed')
    return render(request, 'secureshare/manage-groups.html')


def creategroup(request):
    if not request.user.is_authenticated():
        return render(request, 'securesshare/failed')
    return render(request, 'secureshare/create-group.html')


def manageaccount(request):
    if not request.user.is_authenticated():
        return render(request, 'securesshare/failed')
    return render(request, 'secureshare/manage-account.html')


def manageusersreports(request):
    if not request.user.is_authenticated():
        return render(request, 'securesshare/failed')
    if not UserProfile.objects.get(user_id=request.user.id).siteManager:
        return render(request, 'securesshare/failed')
    return render(request, 'secureshare/manage-users-and-reports.html')
