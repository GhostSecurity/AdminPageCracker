import requests
from datetime import datetime
import os
import httplib
import colorama
import time
import urllib2
import sys
from termcolor import colored
from colorama import Fore, Back, Style
colorama.init()
ADMIN_FINDER_VERSION = '1.1'
gen_headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
		   	  'Accept-Language':'en-US;',
		   	  'Accept-Encoding': 'gzip, deflate',
		   	  'Accept': 'text/html,application/xhtml+xml,application/xml;',
		   	  'Connection':'close'}

pg1 = 0
pg2 = 0

php = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.php','admin/index.php','admin/login.php','admin/admin.php','admin/account.php',
'admin_area/admin.php','admin_area/login.php','siteadmin/login.php','siteadmin/index.php','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.php','bb-admin/index.php','bb-admin/login.php','bb-admin/admin.php','admin/home.php','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.php','admin.php','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.php','cp.php','administrator/index.php','administrator/login.php','nsw/admin/login.php','webadmin/login.php','admin/admin_login.php','admin_login.php',
'administrator/account.php','administrator.php','admin_area/admin.html','pages/admin/admin-login.php','admin/admin-login.php','admin-login.php',
'bb-admin/index.html','bb-admin/login.html','acceso.php','bb-admin/admin.html','admin/home.html','login.php','modelsearch/login.php','moderator.php','moderator/login.php',
'moderator/admin.php','account.php','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.php','admincontrol.php',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.php','adminarea/index.html','adminarea/admin.html',
'webadmin.php','webadmin/index.php','webadmin/admin.php','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.php','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.php','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.php','wp-login.php','adminLogin.php','admin/adminLogin.php','home.php','admin.php','adminarea/index.php',
'adminarea/admin.php','adminarea/login.php','panel-administracion/index.php','panel-administracion/admin.php','modelsearch/index.php',
'modelsearch/admin.php','admincontrol/login.php','adm/admloginuser.php','admloginuser.php','admin2.php','admin2/login.php','admin2/index.php','usuarios/login.php',
'adm/index.php','adm.php','affiliate.php','adm_auth.php','memberadmin.php','administratorlogin.php']

asp = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','account.asp','admin/account.asp','admin/index.asp','admin/login.asp','admin/admin.asp',
'admin_area/admin.asp','admin_area/login.asp','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/admin.html','admin_area/login.html','admin_area/index.html','admin_area/index.asp','bb-admin/index.asp','bb-admin/login.asp','bb-admin/admin.asp',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','admin/controlpanel.html','admin.html','admin/cp.html','cp.html',
'administrator/index.html','administrator/login.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html','moderator.html',
'moderator/login.html','moderator/admin.html','account.html','controlpanel.html','admincontrol.html','admin_login.html','panel-administracion/login.html',
'admin/home.asp','admin/controlpanel.asp','admin.asp','pages/admin/admin-login.asp','admin/admin-login.asp','admin-login.asp','admin/cp.asp','cp.asp',
'administrator/account.asp','administrator.asp','acceso.asp','login.asp','modelsearch/login.asp','moderator.asp','moderator/login.asp','administrator/login.asp',
'moderator/admin.asp','controlpanel.asp','admin/account.html','adminpanel.html','webadmin.html','pages/admin/admin-login.html','admin/admin-login.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','user.asp','user.html','admincp/index.asp','admincp/login.asp','admincp/index.html',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','adminarea/index.html','adminarea/admin.html','adminarea/login.html',
'panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html','admin/admin_login.html',
'admincontrol/login.html','adm/index.html','adm.html','admincontrol.asp','admin/account.asp','adminpanel.asp','webadmin.asp','webadmin/index.asp',
'webadmin/admin.asp','webadmin/login.asp','admin/admin_login.asp','admin_login.asp','panel-administracion/login.asp','adminLogin.asp',
'admin/adminLogin.asp','home.asp','admin.asp','adminarea/index.asp','adminarea/admin.asp','adminarea/login.asp','admin-login.html',
'panel-administracion/index.asp','panel-administracion/admin.asp','modelsearch/index.asp','modelsearch/admin.asp','administrator/index.asp',
'admincontrol/login.asp','adm/admloginuser.asp','admloginuser.asp','admin2.asp','admin2/login.asp','admin2/index.asp','adm/index.asp',
'adm.asp','affiliate.asp','adm_auth.asp','memberadmin.asp','administratorlogin.asp','siteadmin/login.asp','siteadmin/index.asp','siteadmin/login.html']

cfm = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cfm','admin/index.cfm','admin/login.cfm','admin/admin.cfm','admin/account.cfm',
'admin_area/admin.cfm','admin_area/login.cfm','siteadmin/login.cfm','siteadmin/index.cfm','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cfm','bb-admin/index.cfm','bb-admin/login.cfm','bb-admin/admin.cfm','admin/home.cfm','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cfm','admin.cfm','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cfm','cp.cfm','administrator/index.cfm','administrator/login.cfm','nsw/admin/login.cfm','webadmin/login.cfm','admin/admin_login.cfm','admin_login.cfm',
'administrator/account.cfm','administrator.cfm','admin_area/admin.html','pages/admin/admin-login.cfm','admin/admin-login.cfm','admin-login.cfm',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cfm','modelsearch/login.cfm','moderator.cfm','moderator/login.cfm',
'moderator/admin.cfm','account.cfm','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cfm','admincontrol.cfm',
'admin/adminLogin.html','acceso.cfm','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cfm','adminarea/index.html','adminarea/admin.html',
'webadmin.cfm','webadmin/index.cfm','webadmin/admin.cfm','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cfm','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cfm','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cfm','wp-login.cfm','adminLogin.cfm','admin/adminLogin.cfm','home.cfm','admin.cfm','adminarea/index.cfm',
'adminarea/admin.cfm','adminarea/login.cfm','panel-administracion/index.cfm','panel-administracion/admin.cfm','modelsearch/index.cfm',
'modelsearch/admin.cfm','admincontrol/login.cfm','adm/admloginuser.cfm','admloginuser.cfm','admin2.cfm','admin2/login.cfm','admin2/index.cfm','usuarios/login.cfm',
'adm/index.cfm','adm.cfm','affiliate.cfm','adm_auth.cfm','memberadmin.cfm','administratorlogin.cfm']

js = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.js','admin/index.js','admin/login.js','admin/admin.js','admin/account.js',
'admin_area/admin.js','admin_area/login.js','siteadmin/login.js','siteadmin/index.js','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.js','bb-admin/index.js','bb-admin/login.js','bb-admin/admin.js','admin/home.js','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.js','admin.js','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.js','cp.js','administrator/index.js','administrator/login.js','nsw/admin/login.js','webadmin/login.js','admin/admin_login.js','admin_login.js',
'administrator/account.js','administrator.js','admin_area/admin.html','pages/admin/admin-login.js','admin/admin-login.js','admin-login.js',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.js','modelsearch/login.js','moderator.js','moderator/login.js',
'moderator/admin.js','account.js','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.js','admincontrol.js',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.js','adminarea/index.html','adminarea/admin.html',
'webadmin.js','webadmin/index.js','acceso.js','webadmin/admin.js','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.js','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.js','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.js','wp-login.js','adminLogin.js','admin/adminLogin.js','home.js','admin.js','adminarea/index.js',
'adminarea/admin.js','adminarea/login.js','panel-administracion/index.js','panel-administracion/admin.js','modelsearch/index.js',
'modelsearch/admin.js','admincontrol/login.js','adm/admloginuser.js','admloginuser.js','admin2.js','admin2/login.js','admin2/index.js','usuarios/login.js',
'adm/index.js','adm.js','affiliate.js','adm_auth.js','memberadmin.js','administratorlogin.js']

cgi = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.cgi','admin/index.cgi','admin/login.cgi','admin/admin.cgi','admin/account.cgi',
'admin_area/admin.cgi','admin_area/login.cgi','siteadmin/login.cgi','siteadmin/index.cgi','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.cgi','bb-admin/index.cgi','bb-admin/login.cgi','bb-admin/admin.cgi','admin/home.cgi','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.cgi','admin.cgi','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.cgi','cp.cgi','administrator/index.cgi','administrator/login.cgi','nsw/admin/login.cgi','webadmin/login.cgi','admin/admin_login.cgi','admin_login.cgi',
'administrator/account.cgi','administrator.cgi','admin_area/admin.html','pages/admin/admin-login.cgi','admin/admin-login.cgi','admin-login.cgi',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.cgi','modelsearch/login.cgi','moderator.cgi','moderator/login.cgi',
'moderator/admin.cgi','account.cgi','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.cgi','admincontrol.cgi',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.cgi','adminarea/index.html','adminarea/admin.html',
'webadmin.cgi','webadmin/index.cgi','acceso.cgi','webadmin/admin.cgi','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.cgi','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.cgi','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.cgi','wp-login.cgi','adminLogin.cgi','admin/adminLogin.cgi','home.cgi','admin.cgi','adminarea/index.cgi',
'adminarea/admin.cgi','adminarea/login.cgi','panel-administracion/index.cgi','panel-administracion/admin.cgi','modelsearch/index.cgi',
'modelsearch/admin.cgi','admincontrol/login.cgi','adm/admloginuser.cgi','admloginuser.cgi','admin2.cgi','admin2/login.cgi','admin2/index.cgi','usuarios/login.cgi',
'adm/index.cgi','adm.cgi','affiliate.cgi','adm_auth.cgi','memberadmin.cgi','administratorlogin.cgi']

brf = ['admin/','administrator/','admin1/','admin2/','admin3/','admin4/','admin5/','usuarios/','usuario/','administrator/','moderator/','webadmin/','adminarea/','bb-admin/','adminLogin/','admin_area/','panel-administracion/','instadmin/',
'memberadmin/','administratorlogin/','adm/','admin/account.brf','admin/index.brf','admin/login.brf','admin/admin.brf','admin/account.brf',
'admin_area/admin.brf','admin_area/login.brf','siteadmin/login.brf','siteadmin/index.brf','siteadmin/login.html','admin/account.html','admin/index.html','admin/login.html','admin/admin.html',
'admin_area/index.brf','bb-admin/index.brf','bb-admin/login.brf','bb-admin/admin.brf','admin/home.brf','admin_area/login.html','admin_area/index.html',
'admin/controlpanel.brf','admin.brf','admincp/index.asp','admincp/login.asp','admincp/index.html','admin/account.html','adminpanel.html','webadmin.html',
'webadmin/index.html','webadmin/admin.html','webadmin/login.html','admin/admin_login.html','admin_login.html','panel-administracion/login.html',
'admin/cp.brf','cp.brf','administrator/index.brf','administrator/login.brf','nsw/admin/login.brf','webadmin/login.brfbrf','admin/admin_login.brf','admin_login.brf',
'administrator/account.brf','administrator.brf','acceso.brf','admin_area/admin.html','pages/admin/admin-login.brf','admin/admin-login.brf','admin-login.brf',
'bb-admin/index.html','bb-admin/login.html','bb-admin/admin.html','admin/home.html','login.brf','modelsearch/login.brf','moderator.brf','moderator/login.brf',
'moderator/admin.brf','account.brf','pages/admin/admin-login.html','admin/admin-login.html','admin-login.html','controlpanel.brf','admincontrol.brf',
'admin/adminLogin.html','adminLogin.html','admin/adminLogin.html','home.html','rcjakar/admin/login.brf','adminarea/index.html','adminarea/admin.html',
'webadmin.brf','webadmin/index.brf','webadmin/admin.brf','admin/controlpanel.html','admin.html','admin/cp.html','cp.html','adminpanel.brf','moderator.html',
'administrator/index.html','administrator/login.html','user.html','administrator/account.html','administrator.html','login.html','modelsearch/login.html',
'moderator/login.html','adminarea/login.html','panel-administracion/index.html','panel-administracion/admin.html','modelsearch/index.html','modelsearch/admin.html',
'admincontrol/login.html','adm/index.html','adm.html','moderator/admin.html','user.brf','account.html','controlpanel.html','admincontrol.html',
'panel-administracion/login.brf','wp-login.brf','adminLogin.brf','admin/adminLogin.brf','home.brf','admin.brf','adminarea/index.brf',
'adminarea/admin.brf','adminarea/login.brf','panel-administracion/index.brf','panel-administracion/admin.brf','modelsearch/index.brf',
'modelsearch/admin.brf','admincontrol/login.brf','adm/admloginuser.brf','admloginuser.brf','admin2.brf','admin2/login.brf','admin2/index.brf','usuarios/login.brf',
'adm/index.brf','adm.brf','affiliate.brf','adm_auth.brf','memberadmin.brf','administratorlogin.brf']


def Welcome():
    print (Fore.GREEN+"""
    ################################
    #                              #
    #    Brute Force Admin Page    #
    #              &               #
    #         Admin Finder         #
    #      Creator : HydraBoy      #
    #                              #
    ################################
    """)
def download(file_url,local_filename):
	web_file = urllib.urlopen(file_url)
	local_file = open(local_filename, 'w')
	local_file.write(web_file.read())
	web_file.close()
	local_file.close()

def Find(resp, toFind):
	if(len(toFind) > len(resp)):
		return []

	found = False
	indexes = []

	for x in range(0,(len(resp)-len(toFind))+1):
		if(ord(resp[x]) == ord(toFind[0])):
			found = True
			for i in range(0,len(toFind)):
				if(ord(resp[x+i]) != ord(toFind[i])):
					found = False
					break
		if(found):
			indexes.append(x)
			found = False
			x += len(toFind)

	return indexes

def check_for_update():
    admin_github_url = "https://github.com/HydraBoy/AdminPageCracker"
    keyword = "ADMIN_FINDER_VERSION = '"
    updated = False
    print "\n[*] Checking for [ADMIN FINDER] updates.."
    time.sleep(1)
    try:
        http = urllib2.urlopen('https://raw.githubusercontent.com/HydraBoy/AdminPageCracker/master/version.txt',data=None)
        content = http.read()
        read = open('version.txt','r').read()
        print read,content
        if read == content:
            print '[#] No updates available.'
        else:
            print '[+] Updating AdminPage Tool...'
            os.popen("git pull "+ admin_github_url)
            print '[+] AdminPage Tool Updated To Version: ' + content
            updated = True


    except Exception as ex:
        print "\n[!] Problem while updating."
    if updated:
        sys.exit(0)


def FindPassword(word, url):
    wordlist = open (word,'r').readlines()
    for line in wordlist:
        password = line.strip()
        http = requests.post(url, data={'username':user,'password':password,'submit':'submit'})
        content = http.content.decode('utf-8')
        print(Fore.GREEN+"[#] Checking Password: [" + str(password)+ "]")
        if "Welcome" in content:
            print (Fore.RED+'[+] Password Found : '+ password)
            break
        else :
            print ('[!] Password Not Found : '+ password)

    print (Fore.GREEN + 'Scan Ended ')

def IsUrl(source,url):
    if 'https://' not in str(url):
        if 'http://' in str(url):
            urls = url.replace('http://','')
            ScanToFind(source,urls)
        else:

            ScanToFind(source,url)
    else:
        if 'http://' not in str(url):
            if 'https://' in str(url):
                urls = url.replace('https://','')
                ScanToFind(source,urls)
            else:
                ScanToFind(source,url)

def ScanToFind(source,url):
    if str(source) == 'php':
        for pages in php:
            pages = pages.replace("\n","")
            pages = "/" + pages
            found = url + pages
            print (Fore.GREEN+"[#] Checking Site: [http://" + found + "]")
            connection = httplib.HTTPConnection(url)
            connection.request("GET",pages)
            response = connection.getresponse()
            if response.status == 200:
                print(Fore.RED+"Error Code: 200 [+] Admin Page Founded: " +  str(found))
                raw_input(Fore.GREEN+"[!] Press Enter To Continue.")
            elif response.status == 302:
                print(Fore.YELLOW+"Error Code: 302"),
            elif response.status == 404:
                print 'Error Code: 404',
            connection.close()
        print(Fore.GREEN+" [#] Scan Completed.")
        raw_input(Fore.YELLOW+"[#] Press Enter to Exit.")
        exit(0)
    elif str(source) == 'asp':
        for pages in asp:
            pages = pages.replace("\n","")
            pages = "/" + pages
            found = url + pages
            print (Fore.GREEN+"[#] Checking Site: [http://" + found + "]")
            connection = httplib.HTTPConnection(url)
            connection.request("GET",pages)
            response = connection.getresponse()
            if response.status == 200:
                print(Fore.RED+"[+] Admin Page Founded: " +  str(found))
                raw_input(Fore.GREEN+"[!] Press Enter To Continue.")
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + found, "Possible admin page (302 - Redirect)")
            elif response.status == 404:
                print 'Error Code: 404',
            connection.close()
        print(Fore.GREEN+" [#] Scan Completed.")
        print(Fore.GREEN+"[#] Total Admin Pages: " + pg1)
        raw_input(Fore.YELLOW+"[#] Press Enter to Exit.")
        exit(0)
    elif str(source) == 'cfm':
        for pages in cfm:
            pages = pages.replace("\n","")
            pages = "/" + pages
            found = url + pages
            print (Fore.GREEN+"\t [#] Checking Site: [http://" + found + "]")
            connection = httplib.HTTPConnection(url)
            connection.request("GET",pages)
            response = connection.getresponse()
            if response.status == 200:
                print(Fore.RED+"[+] Admin Page Founded: " +  str(found))
                raw_input(Fore.GREEN+"[!] Press Enter To Continue.")
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + found, "Possible admin page (302 - Redirect)")
            elif response.status == 404:
                print 'Error Code: 404',
            connection.close()
        print(Fore.GREEN+" [#] Scan Completed.")
        print(Fore.GREEN+"[#] Total Admin Pages: " + pg1)
        raw_input(Fore.YELLOW+"[#] Press Enter to Exit.")
        exit(0)
    elif str(source) == 'js':
        for pages in js:
            pages = pages.replace("\n","")
            pages = "/" + pages
            found = url + pages
            print (Fore.GREEN+"\t [#] Checking Site: [http://" + found + "]")
            connection = httplib.HTTPConnection(url)
            connection.request("GET",pages)
            response = connection.getresponse()
            if response.status == 200:
                pg1 = pg1 + 1
                print(Fore.RED+"[+] Admin Page Founded: " +  str(found))
                raw_input(Fore.GREEN+"[!] Press Enter To Continue.")
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + found, "Possible admin page (302 - Redirect)")
            elif response.status == 404:
                print 'Error Code: 404',
            connection.close()
        print(Fore.GREEN+" [#] Scan Completed.")
        print(Fore.GREEN+"[#] Total Admin Pages: " + pg1)
        raw_input(Fore.YELLOW+"[#] Press Enter to Exit.")
        exit(0)
    elif str(source) == 'cgi':
        for pages in cgi:
            pages = pages.replace("\n","")
            pages = "/" + pages
            found = url + pages
            print (Fore.GREEN+"\t [#] Checking Site: [http://" + found + "]")
            connection = httplib.HTTPConnection(url)
            connection.request("GET",pages)
            response = connection.getresponse()
            if response.status == 200:
                print(Fore.RED+"[+] Admin Page Founded: " +  str(found))
                raw_input(Fore.GREEN+"[!] Press Enter To Continue.")
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + found, "Possible admin page (302 - Redirect)")
            elif response.status == 404:
                print 'Error Code: 404',
            connection.close()
        print(Fore.GREEN+" [#] Scan Completed.")
        print(Fore.GREEN+"[#] Total Admin Pages: " + pg1)
        raw_input(Fore.YELLOW+"[#] Press Enter to Exit.")
        exit(0)
    elif str(source) == 'brf':
        for pages in brf:
            pages = pages.replace("\n","")
            pages = "/" + pages
            found = url + pages
            print (Fore.GREEN+"\t [#] Checking Site: [http://" + found + "]")
            connection = httplib.HTTPConnection(url)
            connection.request("GET",pages)
            response = connection.getresponse()
            if response.status == 200:
                print(Fore.RED+"[+] Admin Page Founded: " +  str(found))
                raw_input(Fore.GREEN+"[!] Press Enter To Continue.")
            elif response.status == 302:
                print "%s %s" % ("\n>>>" + found, "Possible admin page (302 - Redirect)")
            elif response.status == 404:
                print 'Error Code: 404',
            connection.close()
        print(Fore.GREEN+" [#] Scan Completed.")
        print(Fore.GREEN+"[#] Total Admin Pages: " + pg1)
        raw_input(Fore.YELLOW+"[#] Press Enter to Exit.")
        exit(0)
Welcome()
check_for_update()
try:
    while 1:
        ask = raw_input(Fore.GREEN+
"""
Hi Plase Choose An Option:
-----------------------------
> 1 >> Admin Page Finder
> 2 >> Admin Page Cracker
> 3 >> Exit
------------------------------
> """)
        if ask == '1':
            os.popen('clear').read()
            while 1:
                ask2 = raw_input(
"""
OK, Now Enter Site Source Code.
---------------------------------
> 1 >> PHP
> 2 >> ASP
> 3 >> CFM
> 4 >> JS
> 5 >> CGI
> 6 >> BRF
---------------------------------
> """)
                if ask2 == '1':
                     url = raw_input(Fore.GREEN+"[+] Enter Site Target\n>>> ")
                     IsUrl('php',url)
                elif ask2 == '2':
                     url = raw_input(Fore.GREEN+"[+] Enter Site Target\n>>> ")
                     IsUrl('asp',url)
                elif ask2 == '3':
                     url = raw_input(Fore.GREEN+"[+] Enter Site Target\n>>> ")
                     IsUrl('cfm',url)
                elif ask2 == '4':
                     url = raw_input(Fore.GREEN+"[+] Enter Site Target\n>>> ")
                     IsUrl('js',url)
                elif ask2 == '5':
                     url = raw_input(Fore.GREEN+"[+] Enter Site Target\n>>> ")
                     IsUrl('cgi',url)
                elif ask == '6':
                     url = raw_input(Fore.GREEN+"[+] Enter Site Target\n>>> ")
                     IsUrl('brf',url)
        elif ask == '2':
            url = raw_input(Fore.GREEN+"[+] Enter Site Target\n>>> ")
            word = raw_input(Fore.GREEN+"[+] Enter Password List Directory\n>>> ")
            FindPassword(word, url)
        elif ask == '3':
            print "\nBye ;)\n"
            exit(0)
except (KeyboardInterrupt, SystemExit):
    print "\nBye ;)\n"
    exit(0)
