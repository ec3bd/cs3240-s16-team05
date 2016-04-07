from django.shortcuts import render, render_to_response
from secureshare.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from secureshare.models import User, Document, UploadFile, Message
from secureshare.forms import UserForm, UserProfileForm, UploadFileForm, DocumentForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from Crypto.Cipher import AES
import datetime
import binascii

# For AES encryption/decryption
key = "7AqDiyLmzcjmPO7n"


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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/secureshare/home/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            return render(request, 'secureshare/failed.html')
    else:
        if(request.user.is_authenticated()):
            return HttpResponseRedirect('/secureshare/home/')
        return render(request, 'secureshare/login.html')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            return render(request, 'secureshare/failed.html')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
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


@login_required
def user_logout(request):
    logout(request)
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


'''
Adapted from GitHub
'''
class AESCipher:
    def __init__(self, key):
        self.key = bytes(key, encoding='utf-8')
        self.BLOCK_SIZE = 16
    def __pad(self, raw):
        if (len(raw) % self.BLOCK_SIZE == 0):
            return raw
        padding_required = self.BLOCK_SIZE - (len(raw) % self.BLOCK_SIZE)
        padChar = b'\x00'
        data = raw.encode('utf-8') + padding_required * padChar
        return data
    def __unpad(self, s):
        s = s.rstrip(b'\x00')
        return s
    def encrypt(self, raw):
        if (raw is None) or (len(raw) == 0):
            raise ValueError('input text cannot be null or empty set')
        raw = self.__pad(raw)
        cipher = AES.new(self.key[:32], AES.MODE_ECB)
        ciphertext = cipher.encrypt(raw)
        return  binascii.hexlify(bytearray(ciphertext)).decode('utf-8')
    def decrypt(self, enc):
        if (enc is None) or (len(enc) == 0):
            raise ValueError('input text cannot be null or empty set')
        enc = binascii.unhexlify(enc)
        cipher = AES.new(self.key[:32], AES.MODE_ECB)
        enc = self.__unpad(cipher.decrypt(enc))
        return enc.decode('utf-8')
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
        if message.sender == request.user:
            messageOut.append(message)
    return render(request, 'secureshare/view-messages.html', {'messageIn': messageIn, 'messageOut': messageOut,})
def sendmessage(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    if request.method == 'POST':
        recepient = request.POST.get('recepient')
        message = request.POST.get('message')
        encrypt = request.POST.get('encrypt')
        user = request.user
        if user.is_active:
            # Check if recepient exists
            listUser = User.objects.filter(username=recepient)
            if len(listUser) == 0:
                messageList = Message.objects.all()
                messageIn = []
                messageOut = []
                for message in messageList:
                    if message.receiver == request.user:
                        messageIn.append(message)
                    if message.sender == request.user:
                        messageOut.append(message)
                return render(request, 'secureshare/view-messages.html', {'messageIn': messageIn, 'messageOut': messageOut, 'message': "That user doesn't exist."})
            # Save to database
            recepientUser = User.objects.filter(username=recepient)[0]
            t = datetime.datetime.now()
            timeStr = str(t)[:-7]
            if encrypt == "encrypted":
                aesObj = AESCipher(key)
                encryptedMsg = aesObj.encrypt(message)
                msg = Message(sender=user, receiver=recepientUser, content=encryptedMsg, created_at=timeStr, encrypt=True)
            else:
                databaseMessage = message
                msg = Message(sender=user, receiver=recepientUser, content=databaseMessage, created_at=timeStr, encrypt=False)
            msg.save()

            return HttpResponseRedirect('/secureshare/viewmessages/')
        else:
            return render(request, 'secureshare/failed.html')
    else:
        if(request.user.is_authenticated()):
            return HttpResponseRedirect('/secureshare/home/')
        return render(request, 'secureshare/login.html')
def decryptmessage(request, message_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    message = Message.objects.filter(id=message_pk)[0]
    if message.encrypt:
        aesObj = AESCipher(key)
        decrypted = aesObj.decrypt(message.content)
        return HttpResponse(decrypted)
    else:
        return HttpResponse("That message was not encrypted. Go back to see the plaintext.")
def deletemessage(request, message_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    Message.objects.filter(id=message_pk).delete()
    return HttpResponseRedirect('/secureshare/viewmessages/')


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
    if not UserProfile.objects.get(user_id=request.user.id).siteManager:
        return render(request, 'securesshare/failed')
    return render(request, 'secureshare/manage-users-and-reports.html')

