import requests
import os
<<<<<<< HEAD
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'home.settings')

import django
django.setup()

#if __name__ == "__main__":
#    url = 'http://127.0.0.1:8000/secureshare/'
#    values = {'username': 'user',
#              'password': 'pass'}
    
#    r = requests.post(url, data=values)
#    print(r.content)


# Fill in your details here to be posted to the login form.
username = input("Enter username: ")
password = input("Enter password: ")

payload = {
    'username': username,
    'password': password
}

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post('http://127.0.0.1:8000/secureshare/fdalogin/', data=payload)
    print(p.text)

    p1 = s.post('http://127.0.0.1:8000/secureshare/fdaviewreports/', data=payload)
    print(p1.text)

    reportid = input("Enter the ID of the report you wish to display: ")
    payload['reportid'] = reportid

    p2 = s.post('http://127.0.0.1:8000/secureshare/fdadisplayreport/', data=payload)
    print(p2.text)

    #download = input("\nWould you like to download the files of this report? (1 = yes, 2 = no) ")
    #if download == 1:
        #p3 = s.post('http://127.0.0.1:8000/secureshare/fdadownloadreport/', data=payload)
        #print(p3.text)


    #p3 = s.post('http://127.0.0.1:8000/secureshare/managereports/', data=payload)
    #print(p3.text)


=======

user = input("Username: ")
passw = input("Password: ")
payload = {'username': user, 'password': passw}
with requests.Session() as s:
   # go to the login page and login with the username and password provided
   p =  s.post('http://localhost:8000/secureshare/login/', data=payload)
   print(p.text)
   print(p.content)
   print(p.url)
   # the url isn't redirecting to /home like it should

   # now how to download a file and list the reports of the site?
   print("for testing: ")
   g = s.post('http://localhost:8000/secureshare/manage-reports/')
   print(g.text)
   """ to download using requests
      r = requests.get(url)
      with open("code.zip", "wb") as code:
        code.write(r.content)
   """
   #g = s.post('http://localhost:8000/secureshare/manage-reports/')
  
  

def get_files(dir):
  file_paths = []
  for root, dirs, files in os.walk(dir):
    for fname in files:
      filepath = os.path.join(root, fname)
      file_paths.append(filepath)

  return file_paths

# full_paths = get_filepaths("/Marina/Desktop")
>>>>>>> f539ee815ad27f7690a7f95f80c7cbf3b66e1195
