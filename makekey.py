#!/usr/bin/python
from Crypto.PublicKey import RSA
import sys
location1 = "./root/privatekeys/"
location2 = "./var/www/publickeys/"
key = RSA.generate(2048)
uname = sys.argv[1]
location1 +=uname
uname1 = location1+'.pem'
f = open(uname1,'w')
f.write(key.exportKey('PEM'))
f.close()

location2 +=uname
uname2 = location2 +'.pub'
f = open(uname2,'w')
f.write(key.publickey().exportKey('PEM'))
f.close()

