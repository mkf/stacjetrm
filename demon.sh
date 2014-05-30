#!/bin/sh
costam=345
i=0
while :
do
	i=$[i + 1]
	echo "Zatoczenie petli nr $i"
	rm -v 0*TOR.js*
	for j in 01 02 03 04 05 06 07 08 09 10 11 12
	do
		wget -q --no-check-certificate trm24.pl/panel-trm/0${j}TOR.jsp && echo "Pobieranie stacji 0${j}TOR sukcesem zakonczone"
		python zapetlony.py 0${j}TOR.jsp 0${j}TOR
	done
	echo "Zatoczenie $i completed"
done
echo "Zakonczenie programu przez dziwny traf"
exit
