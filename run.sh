#!/bin/bash

if [ $# -lt 1 ]
then 
		echo "Usage : $0 Number"
fi

case "$1" in

	1) ./makekey.py a.mani.cms@gmail.com
	;;

	2)./sign.py < ./data/inmail > ./data/intermail
	;;

	3)./verify.py <./data/intermail > ./data/outmail
	;;

	4)./verifynet.py <./data/intermail > ./data/outmail
	;;

	5) rm ./root/privatekeys/*
	   rm ./var/www/publickeys/*
	   rm ./data/intermail ./data/outmail
	;;

	*) echo "Eg $0 1 -executes makekey"
	   echo "   $0 2 -executes sign"
	   echo "   $0 3 -executes verify"
	   echo "   $0 4 -executes verifynet"
	   echo "   $0 5 -deletes all data"
		;;
esac
