import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

import django
django.setup()

from secureshare.models import Report
from django.contrib.auth import authenticate, login


import urllib.request
#import urllib2

if __name__ == "__main__":
    username = ''
    password = ''
    username = input('Enter a username to login: ')
    password = input('Enter a password to login: ')
    user = authenticate(username=username, password=password)
    if user:
        if user.is_active:
            reportList = Report.objects.filter(owner=user)
            print("These are the reports that are available to you: ")
            for report in reportList:
                print("Report ID: " + str(report.id) + "\n   Short description: " + report.short_description + "\n   Encrypted = " + str(report.encrypt) + "\n")
            reportid = input("Enter the ID of the report you wish to display: ")
            report1 = None;
            file1 = None;
            file2 = None;
            file3 = None;
            file4 = None;
            file5 = None;
            for report1 in reportList:
                if report1.id == int(reportid):
                    print("Report ID: " + str(report1.id) + 
                      "\n   Created at: " + str(report1.created_at) + 
                      "\n   Owner: " + report1.owner.username + 
                      "\n   Short description: " + report1.short_description + 
                      "\n   Detailed description: " + report1.detailed_description +
                      "\n   Files: ")
                    if not report1.file1 and not report1.file2 and not report1.file3 and not report1.file4 and not report1.file5:
                        print("      This report doesn't have any files")
                    else:
                        if report1.file1: 
                            file1 = str(report1.file1)
                            print("      "+str(report1.file1))
                        if report1.file2: 
                            file2 = str(report1.file2)
                            print("      "+str(report1.file2))
                        if report1.file3: 
                            file3 = str(report1.file3)
                            print("      "+str(report1.file3))
                        if report1.file4: 
                            file4 = str(report1.file4)
                            print("      "+str(report1.file4))
                        if report1.file5: 
                            file5 = str(report1.file5)
                            print("      "+str(report1.file5))
                    print("   Private? " + str(report1.private) +
                     "\n   Encrypted? " + str(report1.encrypt))
                    break
            if not report1:
                print("Could not find a matching report.")
            else:
                download = input("\nWould you like to download the files of this report? (1 = yes, 2 = no) ")
                if int(download) == 1:
                    print("hi")
#                    url1 = "http://127.0.0.1:8000/secureshare/requestfiledownload/2/" + file1
#                    f = urllib2.urlopen(url1)
#                    data = f.read()
#                    with open("downloadworked.txt", "wb") as code:
#                        code.write(data)
                    url1 = "http://127.0.0.1:8000/secureshare/requestfiledownload/2/" + file1
                    urllib.request.urlretrieve(url1, "downloadworked.txt")

        else:
            print("Your account is disabled.")
    else:
        print("Login failed.")
    
    
