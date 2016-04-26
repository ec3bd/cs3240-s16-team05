import requests
import os
import urllib
import urllib.request
import getpass
import django
import webbrowser

# encryption/decryption, connect with heroku

from Crypto.PublicKey import RSA
from Crypto.Cipher import AES

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

key = 'i_love_srikanth!'

def decrypt_file(filename_input, symmetric_key):
    iv = b"1234567890123456" # Just some initialization vector
    AESkey = AES.new(symmetric_key, AES.MODE_CFB, iv)
    output_filename = "DEC_" + filename_input[:-4]
    with open(filename_input, 'rb') as f:
        raw_file = f.read()
        # print("reading file: " + str(raw_file) + " " + str(type(raw_file)))
        data_dec = AESkey.decrypt(raw_file)
        # print("data_dec: " + str(data_dec) + " " + str(type(data_dec)))
        # string = data_dec.decode("utf-8")
    with open(output_filename, 'wb') as o:
        #o.write(string)
        o.write(data_dec)
    return True

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
    parse2 = p2.text
    myList = parse2.split('\n')
    file1 = ""
    file2 = ""
    file3 = ""
    file4 = ""
    file5 = ""
    n = len(myList)
    n = n-1
    if(n >= 9):
        file1 = str(myList[9])
        file1 = file1[21:]
    if(n >= 10):
        file2 = str(myList[10])
        file2 = file2[21:]
    if(n >= 11):
        file3 = str(myList[11])
        file3 = file3[21:]
    if(n >= 12):
        file4 = str(myList[12])
        file4 = file4[21:]
    if(n >= 13):
        file5 = str(myList[13])
        file5 = file5[21:]
    toPrint = ""
    i = 0
    while i < 8:
        toPrint += (str(myList[i]) + '\n')
        i += 1
    toPrint += "   Files: \n" + "      " + (file1 + '\n') + "      " + (file2 + '\n') + "      " + (file3 + '\n') + "      " + (file4 + '\n') + "      " + (file5 + '\n')
    print(toPrint)

    download = input("\nWould you like to download the files of this report? (y/n) ")

    if download.strip() == "y":
      downloadurl = "/secureshare/requestfiledownload/"
      # downloadurl += reportid + "/files/"
      downloadurl += reportid + "/"
      array = parse.split('\n')

      if file1:
        downloadurl = "/secureshare/requestfiledownload/" + str(reportid) + "/" + str(array[9].strip())
        webbrowser.open(host + downloadurl)
      if file2:
        downloadurl = "/secureshare/requestfiledownload/" + str(reportid) + "/" + str(array[10].strip())
        webbrowser.open(host + downloadurl)
      if file3:
        downloadurl = "/secureshare/requestfiledownload/" + str(reportid) + "/" + str(array[11].strip())
        webbrowser.open(host + downloadurl)
      if file4:
        downloadurl = "/secureshare/requestfiledownload/" + str(reportid) + "/" + str(array[12].strip())
        webbrowser.open(host + downloadurl)
      if file5:
        downloadurl = "/secureshare/requestfiledownload/" + str(reportid) + "/" + str(array[13].strip())
        webbrowser.open(host + downloadurl)

      # print(str(myList[8]))
      encryptCheck = str(myList[7])
      if "True" in encryptCheck:

        filename_input = "/home/student/Downloads/"

        if file1:
          filename_input += array[9].strip()[15:]

          decrypt_file(filename_input, key)




        print("Decrypted.")

      exit()
    else:
      print("The FDA will now exit.")
      exit()