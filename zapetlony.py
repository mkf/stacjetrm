import re
import sys
plik = sys.argv[1]
stacyja = sys.argv[2]
trybpracy = sys.argv[6]
unix = sys.argv[3]
dzien = sys.argv[4]
czas = sys.argv[5]
slowniczekkoncowek = {'001TOR.jsp': 'jski', '002TOR.jsp': 'rzyny', '003TOR.jsp': 'packiego', '004TOR.jsp': 'torna', '005TOR.jsp': 'ejskie', '006TOR.jsp': 'sytecka', '007TOR.jsp': 'esco', '008TOR.jsp': 'arket', '009TOR.jsp': 'arket', '010TOR.jsp': 'wny', '011TOR.jsp': 'olicji', '012TOR.jsp': 'aciej'}
# ^ to tutaj to slowniczek koncowek, dzieki ktoremu bedzie mozna wyodrebnic sama liczbe rowerow, ktora jest jedyna liczba pomiedzy owa koncowka a "szt.".
# i tak nie uzylem slowniczka, ale przynajmniej przypomnialem sobie dictionaries w pythonie
szt = '.*szt'

file = open(plik, 'r')


odnaleziono = re.search(r'w na stacji.*szt', file.read(), re.S)

wynalezione = odnaleziono.group()
odnalezione = str(wynalezione)
stacjowystring = re.sub(r'\D',"",stacyja)
stacja = int(stacjowystring)
#comaszukac = slowniczekkoncowek[plik] + szt
comaszukac = 'th.*szt'
renaleziono = re.search(comaszukac, odnalezione, re.S)
renalezione = renaleziono.group()
#reodnalezione = renalezione.group
reodnalezione = re.sub(r'built-in method group of ',"",renalezione)
#wlasciwie, to ten powyzszy re.sub jest zbedny, ale nic nie robi jesli tego built[...] nie ma, wiec niech juz bedzie ;;;; i finally:
rowerki = re.sub(r'\D',"",reodnalezione)
rowery = int(rowerki)
stacjinazwa = re.sub(r'.jsp',"",plik)
if rowery == 0:
	orzim = "estas neniu bicikloj"
elif rowery == -1:
	orzim = "okazis iun eraron, cxar gxi transdonas ke tie estas -1 biciklo - kaj tio estas negativa kvanto"
elif rowery <= 0:
	orzim = "okazis iun eraron, cxar gxi transdonas ke tie estas " + str(rowery) + " bicikloj - kaj tio estas negativa kvanto"
elif rowery == 1:
	orzim = "estas 1  biciklo"
elif rowery >= 2:
	if rowery <= 9:
		orzim = ("estas " + str(rowery) + "  bicikloj")
	if rowery >= 10:
		orzim = ("estas " + str(rowery) + " bicikloj")
else:
	orzim = ", ni ne scias kiom bicikloj estas tie, cxar dum la akiroprovon de la biciklokvanto okazis la eraro"
#La "if" super estos uzota pri la interfaco por homojn: modo 'f' kaj 'u'
if trybpracy == "u":
	print dzien, czas, "Al la biciklastacio", stacjinazwa, orzim
elif trybpracy == "f":
        print dzien, czas, "Al la biciklastacio", stacjinazwa, orzim
elif trybpracy == "p":
	print dzien, czas, stacjinazwa, rowery
elif trybpracy == "c":
	print unix, stacja, rowery
elif trybpracy == "m":
	print unix, stacjinazwa, rowery
else:
	print "Elektu labormodo u, f, p, c aux m se vi volas ke tiun programon funkcas."
#if param1 == "p":
#	print "
#print "Czas: ", unix, " --  na stacji ", stacjinazwa, " jest ", rowery, " rowerow"
#print 'Na stacji ', stacyja, ' jest ', szt, ' rowerow miejskich.'


#tu bedzie jeszcze ladny append do jednego csvka
#EDIT: lub innej, sensowniejszej bazy danych
