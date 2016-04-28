import requests
import os
import urllib
import urllib.request
import getpass
import django
import webbrowser
from time import sleep

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
# host = "https://radiant-peak-61887.herokuapp.com/"

key = 'i_love_srikanth!'

def decrypt_file(filename_input, symmetric_key):
    iv = b"1234567890123456" # Just some initialization vector
    AESkey = AES.new(symmetric_key, AES.MODE_CFB, iv)
    output_filename = filename_input[:-4] # remove '.enc' from filename
    with open(filename_input, 'rb') as f:
        raw_file = f.read()
        data_dec = AESkey.decrypt(raw_file)
    with open(output_filename, 'wb') as o:
        o.write(data_dec)
        print('Decrypted file written to: ' + output_filename)
    return True

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(host + '/secureshare/fdalogin/', data=payload)
    if not p.text == "Login successful.":
      print("Your credentials were incorrect.")
      exit()
    p1 = s.post(host + '/secureshare/fdaviewreports/', data=payload)
    print(p1.text)
    if p1.text == "You don't have any reports to view.":
      print("The FDA will now exit.")
      exit()

    reportid = input("Enter the ID of the report you wish to display: ")
    payload['reportid'] = reportid

    # p2 = s.post('http://127.0.0.1:8000/secureshare/fdadisplayreport/', data=payload)
    p2 = s.post(host + '/secureshare/fdadisplayreport/', data=payload)
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

      print("Confirming file downloads...")
      while True:
          file1Exist = False
          file2Exist = False
          file3Exist = False
          file4Exist = False
          file5Exist = False

          if not file1:
            file1Exist = True
          if not file2:
            file2Exist = True
          if not file3:
            file3Exist = True
          if not file4:
            file4Exist = True
          if not file5:
            file5Exist = True

          # directory = "/home/student/Downloads/"
          directory = "C:/Users/Srikanth/Desktop/"

          if file1:
            if os.path.isfile(directory + array[9].strip()[15:]):
              file1Exist = True
          if file2:
            if os.path.isfile(directory + array[10].strip()[15:]):
              file2Exist = True
          if file3:
            if os.path.isfile(directory + array[11].strip()[15:]):
              file3Exist = True
          if file4:
            if os.path.isfile(directory + array[12].strip()[15:]):
              file4Exist = True
          if file5:
            if os.path.isfile(directory + array[13].strip()[15:]):
              file5Exist = True

          if file1Exist and file2Exist and file3Exist and file4Exist and file5Exist:
            print("Done.")
            break

      encryptCheck = str(myList[7])
      if "True" in encryptCheck:
        # filename_input = "/home/student/Downloads/"
        filename_input = "C:/Users/Srikanth/Desktop/"
        if file1:
          filename_input1 = filename_input + array[9].strip()[15:]
          decrypt_file(filename_input1, key)
        if file2:
          filename_input2 = filename_input + array[10].strip()[15:]
          decrypt_file(filename_input2, key)
        if file3:
          filename_input3 = filename_input + array[11].strip()[15:]
          decrypt_file(filename_input3, key)
        if file4:
          filename_input4 = filename_input + array[12].strip()[15:]
          decrypt_file(filename_input4, key)
        if file5:
          filename_input5 = filename_input + array[13].strip()[15:]
          decrypt_file(filename_input5, key)
      exit()
    else:
      print("The FDA will now exit.")
      exit()