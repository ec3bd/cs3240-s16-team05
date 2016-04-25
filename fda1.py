import requests
import os
import urllib
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

import django
django.setup()

#if __name__ == "__main__":
#    url = 'http://127.0.0.1:8000/secureshare/'
#    values = {'username': 'user',
#              'password': 'pass'}
    
#    r = requests.post(url, data=values)
#    print(r.content)

username = input("Enter username: ")
password = input("Enter password: ")

payload = {
    'username': username,
    'password': password
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('http://127.0.0.1:8000/secureshare/fdalogin/', data=payload)
    #print(p.text)

    p1 = s.post('http://127.0.0.1:8000/secureshare/fdaviewreports/', data=payload)
    print(p1.text)

    reportid = input("Enter the ID of the report you wish to display: ")
    payload['reportid'] = reportid

    p2 = s.post('http://127.0.0.1:8000/secureshare/fdadisplayreport/', data=payload)
    parse = p2.text
    print(p2.text)

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
    download = input("\nWould you like to download the files of this report? (1 = yes, 2 = no) ")
    if download.strip() == "1":
      for url in temp:
        r = requests.get(url_front + url)
        #if not r.ok:
        #  print("An error occured. Try again later.")
        with open(url.split("/")[-1], "wb") as code:
          code.write(r.content)
      print("\n   Downloaded: ")
      print("   " + '\n'.join(x.split("/")[-1] for x in temp))



