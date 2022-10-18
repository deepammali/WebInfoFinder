import socket
import os
import requests
import platform

def back():
    print()
    back = input('\033[92mDo you want to continue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        iseeverything()
    elif back[0].upper() == 'N':
        print('\033[92mRemember https://GitHackTools.blogspot.com')
        exit
    else:
        print('\033[92m?')
        exit

def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def bill():
    clear()
    print("""\033[98m

         _  _  _       _        _         ___         _______ _           _             
        | || || |     | |      | |       / __)       (_______|_)         | |            
        | || || |_____| |__    | |____ _| |__ ___     _____   _ ____   __| |_____  ____ 
        | || || | ___ |  _ \   | |  _ (_   __) _ \   |  ___) | |  _ \ / _  | ___ |/ ___)
        | || || | ____| |_) )  | | | | || | | |_| |  | |     | | | | ( (_| | ____| |    
         \_____/|_____)____/   |_|_| |_||_|  \___/   |_|     |_|_| |_|\____|_____)_|    
                                                                                
                                                                                                                           
    """)

def banner():
#     print("""\033[96m
#  1) DNS Lookup                 13) Host DNS Finder
#  2) Whois Lookup               14) Reserve IP Lookup
#  3) GeoIP Lookup               15) Email Gathering (use Infoga)
#  4) Subnet Lookup              16) Subdomain listing (use Sublist3r)
#  5) Port Scanner               17) Find Admin login site (use Breacher)
#  6) Page Links                 18) Check and Bypass CloudFlare (use HatCloud)
#  7) Zone Transfer              19) Website Copier (use httrack)
#  8) HTTP Header                20) Host Info Scanner (use WhatWeb)
#  9) Host Finder                21) About BillCipher
#  10) IP-Locator                22) Fuck Out Of Here (Exit)
#  11) Find Shared DNS Servers
#  12) Get Robots.txt""")

    print("""\033[96m
        1) IP Scanner                               9) DNS Lookup
        2) Port Scanner                             10) Page Links
        3) WayBack urls                             11) Geo IP
        4) Subdomain Listing (use Sublistr)         12) Subnet Lookup
        5) Get Robots.txt                           13) http Headers
        6) Host Info Scanner (use WhatWeb)          14) Website Copier (use httrack)
        7) Host Finder                              15) IP Locator
        8) Find Shared DNS Servers                  0) EXIT
        """)

    print()

def iseeverything():
    try:
        what = input('\033[92mAre you want to collect information of website or IP address? [website/IP]: ')
        if what[0].upper() == 'W':
            victim = input('Enter the website address: ')
            banner()
        elif what[0].upper() == 'I':
            victim = input('Enter the IP address (or domain to get IP address of this domain): ')
            victim = socket.gethostbyname(victim)
            print('The IP address of target is:',victim)
            banner()
        else:
            print('?')
            iseeverything()

        choose = input('What information would you like to collect? (1-20): ')

        if choose == '7':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+victim
            info = requests.get(dnslook)
            print('\033[91m',info.text)
            back()

        elif choose == '4':
            clear()
            os.system('cd modules/Sublist3r && python3 sublist3r.py -d '+victim)
            back()
            
        elif choose == '9':
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+victim
            info = requests.get(ipgeo)
            print('\033[91m',info.text)
            back()

        elif choose == '10':
            subnet = 'http://api.hackertarget.com/subnetcalc/?q='+victim
            info = requests.get(subnet)
            print('\033[91m',info.text)
            back()

        elif choose == '1':
            clear()
            os.system("nmap " + victim)
            back()

        elif choose == '2':
            clear()
            print("""
            1) Enter port number
            2) All ports (may take long time)
            """)

            portInput = input("Select: ")

            if portInput == '1':
                pn = input("PORT NUMBER: ")
                os.system("nmap -p" + pn + " " + victim)

            if portInput == '2':
                os.system("nmap -p- " + victim)

            back()

        elif choose == '8':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q='+victim
            info = requests.get(pagelink)
            print('\033[91m',info.text)
            back()

        elif choose == '11':
            header = 'https://api.hackertarget.com/httpheaders/?q='+victim
            info = requests.get(header)
            print('\033[91m',info.text)
            back()

        elif choose == '7':
            host = 'https://api.hackertarget.com/hostsearch/?q='+victim
            info = requests.get(host)
            print('\033[91m',info.text)
            back()

        elif choose == '14':
            iplt = 'https://ipinfo.io/'+victim+'/json'
            info = requests.get(iplt)
            print('\033[91m',info.text)
            back()

        elif choose == '15':
            shared = 'https://api.hackertarget.com/findshareddns/?q='+victim
            info = requests.get(shared)
            print('\033[91m',info.text)
            back()

        elif choose == '5':
            robots ='http://'+victim+'/robots.txt'
            info = requests.get(robots)
            print('\033[91m',info.text)
            back()


        ## Todo Work on later
        # elif choose == '25':
        #     clear()
        #     os.system('cd modules/Infoga && python3 infoga.py --domain '+victim)
        #     back()


        # elif choose == '27':
        #     clear()
        #     os.system('cd modules/Breacher && python breacher.py -u '+victim)
        #     back()

        # elif choose == '28':
        #     clear()
        #     os.system('ruby ./modules/HatCloud/hatcloud.rb -b '+victim)
        #     back()

        elif choose == '13':
            os.system('cd websource && mkdir '+victim)
            os.system('cd websource && cd '+victim+' && httrack '+victim)
            print("The website source code was saved in folder 'websource'")
            back()

        elif choose == '6':
            clear()
            os.system('whatweb -v '+victim)
            back()

        elif choose == '0':
            exit

        else:
            print('?')
            iseeverything()
            
    except socket.gaierror:
        print('Name or service not known!\033[93m')
        print()
        iseeverything()
    except UnboundLocalError:
        print('The information you entered is incorrect')
        print()
        iseeverything()
    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
        print('?')
        print()
        iseeverything()

bill()
iseeverything()
