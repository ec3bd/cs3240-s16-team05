from django.shortcuts import render, render_to_response
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from secureshare.models import User, UserProfile, Message, Group, Report, GroupPage
from secureshare.forms import UserForm, UserProfileForm, ReportForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from django.core.urlresolvers import reverse
from Crypto.Cipher import AES
import datetime
import binascii
import mimetypes



def userlogin(request):
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
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})


def home(request):
    if not request.user.is_authenticated():
       return render(request, 'secureshare/failed.html')
    unreadMessageCount = len(Message.objects.filter(receiver=request.user, read=False))
    reportCount = len(Report.objects.filter(owner=request.user))
    siteManager = UserProfile.objects.get(user_id=request.user.id).siteManager
    return render(request, 'secureshare/home.html', {'unreadMessageCount': unreadMessageCount, 'reportCount': reportCount, 'siteManager': siteManager})


@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect('/secureshare/')


def createreport(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    if request.method == 'POST':
        report_form = ReportForm(request.POST or None, request.FILES or None)
        if report_form.is_valid():
            owner = request.user
            t = datetime.datetime.now()
            timeStr = str(t)[:-7]
            short_description = report_form.cleaned_data['short_description']
            detailed_description = report_form.cleaned_data['detailed_description']
            file1 = file2 = file3 = file4 = file5 = ''
            if 'file1' in request.FILES:
                file1 = request.FILES['file1']
            if 'file2' in request.FILES:
                file2 = request.FILES['file2']
            if 'file3' in request.FILES:
                file3 = request.FILES['file3']
            if 'file4' in request.FILES:
                file4 = request.FILES['file4']
            if 'file5' in request.FILES:
                file5 = request.FILES['file5']
            private = report_form.cleaned_data['private']
            encrypt = report_form.cleaned_data['encrypt']
            report = Report(
                owner=owner,
                created_at=timeStr,
                short_description=short_description,
                detailed_description=detailed_description,
                file1=file1,
                file2=file2,
                file3=file3,
                file4=file4,
                file5=file5,
                private=private,
                encrypt=encrypt,
            )
            report.save()
            return render(request, 'secureshare/create-report.html', {'report_form': report_form, 'message': "The report was successfully submitted."})
    else:
        report_form = ReportForm()
    return render(request, 'secureshare/create-report.html', {'report_form': report_form})

def managereports(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed')
    reportList = Report.objects.filter(owner=request.user)
    return render(request, 'secureshare/manage-reports.html', {'reportList': reportList})
def requestnewusertoreport(request, report_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    if request.method == 'POST':
        reportList = Report.objects.filter(owner=request.user)
        user = request.user
        report = Report.objects.filter(id=report_pk)[0]
        userToAddUsername = request.POST.get('user')
        userToAddList = User.objects.filter(username=userToAddUsername)
        if len(userToAddList) == 0:
            return render(request, 'secureshare/manage-reports.html', {'reportList': reportList, 'messageOne': 'Couldn\'t find that user.'})
        userToAdd = userToAddList[0]
        if userToAdd in report.auth_users.all():
            return render(request, 'secureshare/manage-reports.html', {'reportList': reportList, 'messageOne': "That user is already shared."})
        else:
            report.auth_users.add(userToAdd)
            return render(request, 'secureshare/manage-reports.html', {'reportList': reportList, 'messageOne': "Shared successfully."})
def requestdeletereport(request, report_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    report = Report.objects.filter(id=report_pk).delete()
    return HttpResponseRedirect('/secureshare/managereports/')
def reportpage(request, report_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    reportList = Report.objects.filter(id=report_pk)
    if len(reportList) == 0:
        return render(request, 'secureshare/report-page.html', {'message': "That report does not exist"})
    else:
        report = reportList[0]
        # CHECK TO SEE IF USER IS ALLOWED TO SEE REPORT HERE
        return render(request, 'secureshare/report-page.html', {'report': report})
def requesteditreport(request, report_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    if request.method == 'POST':
        report = Report.objects.filter(id=report_pk)[0]
        short_description = request.POST.get('shortdescription')
        detailed_description = request.POST.get('detaileddescription')
        user = request.user
        if user.is_active:
            if short_description != '':
                report.short_description = short_description
            if detailed_description != '':
                report.detailed_description = detailed_description
        return render(request, 'secureshare/report-page.html', {'report': report})
    else:
        return render(request, 'secureshare/report-page.html', {'report': report})


def viewreports(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    return render(request, 'secureshare/view-reports.html')
def requestfiledownload(request, report_pk, file_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    # Add check to see if report exists (for invalid URL)
    report_id = report_pk[0:report_pk.index("/")]
    file_directory = report_pk[report_pk.index("/"):] + "/"
    report = Report.objects.filter(id=report_id)[0]
    if not report.encrypt:
        fp = open(file_directory[1:] + file_pk, 'rb')
        response = HttpResponse(fp.read())
        fp.close()
        type, encoding = mimetypes.guess_type(file_pk)
        if type is None:
            type = 'application/octet-stream'
        response['Content-Type'] = type
        if encoding is not None:
            response['Content-Encoding'] = encoding
        if u'WebKit' in request.META['HTTP_USER_AGENT']:
            filename_header = 'filename=%s' % file_pk.encode('utf-8')
        elif u'MSIE' in request.META['HTTP_USER_AGENT']:
            filename_header = ''
        else:
            filename_header = 'filename*=UTF-8\'\'%s' & urllib.quote(original_filename.encode('utf-8'))
        filename_header = filename_header[2:] # fixes byte string output
        response['Content-Disposition'] = 'attachment; ' + filename_header
        return response
    return HttpResponseRedirect('/secureshare/viewreports/')




# For AES encryption/decryption
key = "7AqDiyLmzcjmPO7n"

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
    messageIn = Message.objects.filter(receiver=request.user)
    Message.objects.filter(receiver=request.user).update(read=True)
    messageOut = Message.objects.filter(sender=request.user)
    return render(request, 'secureshare/view-messages.html', {'messageIn': messageIn, 'messageOut': messageOut})
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
                msg = Message(sender=user, receiver=recepientUser, content=encryptedMsg, created_at=timeStr, encrypt=True, read=False)
            else:
                databaseMessage = message
                msg = Message(sender=user, receiver=recepientUser, content=databaseMessage, created_at=timeStr, encrypt=False, read=False)
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
        return HttpResponse(decrypted + "<br><br><a href='/secureshare/viewmessages/'>Go back</a>")
    else:
        return HttpResponse("That message was not encrypted. Go back to see the plaintext." + "<br><br><a href='/secureshare/viewmessages/'>Go back</a>")
def deletemessage(request, message_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    Message.objects.filter(id=message_pk).delete()
    return HttpResponseRedirect('/secureshare/viewmessages/')
def deletesentmessages(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    Message.objects.filter(sender=request.user).delete()
    return HttpResponseRedirect('/secureshare/viewmessages')
def deletereceivedmessages(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    Message.objects.filter(receiver=request.user).delete()
    return HttpResponseRedirect('/secureshare/viewmessages')

def managegroups(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    user = User.objects.filter(username=request.user)[0]
    groupList = user.groups.all()
    return render(request, 'secureshare/manage-groups.html', {'groupList': groupList})
def requestnewusertogroup(request, group_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    if request.method == 'POST':
        user = request.user
        groupList = user.groups.all()
        userToAddUsername = request.POST.get('user')
        userToAddList = User.objects.filter(username=userToAddUsername)
        if len(userToAddList) == 0:
            return render(request, 'secureshare/manage-groups.html', {'groupList': groupList, 'message': 'Couldn\'t find that user.'})
        userToAdd = userToAddList[0]
        if userToAdd.groups.filter(id=group_pk).exists():
            return render(request, 'secureshare/manage-groups.html', {'groupList': groupList, 'message': "That user is already a member."})
        else:
            group = Group.objects.filter(id=group_pk)[0]
            group.user_set.add(userToAdd)
            return render(request, 'secureshare/manage-groups.html', {'groupList': groupList, 'message': "Added successfully."})
def requestdeletefromgroup(request, group_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    group = Group.objects.filter(id=group_pk)[0]
    group.user_set.remove(request.user)
    return HttpResponseRedirect('/secureshare/managegroups/')

def creategroup(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    return render(request, 'secureshare/create-group.html')
def requestgroup(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    if request.method == 'POST':
        groupName = request.POST.get('groupName')
        user = request.user
        if user.is_active:
            groupList = Group.objects.filter(name=groupName)
            user = User.objects.filter(username=request.user)[0]
            if len(groupList) == 0: # Group does not exist
                group = Group(name=groupName)
                group.save()
                user.groups.add(group)
                return render(request, 'secureshare/create-group.html', {'message': "You have been added."})
            else:
                return render(request, 'secureshare/create-group.html', {'message': "That group already exists."})
        else:
            return render(request, 'secureshare/failed.html')
    else:
        return render(request, 'secureshare/failed.html')
def grouppage(request, group_pk):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    groupList = Group.objects.filter(name=group_pk)
    if len(groupList) == 0:
        return render(request, 'secureshare/group-page.html', {'message': "That group does not exist."})
    else:
        group = groupList[0]
        name = group.name
        members = group.user_set.all()
        if request.user in group.user_set.all():
            return render(request, 'secureshare/group-page.html', {'group': group, 'name': name, 'members': members})    
        else:
            return render(request, 'secureshare/group-page.html', {'message': "You are not authorized to see this group."})
        

def manageaccount(request):
    if not request.user.is_authenticated():
        return render(request, 'secureshare/failed.html')
    return render(request, 'secureshare/manage-account.html')


def manageusersreports(request):
    if not UserProfile.objects.get(user_id=request.user.id).siteManager:
        return render(request, 'secureshare/failed.html')
    return render(request, 'secureshare/manage-users-and-reports.html')