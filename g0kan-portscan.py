#!/usr/bin/python

import socket
import sys
from colorama import Fore
import os

os.system(['clear', 'cls'][os.name == 'nt'])
ip = sys.argv[1]

green = Fore.GREEN
red = Fore.RED
cyan = Fore.CYAN
white = Fore.WHITE
magenta = Fore.MAGENTA 

print(magenta + """
   _____                                 
 / ____|                                
 | (___   ___ __ _ _ __  _ __   ___ _ __ 
  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
  ____) | (_| (_| | | | | | | |  __/ |   
 |_____/ \___\__,_|_| |_|_| |_|\___|_|
""")

for porta in range(1,65535):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if s.connect_ex((ip,porta)) == 0:
        print(cyan + "[*]" , white + "Porta:" , porta , " aberta!")
        s.close()
