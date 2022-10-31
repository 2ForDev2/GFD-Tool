import os
os.system("mode 130,30")
os.system("pip install -r requirements.txt")
from colorama import *
import json
import socket
import colorama
import sys
import requests
import json
import urllib.request, urllib.error, urllib.parse, urllib
import time
init()
sys.tracebacklimit = 0

banner = (f"""{Fore.RED}
   █████████  ███████████ ██████████  
  ███░░░░░███░░███░░░░░░█░░███░░░░███ 
 ███     ░░░  ░███   █ ░  ░███   ░░███{Fore.RESET}
{Fore.CYAN}░███          ░███████    ░███    ░███
░███    █████ ░███░░░█    ░███    ░███
░░███  ░░███  ░███  ░     ░███    ███ 
 ░░█████████  █████       ██████████  
  ░░░░░░░░░  ░░░░░       ░░░░░░░░░░ {Fore.RESET}
{Fore.GREEN}A Normal Griefing Tool Maded By For.Dev {Fore.RESET}""")

options = (f"""
{Fore.RED}1.IP Scanner{Fore.RESET}
{Fore.RED}2.IP Resolver{Fore.RESET}
{Fore.RED}3.Server Lookup{Fore.RESET}
{Fore.RED}4.Griefing Commands{Fore.RESET}
{Fore.RED}5.About The Tool{Fore.RESET}
{Fore.RED}6.Exit{Fore.RESET}

""")
def main():
    os.system("cls")
    os.system("clear")
    print(banner)
    print(options)
    print(Fore.MAGENTA + "Enter The Option:", end='')
    option = input()
    if option == "1":
            try:
                scan = input(f"Enter The IP To Scan: ")
                os.system(f"nmap -p- -n -Pn --unprivileged -vvv --min-rate 5000 -oN GFD-Scan.txt {scan}")
                input("Press Enter to continue...")
                main()
            except KeyboardInterrupt:
                print("Stopping GFD...")
                time.sleep(2)
                exit()
    elif option == "2":
        print(Fore.MAGENTA + "Enter The Domain:", end='')
        Domain = input()
        try:
            print(f"{Fore.RED}IP Address - " + socket.gethostbyname(Domain) + Fore.RESET)
            input("Press Enter to continue...")
            main()
        except:
            print(f"{Fore.RED}Invalid Domain{Fore.RESET}")
            input("Press Enter to continue...")
            main()
    elif option == "3":
            os.system("cls")
            print(Fore.MAGENTA + "Enter The Domain:", end='')
            server = input()
            url2 = "https://api.mcsrvstat.us/2/"
            response2 = urllib.request.urlopen(url2 + server)
            data = response2.read()
            mcinfo = json.loads(data)
            try:
                print(Fore.CYAN+"IP")
                print(mcinfo['ip'])
                print(Fore.CYAN+"Hostname")
                print(mcinfo['hostname'])
                print(Fore.CYAN+"Port")
                print(mcinfo['port'])
                print(Fore.CYAN+"Version")
                print(mcinfo['version'])
            except: KeyError
            pass
            input("Press Enter to continue...")
            main()
    elif option == "4":
        os.system(f'cls')
        print(banner)
        print(f"""
        {Fore.GREEN}Comandos Destructivos
        //brush sphere 0 5
        /fill ~-5 ~-5 ~-5 ~5 ~5 ~5 lava{Fore.RESET}
        {Fore.YELLOW}Comandos De Teletransportacion
        /minecraft:tp @a @p
        /minecraft:execute 0 0 0 @p minecraft:tp @a @p{Fore.RESET}
        {Fore.LIGHTMAGENTA_EX}Comandos De broadcast
        /pt bc &eServer Griefed By For.Dev www.youtube.com/channel/UC8CVlG_TxDl-ZstM53mxNoA
        /alert &eServer Griefed By For.Dev www.youtube.com/channel/UC8CVlG_TxDl-ZstM53mxNoA
        /ept bc &eServer Griefed By For.Dev www.youtube.com/channel/UC8CVlG_TxDl-ZstM53mxNoA{Fore.RESET}
        {Fore.LIGHTRED_EX}Comandos De Op
        /lp user ForDev permission set *
        /minecraft:op ForDev{Fore.RESET}""")
        input("Press Enter to continue...")
        main()
    elif option == "5":
        print(f"{Fore.YELLOW}GFD Was Made To Make Easier Griefing{Fore.RESET}")
        input("Press Enter to continue...")
        main()
    elif option == "6":
        exit()
    else:
        print("Incorrect Option")
        input("Press Enter to continue...")
        main()
main()
