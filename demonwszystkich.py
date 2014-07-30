# -*- coding: utf-8 -*-
import sys
# Do README: Tryby pobierania jednoczesnego umożliwiają szybsze, acz jednoczesne i bardziej podatne na bana pobieranie, zaś pobieranie kolejno daje czas każdego z pomiarów oraz mniejsze ryzyko bana
#później trza będzie zrobić też opcję pobierania 'jak kolejno, acz jednoczesnie', która będzie pobierała jednocześnie acz wyświelała w interfejsie kolejno, przy czym każde pobranie będzie miało swój timestamp
#mimo wielowątkowości, oczywistym jest, że część wątków wykona swoje zadanie szybciej od innych. W związku z tym ich wyni powinien iść dalej od razu, i nie czekać na resztę
#to trzeba będzie przepisać do Github Issues i potytułować po jednym
#mniej istotną jest możliwość odpalenia trybu kolejno w stylu jak jednocześnie
#później zrobi się konwerter danych zebranych kolejno do danych zebranych jednocześnie
#również jest jeszcze kwestia zapisu do wielu celów, do wielu plików/baz danych jednocześnie, przy dwóch różnych trybach
#możliwe musi być jednoczesne zapisywanie zupełnie odmiennymi we wszystkim trybami do wielu różnych plików i baz danych jednocześnie
#przepisać powyższe do GitHub Issues
import re
import argparse
from generatornazwyplikuzdata import *
#from paramdemonwszystkich import *
#argu = sys.argv
#prmdw = paramdemonwszystkich(argu)
#lng = paramdemonwszystkich.lng()
allsta = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
defsta = allsta
defpracy = "f"
defdebugu = "n"
defwritemode = "n"
deftime = 60
deflang = "e"
defget = "k"
defadrlangczy = "l"
argh = argparse.ArgumentParser()
arglang = argh.add_mutually_exclusive_group()
argtime = argh.add_mutually_exclusive_group()
argstac = argh.add_mutually_exclusive_group()
argpracy = argh.add_mutually_exclusive_group()
argdebugu = argh.add_mutually_exclusive_group()
argzapisu = argh.add_mutually_exclusive_group()
arggetu = argh.add_mutually_exclusive_group()
#argh.add_argument("-l", "--lang", type=str, help="Jednoznakowy kod języka: \nOne-character language code: \nUnulitera lingvkodo: \n - a - English \n - e - Esperanto \n - p - Polski \n - d - Deutsch \n ")
arglang.add_argument("-la", "--langenglish", action="store_true", help="LANG: English")
arglang.add_argument("-le", "--langesperanto", action="store_true", help="LANG: Esperanto")
arglang.add_argument("-lp", "--langpolski", action="store_true", help="LANG: Polski")
arglang.add_argument("-ld", "--langdeutsch", action="store_true", help="LANG: Deutsch")
argtime.add_argument("-t", "--time", type=int, help="Opóźnienie między zbieraniem danych/Atendtempo/Delay between instances")
argtime.add_argument("-td", "--deftime", action="store_true", help="-t z domyślną wartością/-t with default value")
argtime.add_argument("-ts", "--singlecheck", action="store_true", help="Jednorazowe sprawdzenie/Check once")
argstac.add_argument("-sa", "--allstations", action="store_true", help="Wszystkie stacje/Ĉiuj biciklstacjoj/All stations")
argstac.add_argument("-sd", "--defstations", action="store_true", help="Domyślne stacje/[def] biciklstacjoj/Default stations")
argstac.add_argument("-s", "--station", type=int, action="append", help="Wybierz stację, można użyć wielokrotnie")
#argpracy.add_argument("-pf", "--pracyfull", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i adresami")
argpracy.add_argument("-pfc", "--pracyfulladrlangchosen", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i w wybranym języku adresami")
argpracy.add_argument("-pfl", "--pracyfulladrlanglocal", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i w lokalnym(polskim) języku adresami")
argpracy.add_argument("-pr", "--pracyrazem", action="store_true", help="Interfejs pełny tabelowy, wszystkie stacje w jednej linii")
argpracy.add_argument("-pl", "--pracylong", action="store_true", help="Interfejs pełny z przedzieleniem na pętli")
argpracy.add_argument("-pu", "--pracyuser", action="store_true", help="Interfejs pełny ciągły")
#argpracy.add_argument("-pa", "--pracyadres", action="store_true", help="Interfejs pełny z adresami")
argpracy.add_argument("-pac", "--pracyadresadrlangchosen", action="store_true", help="Interfejs pełny z w wybranym języku adresami")
argpracy.add_argument("-pal", "--pracyadresadrlanglocal", action="store_true", help="Interfejs pełny z w lokalnym(polskim) języku adresami")
#argpracy.add_argument("-pt", "--pracytabela", action="store_true", help="Interfejs tabeli z adresami")
argpracy.add_argument("-ptc", "--pracytabelaadrlangchosen", action="store_true", help="Interfejs tabeli z w wybranym języku adresami")
argpracy.add_argument("-ptl", "--pracytabelaadrlanglocal", action="store_true", help="Interfejs tabeli z w lokalnym(polskim) języku adresami")
argpracy.add_argument("-pk", "--pracykomp", action="store_true", help="Interfejs programowy")
argpracy.add_argument("-pc", "--pracycompressed", action="store_true", help="Interfejs programowy czasUNIX,jedno- lub dwu cyfrowy numer stacji, liczba rowerów")
argpracy.add_argument("-pm", "--pracyminim", action="store_true", help="Interfejs programowy minimalistyczny")
argpracy.add_argument("-prk", "--pracyrazkomp", action="store_true", help="Interfejs programowy, wszystkie stacje naraz")
argpracy.add_argument("-pn", "--pracynone", action="store_true", help="Interfejs bez danych na stdout")
argpracy.add_argument("-pd", "--pracydef", action="store_true", help="Opcja domyślna trybu pracy")
argdebugu.add_argument("-bf", "--debugfull", action="store_true")
argdebugu.add_argument("-by", "--debugyes", action="store_true")
argdebugu.add_argument("-bn", "--debugno", action="store_true")
argdebugu.add_argument("-bd", "--debugdef", action="store_true")
argzapisu.add_argument("-wck", "--writetocsvkol", type=str, help="Zapis do csv (stacje kolejno, po jednej na linię), wpisz nazwę pliku")
argzapisu.add_argument("-wcr", "--writetocsvraz", type=str, help="Zapis do csv (wszystkie stacje naraz, w jednej linii), wpisz nazwę pliku")
argzapisu.add_argument("-wn", "--writenone", action="store_true", help="Nie zapisuj")
arggetu.add_argument("-gj", "--getjednoczesnie", action="store_true", help="Pobieraj jednocześnie")
arggetu.add_argument("-gk", "--getkolejno", action="store_true", help="Pobieraj kolejno bez odstępu czasowego")
arggetu.add_argument("-gkw", "--getkolejnowait", type=int, help="Pobieraj kolejno z odstępem czasowym")
arggetu.add_argument("-gd", "--getdef", action="store_true", help="Pobieraj w trybie domyślnym")
parmetry = argh.parse_args()
if parmetry.langenglish:
	lang = "en"
	from english import *
	lan = english()
elif parmetry.langesperanto:
	lang = "eo"
	from esperanto import *
	lan = esperanto()
elif parmetry.langpolski:
	lang = "pl"
	from polski import *
	lan = polski()
elif parmetry.langdeutsch:
	lang = "de"
	from deutsch import *
	lan = deutsch()
else:
	lang = "eo"
	from esperanto import *
	lan = esperanto()
if parmetry.singlecheck:
	time = "singlecheck"
else:
	if type(parmetry.time) == "int":
		time = parmetry.time
	elif parmetry.deftime:
		time = deftime
	else:
		time = deftime
if parmetry.defstations:
	sta = defsta
elif parmetry.allstations:
	sta = allsta
#	print "defpar"
#	print sta
#elif len(parmetry.station) > 0:
#	sta = parmetry.station
#	print sta
else:
	try:
		if len(parmetry.station) > 0:
			sta = parmetry.station
		else:
			sta = defsta
	except:
		sta = defsta
#print argpracy

#	print "def"
#	print sta
#print type(parmetry.station)
#print parmetry.station
if parmetry.pracyfulladrlangchosen:
	pracy = "f"
	adrlangczy = "c"
	kolczyraz = "k"
elif parmetry.pracyfulladrlanglocal:
	pracy = "f"
	adrlangczy = "l"
	kolczyraz = "k"
elif parmetry.pracylong:
	pracy = "l"
	kolczyraz = "k"
elif parmetry.pracyrazem:
	pracy = "r"
	kolczyraz = "r"
elif parmetry.pracyrazkomp:
	pracy = "rk"
	kolczyraz = "r"
elif parmetry.pracyuser:
	pracy = "u"
	kolczyraz = "k"
elif parmetry.pracyadresadrlangchosen:
	pracy = "a"
	kolczyraz = "k"
	adrlangczy = "c"
elif parmetry.pracyadresadrlanglocal:
	pracy = "a"
	kolczyraz = "k"
	adrlangczy = "l"
elif parmetry.pracytabelaadrlangchosen:
	pracy = "t"
	kolczyraz = "k"
	adrlangczy = "c"
elif parmetry.pracytabelaadrlanglocal:
	pracy = "t"
	kolczyraz = "k"
	adrlangczy = "l"
elif parmetry.pracykomp:
	pracy = "k"
	kolczyraz = "k"
elif parmetry.pracycompressed:
	pracy = "c"
	kolczyraz = "k"
elif parmetry.pracyminim:
	pracy = "m"
	kolczyraz = "k"
elif parmetry.pracynone:
	pracy = "n"
	kolczyraz = "k"
elif parmetry.pracydef:
	pracy = defpracy
	adrlangczy = defadrlangczy
	if pracy == "f" or pracy == "l" or pracy == "u" or pracy == "a" or pracy == "t" or pracy == "k" or pracy == "c" or pracy == "m":
		kolczyraz = "k"
	elif pracy == "r" or pracy == "rk":
		kolczyraz = "r"
	elif pracy == "n":
		kolczyraz = "n"
	else:
		print "Źlee"
		quit()
else:
	pracy = defpracy
	adrlangczy = defadrlangczy
	if pracy == "f" or pracy == "l" or pracy == "u" or pracy == "a" or pracy == "t" or pracy == "k" or pracy == "c" or pracy == "m":
		kolczyraz = "k"
	elif pracy == "r" or pracy == "rk":
		kolczyraz = "r"
	elif pracy == "n":
		kolczyraz = "n"
	else:
		print "Źlee"
		quit()
if parmetry.debugfull:
	debugu = "f"
elif parmetry.debugyes:
	debugu = "y"
elif parmetry.debugno:
	debugu = "n"
elif parmetry.debugdef:
	debugu = defdebugu
else:
	debugu = defdebugu

import datetime
import time

if parmetry.getjednoczesnie:
	pob = "j"
elif parmetry.getkolejno:
	pob = "k"
else:
	try:
		if int(parmetry.getkolejnowait) >= 0:
			if int(parmetry.getkolejnowait) == 0:
				pob = "k"
			elif int(parmetry.getkolejnowait) > 0:
				pob = "w"
				pobw = int(parmetry.getkolejnowait)
			else:
				print "Źle"
				quit()
		elif parmetry.getdef:
			pob = defget
	except:
		pob = defget
	
if kolczyraz == "n":
	#if zapis kolejny czy jednoczesny
	jezelikolczyraz = 1
