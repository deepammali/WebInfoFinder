import socket
import os
import requests
import platform


# def back():
#     print()
#     back = input('\033[92mDo you want to continue? [Yes/No]: ')
#     if back[0].upper() == 'Y':
#         print()
#         iseeverything(newTarget, victim)
#     elif back[0].upper() == 'N':
#         print('\033[92mTHANK YOU!')   
#         exit
#     else:
#         print('\033[92m?')
#         exit


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

    print("""\033[96m

        01) IP Finder                                
        02) Port Scanner                             
        03) WayBack urls                             
        04) Subdomain Listing (use Sublistr)         
        05) Get robots.txt                          
        06) Host Info Scanner (use WhatWeb)         
        07) DNS Lookup                               
        08) Hosts Search                            
        09) Geo Location
        10) Host Information
        11) List Shared DNS Servers
        12) Dorking


        13) Set New Target
        14) EXIT


        """)

    print()


def iseeverything(newTarget, victim):
    try:
        if newTarget:
            what = input(
            '\033[92mAre you want to collect information of website or IP address? [website/IP]: ')
            
            if what[0].upper() == 'W':
                victim = input('Enter the website address: ')

            elif what[0].upper() == 'I':
                victim = input('Enter the IP address (or domain to get IP address of this domain): ')
                victim = socket.gethostbyname(victim)
                
            else:
                print('?')
                iseeverything(newTarget, victim)

            newTarget = False
            
            banner()

        choose = input('What would you like to do? (1-20): ')

        if choose == '1':
            ipAddr = socket.gethostbyname(victim)
            print()
            print(ipAddr)
            banner()
            iseeverything(newTarget, victim)

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

            banner()
            iseeverything(newTarget, victim)

        elif choose == '3':
            statusCode = "0"

            option = input("""
            1) Status Code 200
            2) Status Code 302
            3) Status Code 403
            4) Status Code 404
            5) ALL Urls
            
            INPUT: """)

            if (option == "1"):
                statusCode = "200"
            elif (option == "2"):
                statusCode = "302"
            elif (option == "3"):
                statusCode = "403"
            elif (option == "4"):
                statusCode = "404"
            elif (option != "5"):
                print("\n\033[91mNot Valid. Kindly fill the between 1-5 ONLY!")
                banner()
                iseeverything(newTarget, victim)

            if (statusCode != "0"):
                pagelink = "http://web.archive.org/cdx/search/cdx?url=*." + victim + \
                    "/*&output=text&fl=original&collapse=urlkey&filter=statuscode:" + statusCode
            else:
                pagelink = "http://web.archive.org/cdx/search/cdx?url=*." + \
                    victim + "/*&output=text&fl=original&collapse=urlkey"

            info = requests.get(pagelink)
            print('\033[91m', info.text)
            banner()
            iseeverything(newTarget, victim)

        elif choose == '4':
            clear()
            os.system('cd modules/Sublist3r && python3 sublist3r.py -d ' + victim)
            banner()
            iseeverything(newTarget, victim)

        elif choose == '5':
            robots = 'http://' + victim + '/robots.txt'
            info = requests.get(robots)
            print('\033[91m', info.text)
            banner()
            iseeverything(newTarget, victim)

        elif choose == '6':
            clear()
            os.system('whatweb -v '+victim)
            banner()
            iseeverything(newTarget, victim)

        elif choose == '7':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q='+victim
            info = requests.get(dnslook)
            print('\033[91m', info.text)
            banner()
            iseeverything(newTarget, victim)

        elif choose == '8':
            host = 'https://api.hackertarget.com/hostsearch/?q='+victim
            info = requests.get(host)
            print('\033[91m', info.text)
            banner()
            iseeverything(newTarget, victim)

        elif choose == '9':
            ipgeo = 'https://api.hackertarget.com/geoip/?q='+victim
            info = requests.get(ipgeo)
            print('\033[91m', info.text)
            info.close()
            banner()
            iseeverything(newTarget, victim)

        elif choose == '10':  # Host Information
            iplt = 'https://ipinfo.io/'+socket.gethostbyname(victim)+'/json'
            info = requests.get(iplt)
            print('\033[91m', info.text)
            info.close()
            banner()
            iseeverything(newTarget, victim)

        elif choose == '11':
            shared = 'https://api.hackertarget.com/findshareddns/?q='+victim
            info = requests.get(shared)
            print('\033[91m', info.text)
            banner()
            iseeverything(newTarget, victim)

        elif choose == '12':
            keywords = input("Enter Keywords: ")
            os.system('cd modules/Dorker && python3 dorker.py search ' +
                      keywords + " >> output.txt")
            run = open('modules/Dorker/output.txt', 'r')
            file = run.read()
            for i in file.split(sep="\n"):
                print('site:*.' + victim + " " + i)
            run.close()
            os.system('rm modules/Dorker/output.txt')
            banner()
            iseeverything(newTarget, victim)

        elif choose == '13':
            clear()
            newTarget = True
            iseeverything(newTarget, victim)

        elif choose == '14':
            exit

        elif choose == '010':
            os.system('cd modules/dosattack && python3 dosattack.py -g ' + victim)
            # option = input('option: ')
            banner()
            iseeverything(newTarget, victim)

        else:
            print('?')
            iseeverything(newTarget, victim)

    except socket.gaierror:
        print('Name or service not known!\033[93m')
        print()
        iseeverything(newTarget, victim)
    except UnboundLocalError:
        print('The information you entered is incorrect')
        print()
        iseeverything(newTarget, victim)
    except requests.exceptions.ConnectionError:
        print('Your Internet Offline')
        exit
    except IndexError:
        print('?')
        print()
        iseeverything(newTarget, victim)


newTarget = True
victim = ''
bill()
iseeverything(newTarget, victim)

        # elif choose == '10':
        #     header = 'https://api.hackertarget.com/httpheaders/?q='+victim
        #     info = requests.get(header)
        #     print('\033[91m', info.text)
        #     back()

        # elif choose == '7':
        #     pagelink = 'https://api.hackertarget.com/pagelinks/?q='+victim
        #     info = requests.get(pagelink)
        #     print('\033[91m', info.text)
        #     back()

        # elif choose == '8':
        #     clear()
        #     os.system('cd modules/Breacher && python3 breacher.py -u '+victim)
        #     back()
        # elif choose == '13':
        #     os.system('cd websource && mkdir '+victim)
        #     os.system('cd websource && cd '+victim+' && httrack '+victim)
        #     print("The website source code was saved in folder 'websource'")
        #     back()
        # Todo Work on later
        # elif choose == '25':
        #     clear()
        #     os.system('cd modules/Infoga && python3 infoga.py --domain '+victim)
        #     back()

        # elif choose == '28':
        #     clear()
        #     os.system('ruby ./modules/HatCloud/hatcloud.rb -b '+victim)
        #     back()