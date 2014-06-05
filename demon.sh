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
deft=60
if [ "$1" = "d" ]
then
	t = deft
elif [ -n "$1" ]
then
	if [ "$1" -ge 0 ]
	then
		t=$1
	else
		echo "Malbonan atendotempon: " $1 >&2
	        exit
	fi
else
	echo "Malbonan atendotempon: " $1 >&2
	exit
fi
if [ "$2" = "u" ]
then
	pracy=u
elif [ "$2" = "l" ]
then
	pracy=l
elif [ "$2" = "p" ]
then
        pracy=p
elif [ "$2" = "c" ]
then
        pracy=c
elif [ "$2" = "m" ]
then
        pracy=m
elif [ "$2" = "a" ]
then
        pracy=a
elif [ "$2" = "t" ]
then
        pracy=t
elif [ -z "$2" ]
then
	pracy=defpracy
elif [ "$2" = "d" ]
then
	pracy=defpracy
else
	echo 'Malkorekta parametron de la labormodon: ' $2 >&2
	cat README*
	exit
fi
if [ "$3" = "f" ]
then
	debugu=f
elif [ "$3" = "y" ]
then
	debugu=y
elif [ "$3" = "n" ]
then
	debugu=n
elif [ -z "$3" ]
then
	debugu=defdebugu
elif [ "$3" = "d" ]
then
	debugu=defdebugu
else
	echo 'Malkorekta parametron de la senfusximodo: ' $3 >&2
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
if [ "$4" = "c" ]
then
        sm=c
elif [ "$4" = "n" ]
then
        sm=n
elif [ "$4" = "s" ]
then
        sm=s
elif [ -z "$4" ]
then
	sm=defsm
else
	echo 'Malkorekta parametron de la skribamodo: ' $4 >&2
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
#if [ "$5"
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
	elif [ "$pracy" = "t" ]
	then
		for u in $( seq 1 86 )
		do
			printf "_"
		done
		echo ""
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
		echo "Kaj nun ni atendas" $t "sekundojn"
		sleep $t
	fi
	if [ "$debug" = "true" ]
	then
		echo "La ${i}a lancxo de la lopon finis"
	fi
done
echo "Zakonczenie programu przez dziwny traf"
exit
