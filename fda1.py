import requests
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

import django
django.setup()

#if __name__ == "__main__":
#    url = 'http://127.0.0.1:8000/secureshare/'
#    values = {'username': 'user',
#              'password': 'pass'}
    
#    r = requests.post(url, data=values)
#    print(r.content)

#username = input("Enter username: ")
#password = input("Enter password: ")

payload = {
    'username': "test1",
    'password': "password"
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

    print( str(temp))
    url_front = "localhost:8000/secureshare/requestfiledownload/" + str(reportid) + "/"
    for url in temp:
      r = requests.get(url_front + url)
      with open(url, "wb") as code:
        code.write(r.content)
    #download = input("\nWould you like to download the files of this report? (1 = yes, 2 = no) ")
    #if download == 1:
        #p3 = s.post('http://127.0.0.1:8000/secureshare/fdadownloadreport/', data=payload)
        #print(p3.text)


    #p3 = s.post('http://127.0.0.1:8000/secureshare/managereports/', data=payload)
    #print(p3.text)


