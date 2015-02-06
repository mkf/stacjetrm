#!/usr/bin/python
# -*- coding: utf-8 -*-
allsta=[1,2,3,4,5,6,7,8,9,10,11,12,13];defsta=allsta
defprac="full";defdebugu="n";defwritemode="n";defwaitbetweenloops="singlecheck";deflang="esperanto"
defget = "k";defadrlangczy = "l";defwvt = 24;defwvc = 1000
from ownlib.argparsingtrmstacli import argparsowanie
parmetry=argparsowanie(defwvt,defwvc)

#—————————————INSTAWRITE,,INSTADISP———————————————————————————
instawrite = 1 if parmetry.instantly or parmetry.instawrite else 0
instadisp = 1 if parmetry.instantly or parmetry.instadisp else 0

#—————————————————————WRITE MODES——————————————————————————————————
from ownlib.writekolczyraz import writekolczyraz as writerkolczyraza; writekolczyraz = writerkolczyraza(parmetry).writekolczyraz
#if parmetry.writetocsvkolsinglefile or parmetry.writetocsvrazsinglefile: multivol = 'j'
#elif parmetry.writetocsvrazmultiwaitbetweenloopsvolumefile or parmetry.writetocsvkolmultiwaitbetweenloopsvolumefile: multivol = 't'
#elif parmetry.writetocsvrazmulticountvolumefile or parmetry.writetocsvkolmulticountvolumefile: multivol = 'c'
#else: multivol = 'n'
tybyzapisu = []
for tybzapisu in (parmetry.writetocsvkolsinglefile, parmetry.writetocsvrazsinglefile,
				  parmetry.writetocsvrazvolumesbytime,
				  parmetry.writetocsvkolvolumesbytime, parmetry.writetocsvrazvolumesbycount,
				  parmetry.writetocsvkolvolumesbycount):
	try:
		if len(tybzapisu) > 0:
			for jtybzapisu in tybzapisu: tybyzapisu.append(jtybzapisu)
	except: pass

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
if 'adrlangczy' in pracprob: adrlangczy=pracprob['adrlangczy']


#———————————————JĘZYK ADRESÓW —————————————————————
try: jezadr = adrlangczy
except: jezadr = "l"

#—————————————————— DEBUGU ———————————————
if parmetry.debugfull: debugu = "f"
elif parmetry.debugyes: debugu = "y"
elif parmetry.debugno: debugu = "n"
elif parmetry.debugdef: debugu = defdebugu
else: debugu = defdebugu

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
	if waitbetweenloops == "singlecheck": getkol(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite)
	elif type(waitbetweenloops) == int:
		from time import sleep
		while True: getkol(sta,pracy,debugu,lan,jezadr,lanchar,instadisp,instawrite) ; sleep(waitbetweenloops)
elif pob == 'j':  # jednocześnie
	from ownlib.getjednoczesnie import *
	if waitbetweenloops == "singlecheck": getjednoczesnie(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite)
	elif type(waitbetweenloops) == int:
		from time import sleep
		while True: getjednoczesnie(sta,pracy,debugu,lan,jezadr,lanchar,instadisp,instawrite) ; sleep(waitbetweenloops)
elif pob == 'w':  # kolejno-wait (getkolwait)
	pass
