# -*- coding: utf-8 -*-
import sys
import re
import argparse
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
argh = argparse.ArgumentParser()
arglang = argh.add_mutually_exclusive_group()
argtime = argh.add_mutually_exclusive_group()
argstac = argh.add_mutually_exclusive_group()
argpracy = argh.add_mutually_exclusive_group()
argdebugu = argh.add_mutually_exclusive_group()
argzapisu = argh.add_mutually_exclusive_group()
#argh.add_argument("-l", "--lang", type=str, help="Jednoznakowy kod języka: \nOne-character language code: \nUnulitera lingvkodo: \n - a - English \n - e - Esperanto \n - p - Polski \n - d - Deutsch \n ")
arglang.add_argument("-la", "--langenglish", action="store_true", help="LANG: English")
arglang.add_argument("-le", "--langesperanto", action="store_true", help="LANG: Esperanto")
arglang.add_argument("-lp", "--langpolski", action="store_true", help="LANG: Polski")
arglang.add_argument("-ld", "--langdeutsch", action="store_true", help="LANG: Deutsch")
argtime.add_argument("-t", "--time", type=int, help="Opóźnienie między zbieraniem danych/Atendtempo/Delay between instances")
argtime.add_argument("-td", "--deftime", action="store_true", help="-t z domyślną wartością/-t with default value")
argstac.add_argument("-sa", "--allstations", action="store_true", help="Wszystkie stacje/Ĉiuj biciklstacjoj/All stations")
argstac.add_argument("-sd", "--defstations", action="store_true", help="Domyślne stacje/[def] biciklstacjoj/Default stations")
argstac.add_argument("-s", "--station", type=int, action="append", help="Wybierz stację, można użyć wielokrotnie")
argpracy.add_argument("-pf", "--pracyfull", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i adresami")
argpracy.add_argument("-pl", "--pracylong", action="store_true", help="Interfejs pełny z przedzieleniem na pętli")
argpracy.add_argument("-pu", "--pracyuser", action="store_true", help="Interfejs pełny ciągły")
argpracy.add_argument("-pa", "--pracyadres", action="store_true", help="Interfejs pełny z adresami")
argpracy.add_argument("-pt", "--pracytabela", action="store_true", help="Interfejs tabeli z adresami")
argpracy.add_argument("-pk", "--pracykomp", action="store_true", help="Interfejs programowy")
argpracy.add_argument("-pc", "--pracycompressed", action="store_true", help="Interfejs programowy czasUNIX,jedno- lub dwu cyfrowy numer stacji, liczba rowerów")
argpracy.add_argument("-pm", "--pracyminim", action="store_true", help="Interfejs programowy minimalistyczny")
argpracy.add_argument("-pn", "--pracynone", action="store_true", help="Interfejs bez danych na stdout")
argpracy.add_argument("-pd", "--pracydef", action="store_true", help="Opcja domyślna trybu pracy")
argdebugu.add_argument("-bf", "--debugfull", action="store_true")
argdebugu.add_argument("-by", "--debugyes", action="store_true")
argdebugu.add_argument("-bn", "--debugno", action="store_true")
argdebugu.add_argument("-bd", "--debugdef", action="store_true")
argzapisu.add_argument("-wc", "--writetocsv", type=str, help="Zapis do csv, wpisz nazwę pliku")
argzapisu.add_argument("-wn", "--writenone", action="store_true", help="Nie zapisuj")
parmetry = argh.parse_args()
if parmetry.langenglish:
	lang = "a"
	from english import *
	lan = english()
elif parmetry.langesperanto:
	lang = "e"
	from esperanto import *
	lan = esperanto()
elif parmetry.langpolski:
	lang = "p"
	from polski import *
	lan = polski()
elif parmetry.langdeutsch:
	lang = "d"
	from deutsch import *
	lan = deutsch()
else:
	lang = "e"
	from esperanto import *
	lan = esperanto()
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
elif len(parmetry.station) > 0:
	sta = parmetry.station
#	print sta
else:
	sta = defsta
#print argpracy

#	print "def"
#	print sta
#print type(parmetry.station)
#print parmetry.station
if parmetry.pracyfull:
	pracy = "f"
elif parmetry.pracylong:
	pracy = "l"
elif parmetry.pracyuser:
	pracy = "u"
elif parmetry.pracyadres:
	pracy = "a"
elif parmetry.pracytabela:
	pracy = "t"
elif parmetry.pracykomp:
	pracy = "k"
elif parmetry.pracycompressed:
	pracy = "c"
elif parmetry.pracyminim:
	pracy = "m"
elif parmetry.pracynone:
	pracy = "n"
elif parmetry.pracydef:
	pracy = defpracy
else:
	pracy = defpracy

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


