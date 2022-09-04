# -*- coding: utf-8 -*-
"""port scanner.ipynb

Automatically generated by Colaboratory.   

Internal Port Scanner for Queens medical center ASMIS network - set of code with #comments.
This scanner points at scanme.nmap.org for testing purposes only due to permissions granted by scanme.nmap.org. The actual host (IP Address) MUST be changed to the desired (Permissioned) host prior to usage of this scanner outside of this project assignment.
see the README.md file for support.
"""

import sys 
import socket 
from datetime import datetime 
from unittest import result 

if len(sys.argv) != 2: 
    print("Invalid amount of arguments due to scanning internally")
    print("Syntax: Testing Internal ASMIS Port Scanner")

else:   
    target = socket.gethostbyname('45.33.32.156', sys.argv[1]) 

print("-" * 30) 
print("-" * 70) 
print("-" * 100) 
print("Scanning scanme.nmap.org for testing reasons due to permissions. ") 
print("-" * 70) 
print("Time started " + str(datetime.now())) 
print("-" * 100) 
print("-" * 70) 
print("-" * 30) 

t1 = datetime.now() 

try: 
    for port in range(1,100): 
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
                socket.setdefaulttimeout(0.2) 
                result = s.connect_ex(('45.33.32.156', port)) 
                if result ==0: 
                        print("Port {} is OPEN! Check if this needs changing".format(port)) 

except KeyboardInterrupt: 
        print("\n Exiting program.")
        sys.exit() 

except socket.gaierror: 
        print("Hostname could not be resolved, scan will now exit.") 
        sys.exit()

except socket.error: 
        print("Could not connect to the specified IP address")
        sys.exit() 

t2 = datetime.now()
total = t2 - t1
print("-" * 70) 
print ("Time to complete =  ", total)
