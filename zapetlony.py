# -*- coding: utf-8 -*-
import re
import sys
from pars import *
from orzeczim import *
plik = sys.argv[1]
stacyja = sys.argv[2]	#nazwa stacji
pracy = sys.argv[6]	#tryb pracy
debugu = sys.argv[7]	#tryb debugu
unix = sys.argv[3]	#unixtime
dzien = sys.argv[4]	#dzien lokalny
czas = sys.argv[5]	#czas lokalny
#sf = 			#save file
#sm = 			#save mode

file = open(plik, 'r')
#save = open(sf, 'a')

par = pars(file.read(), stacyja)
rowery = par.rowerry()
stacjinazwa = stacyja
orze = orzeczim(rowery, stacjinazwa, unix, dzien, czas)
if pracy == 'u':
	orze.orz()
	orze.pisul()
elif pracy == 'l':
	orze.orz()                                                  
	orze.pisul()
elif pracy == 'p':
	orze.pisp()
elif pracy == 'c':
	orze.pisc()
elif pracy == 'm':
	orze.pism()
elif pracy == 'a':
	orze.orz()
	orze.pisa()
elif pracy == 't':
	orze.pist()
else:
	print "Elektu labormodo a, l, u, p, c aux m se vi volas ke tiun programon funkcas."
        print "Plej eble ke la labormodo ", pracy, " estas malbona."

#tu bedzie jeszcze append do csvka
#EDIT: lub innej, sensowniejszej bazy danych

#tie estos ankaux append al la csv-o
#aux al alian, pli sencan datumbazon

file.close()
