#!/usr/bin/python
import hashlib
import sys
import re
import urllib2
from Crypto.PublicKey import RSA
#location = "./var/www/publickeys/"
location = "http://127.0.0.1/publickeys/"
message = ""
while True:
    try:
        message += raw_input()
        message +='\n'
    except EOFError:
        break
m = hashlib.md5()
rx = re.compile(r'\n\n(.*)\n\n--MAC--\n([0-9]*)',re.S)
m1 = rx.findall(message)
if not len(m1) > 0:
	sys.exit()
strings =  m1[0][0]
print strings
m.update(strings)
premac =  m.hexdigest()

rx = re.compile(r'from\s*:\s*.*?([\w.]+[@][\w.]+)',re.I)
m2 = rx.search(message)
if m2 == None:
	sys.exit()
else :
	stri = m2.group(1)
uname = stri
uname +=".pub"
location += uname
uname = location
l = long(m1[0][1])
m = (l,)
try:
	response = urllib2.urlopen(uname)
	html = response.read()
except urllib2.HTTPError, e:
	print message
	sys.exit()
if True:
 	key = RSA.importKey(html)
	message = message[0:message.find("\n\n--MAC--")]
	if key.verify(premac,m):
		message +='\n\n--Verified by IIITM--\n'
	else:
		message +='\n\n--Not Verified--\n'
	print message

else:
	print "Key Not Available"
