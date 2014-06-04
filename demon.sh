#!/bin/bash
#cd /*/stacjetrm
#cd /*/*/stacjetrm
#cd /*/*/*/stacjetrm
#cd /*/*/*/*/stacjetrm
#cd /*/*/*/*/*/stacjetrm
#cd /*/*/*/*/*/*/stacjetrm
defpracy="a"
defdebugu="n"
defsm="n"
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
elif [ "$1" = "a" ]
then
        pracy=a
elif [ -z "$1" ]
then
	pracy=defpracy
elif [ "$1" = "d" ]
then
	pracy=defpracy
else
	echo 'Malkorekta parametron de la labormodon: ' $1 >&2
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
	debugu=defdebugu
elif [ "$2" = "d" ]
then
	debugu=defdebugu
else
	echo 'Malkorekta parametron de la senfusximodo: ' $2 >&2
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
if [ "$3" = "c" ]
then
        sm=c
elif [ "$3" = "n" ]
then
        sm=n
elif [ "$3" = "s" ]
then
        sm=s
elif [ -z "$3" ]
then
	sm=defsm
else
	echo 'Malkorekta parametron de la skribamodo: ' $3 >&2
fi
if [ "$sm" = "c" ]
then
	sd=csv
	echo "La ebleco de la skribadon al la dosieron ne ekzistas ankoraux."
elif [ "$sm" = "n" ]
then
	sd=none
elif [ "$sm" = "s" ]
then
	sd=sql
	echo "La ebleco de la skribadon al la SQL-datumbazo ne ekzistas ankoraux."
fi
#if [ "$4"
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
		echo "La ${i}a lancxo de la lopon"
		rm -v 0*TOR.js*
	else
		rm 0*TOR.js*
	fi
	if [ "$pracy" = "l" ]
	then
		echo "–—===================—–"
	elif [ "$pracy" = "a" ]
	then
		echo "–—===================—–"
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
				wget --no-check-certificate trm24.pl/panel-trm/0${j}TOR.jsp && echo "La staton de la biciklastacio 0${j}TOR elsxutita sukcese"
			else
				wget -q --no-check certificate trm24.pl/panel-trm/0${j}TOR.jsp && echo "La staton de la biciklastacio 0${j}TOR elsxutita sukcese"
			fi
		else
			wget -q --no-check-certificate trm24.pl/panel-trm/0${j}TOR.jsp
		fi
		python zapetlony.py 0${j}TOR.jsp 0${j}TOR $dzien $localdate $localtime $pracy $debugu $sd $sf
	done
	if [ "$debug" = "true" ]
	then
		echo "La ${i}a lancxo de la lopon finis"
	fi
done
echo "Zakonczenie programu przez dziwny traf"
exit
