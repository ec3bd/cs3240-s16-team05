import requests
import os
import urllib
import urllib.request
import getpass
import django
from splinter import Browser
from time import sleep
import webbrowser

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')
django.setup()

username = input("Enter username: ")
password = getpass.getpass('Enter a password to login: ')
payload = {
    'username': username,
    'password': password
}

host = "http://127.0.0.1:8000"
# host = ""

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(host + '/secureshare/fdalogin/', data=payload)
    if not p.text == "Login successful.":
      print("Your credentials were incorrect.")
      exit()
    p1 = s.post(host + '/secureshare/fdaviewreports/', data=payload)
    print(p1.text)

    reportid = input("Enter the ID of the report you wish to display: ")
    payload['reportid'] = reportid

    p2 = s.post('http://127.0.0.1:8000/secureshare/fdadisplayreport/', data=payload)
    parse = p2.text
    print(p2.text)

    download = input("\nWould you like to download the files of this report? (y/n) ")

    if download.strip() == "y":
      downloadurl = "/secureshare/requestfiledownload/"
      # downloadurl += reportid + "/files/"
      downloadurl += reportid + "/"
      array = parse.split('\n')
      downloadurl += str(array[9].strip())
      downloadurl = host + downloadurl
      print(downloadurl)

      webbrowser.open(downloadurl)

      # urllib.request.urlopen(downloadurl).read()

      # with Browser() as browser:
      #   browser.visit(host + downloadurl)
      #   sleep(100)

      exit()
    else:
      print("The FDA will now exit.")
      exit()












    parse = parse.split('\n')
    temp = []
    found = False
    for line in parse:
      if not found and line.strip() == "Files:":
        found = True
        continue
      if line.strip() in ["Private? False", "Private? True"]:
        break
      if found:
        temp.append(line.strip())

    url_front = "http://localhost:8000/secureshare/requestfiledownload/" + str(reportid) + "/"
    
    if download.strip() == "y":
      for url in temp:
        r = requests.get(url_front + url)
        #if not r.ok:
        #  print("An error occured. Try again later.")
        #  exit(0)
        with open(url.split("/")[-1], "wb") as code:
          code.write(r.content)
      print("\nDownloaded: ")
      print("   " + '\n'.join(x.split("/")[-1] for x in temp))



