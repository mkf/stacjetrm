#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
# Do README: Tryby pobierania jednoczesnego umożliwiają szybsze, acz jednoczesne i bardziej podatne na bana pobieranie, zaś pobieranie kolejno daje czas każdego z pomiarów oraz mniejsze ryzyko bana
#później trza będzie zrobić też opcję pobierania 'jak kolejno, acz jednoczesnie', która będzie pobierała jednocześnie acz wyświelała w interfejsie kolejno, przy czym każde pobranie będzie miało swój waitbetweenloopsstamp
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
defwaitbetweenloops = "singlecheck"
deflang = "e"
defget = "k"
defadrlangczy = "l"
defadrchar = 'l'
defwvt = 24
defwvc = 1000
argh = argparse.ArgumentParser()
arglang = argh.add_mutually_exclusive_group()
argchar = argh.add_mutually_exclusive_group()
argwaitbetweenloops = argh.add_mutually_exclusive_group()
argstac = argh.add_mutually_exclusive_group()
argpracy = argh.add_mutually_exclusive_group()
argdebugu = argh.add_mutually_exclusive_group()
argzapisu = argh #.add_mutually_exclusive_group()
arggetu = argh.add_mutually_exclusive_group()
#argh.add_argument("-l", "--lang", type=str, help="Jednoznakowy kod języka: \nOne-character language code: \nUnulitera lingvkodo: \n - a - English \n - e - Esperanto \n - p - Polski \n - d - Deutsch \n ")
argchar.add_argument("-cs", "--charsafe", action="store_true", help='No "unsafe" national characters in language and adresses')
argchar.add_argument("-cn", "--charwithnational", action="store_true", help='Enable "unsafe" national characters in language and adresses')
arglang.add_argument("-la", "--langenglish", action="store_true", help="LANG: English")
arglang.add_argument("-le", "--langesperanto", action="store_true", help="LANG: Esperanto")
arglang.add_argument("-lp", "--langpolski", action="store_true", help="LANG: Polski")
arglang.add_argument("-ld", "--langdeutsch", action="store_true", help="LANG: Deutsch")
argwaitbetweenloops.add_argument("-t", "--waitbetweenloops", type=int, help="Opóźnienie między zbieraniem danych w sekundach/Atendtempo/Delay between instances")
argwaitbetweenloops.add_argument("-td", "--defwaitbetweenloops", action="store_true", help="-t z domyślną wartością/-t with default value")
argwaitbetweenloops.add_argument("-ts", "--singlecheck", action="store_true", help="Jednorazowe sprawdzenie/Check once")
argstac.add_argument("-sa", "--allstations", action="store_true", help="Wszystkie stacje/Ĉiuj biciklstacjoj/All stations")
argstac.add_argument("-sd", "--defstations", action="store_true", help="Domyślne stacje/[def] biciklstacjoj/Default stations")
argstac.add_argument("-s", "--station", type=int, action="append", choices=range(1,13), help="Wybierz stację, można użyć wielokrotnie")
#argpracy.add_argument("-pf", "--pracyfull", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i adresami")
argpracy.add_argument("-pfc", "--pracyfulladrlangchosen", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i w wybranym języku adresami")
argpracy.add_argument("-pfl", "--pracyfulladrlanglocal", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i w lokalnym(polskim) języku adresami w alfabecie polskim")
#argpracy.add_argument("-pfle", "--pracyfulladrlanglocalenglishalphabet", action="store_true", help="Interfejs pełny z przedzieleniem na pętli i w lokalnym(polskim) języku adresami w alfabecie angielskim")
argpracy.add_argument("-pr", "--pracyrazem", action="store_true", help="Interfejs pełny tabelowy, wszystkie stacje w jednej linii")
argpracy.add_argument("-pl", "--pracylong", action="store_true", help="Interfejs pełny z przedzieleniem na pętli")
argpracy.add_argument("-pu", "--pracyuser", action="store_true", help="Interfejs pełny ciągły")
#argpracy.add_argument("-pa", "--pracyadres", action="store_true", help="Interfejs pełny z adresami")
argpracy.add_argument("-pac", "--pracyadresadrlangchosen", action="store_true", help="Interfejs pełny z w wybranym języku adresami")
argpracy.add_argument("-pal", "--pracyadresadrlanglocal", action="store_true", help="Interfejs pełny z w lokalnym(polskim) języku adresami w alfabecie polskim")
#argpracy.add_argument("-pale", "--pracyadresadrlanglocalenglishalphabet", action="store_true", help="Interfejs pełny z w lokalnym(polskim) języku adresami w alfabecie angielskim")
#argpracy.add_argument("-pt", "--pracytabela", action="store_true", help="Interfejs tabeli z adresami")
argpracy.add_argument("-ptc", "--pracytabelaadrlangchosen", action="store_true", help="Interfejs tabeli z w wybranym języku adresami")
argpracy.add_argument("-ptl", "--pracytabelaadrlanglocal", action="store_true", help="Interfejs tabeli z w lokalnym(polskim) języku adresami w alfabecie polskim")
#argpracy.add_argument("-ptle", "--pracytabelaadrlanglocalenglishalphabet", action="store_true", help="Interfejs tabeli z w lokalnym(polskim) języku adresami w alfabecie angielskim")
argpracy.add_argument("-pk", "--pracykomp", action="store_true", help="Interfejs programowy")
argpracy.add_argument("-pc", "--pracycompressed", action="store_true", help="Interfejs programowy czasUNIX,jedno- lub dwu cyfrowy numer stacji, liczba rowerów")
argpracy.add_argument("-pm", "--pracyminim", action="store_true", help="Interfejs programowy minimalistyczny")
argpracy.add_argument("-prk", "--pracyrazkomp", action="store_true", help="Interfejs programowy, wszystkie stacje naraz")
argpracy.add_argument("-pn", "--pracynone", action="store_true", help="Interfejs bez danych na stdout")
argpracy.add_argument("-pd", "--pracydef", action="store_true", help="Opcja domyślna trybu pracy")
argdebugu.add_argument("-bf", "--debugfull", action="store_true", help="Debug pełny")
argdebugu.add_argument("-by", "--debugyes", action="store_true", help="Debug częściowy")
argdebugu.add_argument("-bn", "--debugno", action="store_true", help="Debug wyłączony")
argdebugu.add_argument("-bd", "--debugdef", action="store_true", help="Domyślne opcje debugu")
argzapisu.add_argument("-wcks", "--writetocsvkolsinglefile", type=str, action="append", help="Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), wpisz nazwę pliku, zapis do jednego pliku ciągły")
argzapisu.add_argument("-wcrs", "--writetocsvrazsinglefile", type=str, action="append", help="Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), wpisz nazwę pliku, zapis do jednego pliku ciągły")
argzapisu.add_argument("-wckvt", "--writetocsvkolmultiwaitbetweenloopsvolumefile", action="append", type=str, nargs=2, help=str("Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), wpisz początek nazwy pliku i liczbę godzin (ta druga domyślnie %s); zapis wielowolumenowy wg czasu" % defwvt))
argzapisu.add_argument("-wcrvt", "--writetocsvrazmultiwaitbetweenloopsvolumefile", action="append", type=str, nargs=2, help=str("Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), wpisz początek nazwy pliku i liczbę godzin (ta druga domyślnie %s); zapis wielowolumenowy wg czasu" % defwvt))
#argzapisu.add_argument("-wvt", "--writemultivolumewaitbetweenloopshours", type=int, action="store_true", help="Parametr opcjonalny zapisu wielowolumenowego: czas w godzinach na jeden plik"
argzapisu.add_argument("-wckvc", "--writetocsvkolmulticountvolumefile", type=str, action="append", nargs=2, help=str("Zapis do csv (stacje kolejno, po jednej na linię - czas zapisywany dla każdego odczytu z osobna), wpisz początek nazwy pliku i liczbę zapisów na wolumen (domyślnie %s); zapis wielowolumenowy wg ilości zapisów" % defwvc))
argzapisu.add_argument("-wcrvc", "--writetocsvrazmulticountvolumefile", type=str, action="append", nargs=2, help=str("Zapis do csv (wszystkie stacje naraz, w jednej linii - czas zapisywany jednorazowo dla całej serii odczytów), wpisz początek nazwy pliku i liczbę zapisów na wolumen (domyślnie %s); zapis wielowolumenowy wg ilości zapisów" % defwvc))
#argzapisu.add_argument("-wvc", "--writemultivolumeentrycount", type=int, action="store_true", help="Parametr opcjonalny zapisu wielowolumenowego: ilość wpisów na jeden plik"
argzapisu.add_argument("-wn", "--writeno", action="store_true", help="Nie zapisuj")
arggetu.add_argument("-gj", "--getjednoczesnie", action="store_true", help="Pobieraj jednocześnie")
arggetu.add_argument("-gk", "--getkolejno", action="store_true", help="Pobieraj kolejno bez odstępu czasowego")
arggetu.add_argument("-gkw", "--getkolejnowait", type=int, help="Pobieraj kolejno z odstępem czasowym pomiędzy odczytami pojedyńczych stacji")
arggetu.add_argument("-gd", "--getdef", action="store_true", help="Pobieraj w trybie domyślnym")
argh.add_argument("-in", "--instantly", action="store_true", help="Wyświetlaj oraz zapisuj natychmiast po pobraniu informacji, równoważne z -iw oraz -id")
argh.add_argument("-iw", "--instawrite", action="store_true", help="Zapisuj natycmiast po pobraniu informacji.")
argh.add_argument("-id", "--instadisp", action="store_true", help="Wyświetlaj natychmiast po pobraniu informacji")
argh.add_argument("-tor", "--tor", action="store_true", help="Pobieraj za pośrednictwem sieci Tor (wymaga stem)")
parmetry = argh.parse_args()
instawrite = 0
instadisp = 0
if parmetry.instantly:
	instawrite = 1
	instadisp = 1
if parmetry.instawrite:
	instawrite = 1
if parmetry.instadisp:
	instadisp = 1
if parmetry.tor:
	try:
		import stem.process
		tor = 1
	except:
		print "Importing stem library failed. Install it with 'sudo easy_install stem' or 'sudo pip install stem'. Exiting."
		quit()
else:
	tor = 0

try:
	if len(parmetry.writetocsvkolsinglefile+parmetry.writetocsvkolmultiwaitbetweenloopsvolumefile+parmetry.writetocsvkolmulticountvolumefile)>0:
		writekolczyraz = 'k'
	elif len(parmetry.writetocsvrazsinglefile+parmetry.writetocsvrazmultiwaitbetweenloopsvolumefile+parmetry.writetocsvrazmulticountvolumefile)>0:
		writekolczyraz = 'r'
	elif parmetry.writeno:
		writekolczyraz = 'n'
	else:
		writekolczyraz = 'n'
except:
	try:
		if len(parmetry.writetocsvrazsinglefile+parmetry.writetocsvrazmultiwaitbetweenloopsvolumefile+parmetry.writetocsvrazmulticountvolumefile)>0:
			writekolczyraz = 'r'
		elif parmetry.writeno:
			writekolczyraz = 'n'
		else:
			writekolczyraz = 'n'
	except:
		if parmetry.writeno:
			writekolczyraz = 'n'
		else:
			writekolczyraz = 'n'
#if parmetry.writetocsvkolsinglefile or parmetry.writetocsvrazsinglefile:
#	multivol = 'j'
#elif parmetry.writetocsvrazmultiwaitbetweenloopsvolumefile or parmetry.writetocsvkolmultiwaitbetweenloopsvolumefile:
#	multivol = 't'
#elif parmetry.writetocsvrazmulticountvolumefile or parmetry.writetocsvkolmulticountvolumefile:
#	multivol = 'c'
#else:
#	multivol = 'n'
tybyzapisu = []
for tybzapisu in (parmetry.writetocsvkolsinglefile, parmetry.writetocsvrazsinglefile, parmetry.writetocsvrazmultiwaitbetweenloopsvolumefile, parmetry.writetocsvkolmultiwaitbetweenloopsvolumefile, parmetry.writetocsvrazmulticountvolumefile, parmetry.writetocsvkolmulticountvolumefile):
	try:
		if len(tybzapisu)>0:
			tybyzapisu.append(tybzapisu)
	except:
		nicsieniedziejealecostrzawstawic = 1
if parmetry.charsafe:
	lanchar = 'n'
elif parmetry.charwithnational:
	lanchar = 'y'
else:
	lanchar = "a"
if parmetry.langenglish:
	lang = "en"
	if lanchar == 'a':
		lanchar = 'n'
	from english import *
	lan = english()
elif parmetry.langesperanto:
	lang = "eo"
	if lanchar == 'a':
		lanchar = 'y'
	if lanchar == 'y':
		from esperanto import eo_natio
		lan = eo_natio()
	if lanchar == 'n':
		from esperanto import eo_safe
		lan = eo_safe()
elif parmetry.langpolski:
	lang = "pl"
	if lanchar == 'a':
		lanchar = 'y'
	if lanchar == 'y':
		from polski import pl_natio
		lan = pl_natio()
	if lanchar == 'n':
		from polski import pl_safe
		lan = pl_safe()
elif parmetry.langdeutsch:
	lang = "de"
	if lanchar == 'a':
		lanchar = 'y'
	if lanchar == 'y':
		from deutsch import de_natio
		lan = de_natio()
	if lanchar == 'n':
		from deutsch import de_safe
		lan = de_safe()
else:
	lang = "eo"
	if lanchar == 'a':
		lanchar = 'n'
	if lanchar == 'y':
		from esperanto import eo_natio
		lan = eo_natio()
	if lanchar == 'n':
		from esperanto import eo_safe
		lan = eo_safe()

if parmetry.singlecheck:
	waitbetweenloops = "singlecheck"
else:
	if type(parmetry.waitbetweenloops) == "int":
		waitbetweenloops = parmetry.waitbetweenloops
	elif parmetry.defwaitbetweenloops:
		waitbetweenloops = defwaitbetweenloops
	else:
		waitbetweenloops = defwaitbetweenloops
if parmetry.defstations:
	sta = defsta
elif parmetry.allstations:
	sta = allsta
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
# 	adrchar = 'e'
# elif parmetry.pracyfulladrlanglocalpolishalphabet:
# 	pracy = "f"
# 	adrlangczy = "l"
# 	kolczyraz = "k"
# 	adrchar = 'l'
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
# 	adrchar = 'e'
# elif parmetry.pracyadresadrlanglocalpolishalphabet:
# 	pracy = "a"
# 	kolczyraz = "k"
# 	adrlangczy = "l"
# 	adrchar = 'l'
elif parmetry.pracytabelaadrlangchosen:
	pracy = "t"
	kolczyraz = "k"
	adrlangczy = "c"
elif parmetry.pracytabelaadrlanglocal:
	pracy = "t"
	kolczyraz = "k"
	adrlangczy = "l"
# 	adrchar = 'e'
# elif parmetry.pracytabelaadrlanglocalpolishalphabet:
# 	pracy = "t"
# 	kolczyraz = "k"
# 	adrlangczy = "l"
# 	adrchar = 'l'
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
	adrchar = defadrchar
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
	adrchar = defadrchar
	if pracy == "f" or pracy == "l" or pracy == "u" or pracy == "a" or pracy == "t" or pracy == "k" or pracy == "c" or pracy == "m":
		kolczyraz = "k"
	elif pracy == "r" or pracy == "rk":
		kolczyraz = "r"
	elif pracy == "n":
		kolczyraz = "n"
	else:
		print "Źlee"
		quit()
try:
	jezadr = adrlangczy
except:
	jezadr = "l"
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

#import datewaitbetweenloops
#import waitbetweenloops

if kolczyraz == 'k':
	smartget = 'k'
elif kolczyraz == 'r':
	if writekolczyraz == 'k':
		smartget = 'k'
	elif writekolczyraz == 'j' or writekolczyraz == 'n':
		smartget = 'j'
elif kolczyraz == 'n':
	if writekolczyraz == 'k' or writekolczyraz == 'r':
		smartget = writekolczyraz
	else:
		smartget = defget
#			   ^— to może budzić kontrowersje. Otóż zamiast tego powinno być jeszcze
#	(sub)if-owanie na temat odpowiednika kolczyrazu, tyle że do spraw nie wyświetlania, a zapisu
# sęk w tym, że będzie to miało sens dopiero, gdy powstanie zapis
else:
	print 'kolczyraz nie jest ani k, ani r, ani n, więc czym jest?! Przecież ten program nie może, ot tak, niczego nie robić!'
	try:
		print 'Otóż jest on stringiem "%s"' % str(kolczyraz)
	except:
		print 'Otóź nie jest on nawet stringiem. Jego wartość to:'
		print kolczyraz

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
		pob = smartget
		
if pob == 'k':
	from getkol import *
	if waitbetweenloops == "singlecheck":
		getkol(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite, tor)
	elif type(waitbetweenloops) == int:
		import time
		while True:
			getkol(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite, tor)
			time.sleep(waitbetweenloops)
elif pob == 'j':
	from getjednoczesnie import *
	if waitbetweenloops == "singlecheck":
		getjednoczesnie(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite, tor)
	elif type(waitbetweenloops) == int:
		import time
		while True:
			getjednoczesnie(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite, tor)
			time.sleep(waitbetweenloops)
	
elif pob == 'w':
	from getkolwait import *
	
