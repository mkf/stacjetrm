#!/usr/bin/python
# -*- coding: utf-8 -*-
defprac="full";defdebugu="n";defwritemode="n";defwaitbetweenloops="singlecheck";deflang="esperanto"
defget = "k";defadrlangczy = "l"

# Do README: Tryby pobierania jednoczesnego umożliwiają szybsze, acz jednoczesne i bardziej podatne na bana pobieranie, zaś pobieranie kolejno daje czas każdego z pomiarów oraz mniejsze ryzyko bana
# później trza będzie zrobić też opcję pobierania 'jak kolejno, acz jednoczesnie', która będzie pobierała jednocześnie acz wyświelała w interfejsie kolejno, przy czym każde pobranie będzie miało swój waitbetweenloopsstamp
# mimo wielowątkowości, oczywistym jest, że część wątków wykona swoje zadanie szybciej od innych. W związku z tym ich wyni powinien iść dalej od razu, i nie czekać na resztę
# to trzeba będzie przepisać do Github Issues i potytułować po jednym
# mniej istotną jest możliwość odpalenia trybu kolejno w stylu jak jednocześnie
# później zrobi się konwerter danych zebranych kolejno do danych zebranych jednocześnie
# również jest jeszcze kwestia zapisu do wielu celów, do wielu plików/baz danych jednocześnie, przy dwóch różnych trybach
# możliwe musi być jednoczesne zapisywanie zupełnie odmiennymi we wszystkim trybami do wielu różnych plików i baz danych jednocześnie
# przepisać powyższe do GitHub Issues

#import argparse

# from ownlib.paramdemonwszystkich import *
# argu = sys.argv
# prmdw = paramdemonwszystkich(argu)
# lng = paramdemonwszystkich.lng()
allsta=list(range(1,27));defsta=allsta
from ownlib.argparsingtrmstacli import argparsowanie
parmetry=argparsowanie()

#—————————————INSTAWRITE,,INSTADISP———————————————————————————
instawrite = 1 if parmetry.instantly or parmetry.instawrite else 0
instadisp = 1 if parmetry.instantly or parmetry.instadisp else 0

#—————————————————————WRITE MODES——————————————————————————————————
writetryby = {
	"tocsvkolsinglefile": {'kolraz':'k','vol':'s','wtype':'csv','args':['filename']},
	"tocsvrazsinglefile": {'kolraz':'r','vol':'s','wtype':'csv','args':['filename']},
	'tocsvkolvolumesbytime':{'kolraz':'k','vol':'t','wtype':'csv','args':['filename','timebetwvol']},
	'tocsvrazvolumesbytime':{'kolraz':'r','vol':'t','wtype':'csv','args':['filename','timebetwvol']},
	'tocsvkolvolumesbycount':{'kolraz':'k','vol':'c','wtype':'csv','args':['filename','timebetwvol']},
	'tocsvrazvolumesbycount':{'kolraz':'r','vol':'c','wtype':'csv','args':['filename','timebetwvol']},
	'no':{'kolraz':'n','wtype':None,'args':None},
}
foundwrite=False
listevejled=[]
writekolczyraz=None
for pr_probwrite_str in writetryby.keys():
	evaledprobwrite=eval('parmetry.write{0}'.format(pr_probwrite_str))
	if pr_probwrite_str=='no' and evaledprobwrite: break
	if evaledprobwrite is not None and evaledprobwrite is not False:
		foundwrite=True
		trybofwrite=writetryby[pr_probwrite_str]
		if writekolczyraz!='k':
			if trybofwrite['kolraz']=='k': writekolczyraz='k'
			elif writekolczyraz!='r' and trybofwrite['kolraz']=='r': writekolczyraz='r'
		for evejled in evaledprobwrite: listevejled.append((trybofwrite,evejled))
if not foundwrite: listevejled.append((writetryby['no'],None));writekolczyraz='n'

print listevejled #debug

#——————————————————————CHARACTER SAFETY——————————————————
if parmetry.charsafe: lanchar = 'n'
elif parmetry.charwithnational: lanchar = 'y'
else: lanchar = "a"

#——————————————————————-LANGUAGES-——————————————————————
langs = {
	'english': {'shortname':'en','natiothing':False,'lanchar_a':'n'},
	'esperanto': {'shortname':'eo','natiothing':True,'lanchar_a':'n'},
	'polski': {'shortname':'pl','natiothing':True,'lanchar_a':'y'},
	'deutsch': {'shortname':'de','natiothing':True,'lanchar_a':'y'}
}
langorder=['english','esperanto','polski','deutsch']
islang=False
exec 'import importlib'
natiolamb = lambda lanchar: 'natio' if lanchar=='y' else 'safe' if lanchar=='n' else None
langen = lambda lingvo,langs,lanchar: eval("importlib.import_module('ownlib.lang."+lingvo+"')."+langs[lingvo]['shortname']+"_"+natiolamb(lanchar)+"()")
for lingvo in langorder:
	if eval('parmetry.lang'+str(lingvo)): islang=True ; lanchar=lanchar if not lanchar=='a' else langs[lingvo]['lanchar_a']; lan = langen(lingvo,langs,lanchar) ; lang = langs[lingvo]['shortname'] ; break
if not islang: lanchar=lanchar if not lanchar=='a' else langs[deflang]['lanchar_a'] ; lan=langen(deflang,langs,lanchar) ; lang = langs[deflang]['shortname']
#—— E N D : —————————— LANGUAGES ———————————————————————————————


#———————————————————————————SINGLE CHECK OR WAITING BETWEEN LOOPS —————————————————————————————————
if parmetry.singlecheck: waitbetweenloops = "singlecheck"
else: waitbetweenloops = parmetry.waitbetweenloops if type(parmetry.waitbetweenloops) == int else \
	defwaitbetweenloops if parmetry.defwaitbetweenloops else defwaitbetweenloops  #bzdurna nibyformalność

#———————————————————————————STATIONS CHOSEN————————————————————————
if parmetry.defstations: sta = defsta
elif parmetry.allstations: sta = allsta
else:
	try: sta = parmetry.station if len(parmetry.station)>0 else defsta
	except: sta = defsta

#————————————————————PRACY————————————————————————
pracedicto = {
	'full':      {'pracy':'f', 'kolczyraz':'k','needadrlangczy':True},
	'long':      {'pracy':'l', 'kolczyraz':'k'},
	'razem':     {'pracy':'r', 'kolczyraz':'r'},
	'razkomp':   {'pracy':'rk','kolczyraz':'r'},
	'user':      {'pracy':'u', 'kolczyraz':'k'},
	'adres':     {'pracy':'a', 'kolczyraz':'k','needadrlangczy':True},
	'tabela':    {'pracy':'t', 'kolczyraz':'k','needadrlangczy':True},
	'komp':      {'pracy':'k', 'kolczyraz':'k'},
	'compressed':{'pracy':'c', 'kolczyraz':'k'},
	'minim':     {'pracy':'m', 'kolczyraz':'k'},
	'none':      {'pracy':'n', 'kolczyraz':'n'},
	'def':       {'pracy':None}
}
foundpraca=False
for probprace in pracedicto.keys():
	if eval('parmetry.pracy'+probprace):probprac=probprace;foundpraca=True;break
if not foundpraca or probprac=='def':probprac=defprac
pracprob=pracedicto[probprac]
pracy=pracprob['pracy']
kolczyraz=pracprob['kolczyraz']
if 'adrlangczy' in pracprob: adrlangczy='l' if parmetry['adrlanglocal'] else 'c' if parmetry['adrlangchosen'] else defadrlangczy

#———————————————JĘZYK ADRESÓW —————————————————————
try: jezadr = adrlangczy
except: jezadr = "l"

#—————————————————— DEBUGU ———————————————
if parmetry.debugfull: debugu = "f"
elif parmetry.debugyes: debugu = "y"
elif parmetry.debugno: debugu = "n"
elif parmetry.debugdef: debugu = defdebugu
else: debugu = defdebugu

#——————————————DB———————————————————
if parmetry.withdb: czydb = True
elif parmetry.withoutdb: czydb = False

plikdb = 'trmdata.db'
try: plikdb = parmetry.dbfile

# import datewaitbetweenloops
# import waitbetweenloops

#———————————————– TRYB POBIERANIA : KOLEJNO CZY JEDNOCZEŚNIE — DZIAŁ SMARTGET —————————————————————_
if kolczyraz == 'k': smartget = 'k'
elif kolczyraz == 'r':
	if writekolczyraz == 'k': smartget = 'k'
	elif writekolczyraz == 'j' or writekolczyraz == 'n': smartget = 'j'
elif kolczyraz == 'n':
	if writekolczyraz == 'k' or writekolczyraz == 'r': smartget = writekolczyraz
	else: smartget = defget
# ^— to jest jeszcze niezupełnie gotowe. Zamiast tego powinno być jeszcze
# (sub)if-owanie na temat odpowiednika kolczyrazu, tyle że do spraw nie wyświetlania, a zapisu
# sęk w tym, że będzie to miało sens dopiero, gdy powstanie zapis
else:
	print 'kolczyraz nie jest ani k, ani r, ani n, więc czym jest?! Przecież ten program nie może, ot tak, niczego nie robić!'
	try: raise ValueError('Otóż jest on stringiem "%s"' % str(kolczyraz))
	except TypeError:raise TypeError('Otóź nie jest on nawet stringiem. Jego wartość to: %s'%str(kolczyraz))


#———————————————– TRYB POBIERANIA : KOLEJNO CZY JEDNOCZEŚNIE — DZIAŁ OSTATECZNEGO PARAMETRU —————————————————————_
if parmetry.getjednoczesnie: pob = "j"
elif parmetry.getkolejno: pob = "k"
else:
	try:
		if int(parmetry.getkolejnowait) >= 0:
			if int(parmetry.getkolejnowait) == 0: pob = "k"
			elif int(parmetry.getkolejnowait) > 0: pob = "w" ; pobw = int(parmetry.getkolejnowait)
			else: raise AssertionError
		elif parmetry.getdef: pob = defget
	except: pob = smartget

#——————————————————— RUN! —————————————————————————————————————
if pob == 'k':  # kolejno
	from ownlib.getkol import *
	if waitbetweenloops == "singlecheck": getkol(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite, czydb = czydb, plikdb = plikdb)
	elif type(waitbetweenloops) == int:
		from time import sleep
		while True: getkol(sta,pracy,debugu,lan,jezadr,lanchar,instadisp,instawrite, czydb=czydb, plikdb=plikdb) ; sleep(waitbetweenloops)
elif pob == 'j':  # jednocześnie
	from ownlib.getjednoczesnie import *
	if waitbetweenloops == "singlecheck": getjednoczesnie(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite,czydb=czydb,plikdb=plikdb)
	elif type(waitbetweenloops) == int:
		from time import sleep
		while True: getjednoczesnie(sta,pracy,debugu,lan,jezadr,lanchar,instadisp,instawrite,czydb=czydb, plikdb=plikdb) ; sleep(waitbetweenloops)
elif pob == 'w':  # kolejno-wait (getkolwait)
	pass
