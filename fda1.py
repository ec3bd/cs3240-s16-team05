import requests
import os

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
