import random
import pyfiglet
import sys
import time
from colorama import Fore
from time import sleep
def combo(s):
	for ASU in s + '\n':
		sys.stdout.write(ASU)
		sys.stdout.flush()
		sleep(1. / 150)
n = '\x1b[1;31m'
j = '\x1b[1;36m'
o = '\x1b[1;32m'
Z=n+'================================'
combo(Z)
X=o+'Welcome To Combo Maker Script V1'
combo(X)
Z=n+'================================'
combo(Z)
C=o+'Script Code By:- VODKA_HUNTER\nTELEGRAM CH:- @toso011\nGIT-HUB:- ?'
combo(C)
Z=n+'================================'
combo(Z)
Z = '\x1b[2;32m'
P55 = pyfiglet.figlet_format('COMBO ')
import requests
ss = '1'
rs ='1'
if '1' ==  rs:
    combo(Z + P55)
Z = '\x1b[2;31m'
P55 = pyfiglet.figlet_format(' MAKER')
import requests
ss = '1'
rs ='1'
if '1' ==  rs:
    print(Z + P55)
city = input(Fore.GREEN+ 'Enter 077 or 078 or 010 or 011 or 075 : ') #like 077 or 05 or .... don't' put +964 or +966 or something like that
use = '0123456789'
many = input(Fore.YELLOW +'\nHow Many Number: ')
many = int(many)
	
letter = input(Fore.BLUE + 'Contains How Many Naumber:-') 
letter = int(letter)
print(j+'')
	
for num in range(many):
	num = ''
	for item in range(letter):
		num = ''
	for item in range(letter):
		num += random.choice(use)
	print ('	'+city+num+':'+city+num)
	with open('Number_List.txt', 'a') as x:
		x.write(city+num+':'+city+num+'\n')