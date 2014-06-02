#!/bin/bash
#cd /*/stacjetrm
#cd /*/*/stacjetrm
#cd /*/*/*/stacjetrm
#cd /*/*/*/*/stacjetrm
#cd /*/*/*/*/*/stacjetrm
#cd /*/*/*/*/*/*/stacjetrm
defpracy="u"
if [ "$1" = "u" ]
then
	pracy=u
elif [ "$1" = "l" ]
then
	pracy=l
elif [ "$1" = "p" ]
then
        pracy=p
elif [ "$1" = "c" ]
then
        pracy=c
elif [ "$1" = "m" ]
then
        pracy=m
elif [ -z "$1" ]
then
	pracy=defpracy
else
	echo 'Niepoprawny parametr trybu pracy: ' $1 >&2
	cat README*
	exit
fi
if [ "$2" = "f" ]
then
	debugu=f
elif [ "$2" = "y" ]
then
	debugu=y
elif [ "$2" = "n" ]
then
	debugu=n
elif [ -z "$2" ]
then
	debugu=n
else
	echo 'Niepoprawny parametr trybu debugu: ' $2 >&2
        cat README*
        exit
fi
if [ "$debugu" = "y" ]
then
	debug=true
elif [ "$debugu" = "f" ]
then
	debug=true
	fdebug=true
else
	debug=false
	fulldebug=false
fi
unixtime=$(date "+%s")
localdate=$(TZ='Europe/Warsaw' date "+%F")
localtime=$(TZ='Europe/Warsaw' date "+%T")
costam=345
i=0
while :
do
	i=$[i + 1]
	if [ "$debug" = "true" ]
	then
		echo "Zatoczenie petli nr $i"
		rm -v 0*TOR.js*
	else
		rm 0*TOR.js*
	fi
	for j in 01 02 03 04 05 06 07 08 09 10 11 12
	do
		unixtime=$(date "+%s")
		localdate=$(TZ='Europe/Warsaw' date "+%F")
		localtime=$(TZ='Europe/Warsaw' date "+%T")
		dzien=$unixtime
		if [ "$debug" = "true" ]
		then
			if [ "$fdebug" = "true" ]
			then
				wget --no-check-certificate trm24.pl/panel-trm/0${j}TOR.jsp && echo "Pobieranie stacji 0${j}TOR sukcesem zakonczone"
			else
				wget -q --no-check certificate trm24.pl/panel-trm/0${j}TOR.jsp && echo "Pobieranie stacji 0${j}TOR sukcesem zakonczone"
			fi
		else
			wget -q --no-check-certificate trm24.pl/panel-trm/0${j}TOR.jsp
		fi
		python zapetlony.py 0${j}TOR.jsp 0${j}TOR $dzien $localdate $localtime $pracy $debugu
	done
	if [ "$debug" = "true" ]
	then
		echo "Zatoczenie $i completed"
	fi
done
echo "Zakonczenie programu przez dziwny traf"
exit
