#!/usr/bin/python
import hashlib
import sys
import os.path
import re
from Crypto.PublicKey import RSA
location = "./root/privatekeys/"
message = ""
while True:
    try:
        message += raw_input()
        message +='\n'
    except EOFError:
        break
m = hashlib.md5()
rx = re.compile(r'\n\n(.*)',re.S)
m1 = rx.findall(message)
if not len(m1) > 0:
	sys.exit()
strings =  m1[len(m1)-1]
m.update(strings)
premac =  m.hexdigest()

rx = re.compile(r'from\s*:\s*.*?([\w.]+[@][\w.]+)',re.I)
m2 = rx.search(message)
if m2 == None:
	sys.exit()
else :
	stri = m2.group(1)
uname = stri
uname +=".pem"
location += uname
uname = location
if os.path.isfile(uname):
	f = open(uname,'r')
 	key = RSA.importKey(f.read())
	mac = key.sign(premac,'')
	message +='\n\n--MAC--\n'
	message +=str(mac[0])
	print message
	f.close()

else:
	print "Hash not found"
