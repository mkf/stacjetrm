#!/bin/bash
#cd /*/stacjetrm
#cd /*/*/stacjetrm
#cd /*/*/*/stacjetrm
#cd /*/*/*/*/stacjetrm
#cd /*/*/*/*/*/stacjetrm
#cd /*/*/*/*/*/*/stacjetrm
defparam1="u"
if [ "$1" = "u" ]
then
	param1=u
elif [ "$1" = "f" ]
then
	param1=f
elif [ "$1" = "p" ]
then
        param1=p
elif [ "$1" = "c" ]
then
        param1=c
elif [ "$1" = "m" ]
then
        param1=m
elif [ -z "$1" ]
then
	param1=defparam1
else
	echo 'Niepoprawny parametr: ' $1 >&2
	cat README*
	exit
fi

unixtime=$(date "+%s")
localdate=$(TZ='Europe/Warsaw' date "+%F")
localtime=$(TZ='Europe/Warsaw' date "+%T")
costam=345
i=0
while :
do
	i=$[i + 1]
	if [ "$param1" = "f" ]
	then
		echo "Zatoczenie petli nr $i"
		rm -v 0*TOR.js*
	else
		rm 0*TOR.js*
	fi
	for j in 01 02 03 04 05 06 07 08 09 10 11 12
	do
		unixtime=$(date "+%s")
		dzien=$unixtime
		wget -q --no-check-certificate trm24.pl/panel-trm/0${j}TOR.jsp && echo "Pobieranie stacji 0${j}TOR sukcesem zakonczone"
		python zapetlony.py 0${j}TOR.jsp 0${j}TOR $dzien $localdate $localtime $param1
	done
	echo "Zatoczenie $i completed"
done
echo "Zakonczenie programu przez dziwny traf"
exit
