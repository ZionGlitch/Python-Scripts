#!/bin/python3

import sys
import socket
from datetime import datetime

#Define our target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else: 
	print("Invalid amount of argumnets.")
	print("Syntax: python3 scanner.py <ip>")

#Banner
print("-" * 50)
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" *50)

try:
	for port in range(1,1200):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port)) #resturns an error indicator
			if result == 0:
				print("Port {} is open".format(port))
			s.close()

except KeyboardInterrupt:
	print("\n Exiting Program.")
	sys.exit()

except socket.gaierror:
	print("Hostname cannot be resolved.")
	sys.exit()

except socket.error:
	print("Couldn't connect to server.")
	sys.exit()