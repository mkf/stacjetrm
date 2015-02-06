#!/usr/bin/python
# -*- coding: utf-8 -*-
allsta=[1,2,3,4,5,6,7,8,9,10,11,12,13];defsta=allsta;defpracy="f";defdebugu="n";defwritemode="n";defwaitbetweenloops="singlecheck";deflang="e"
defget = "k";defadrlangczy = "l";defadrchar = 'l';defwvt = 24;defwvc = 1000
from ownlib.argparsingtrmstacli import argparsowanie
parmetry=argparsowanie(defwvt,defwvc)
#TODO: Wywalić pozostałość zwaną adrchar/defadrchar stąd, z argparsowania i zewsząd

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
				  parmetry.writetocsvrazmultiwaitbetweenloopsvolumefile,
				  parmetry.writetocsvkolmultiwaitbetweenloopsvolumefile, parmetry.writetocsvrazmulticountvolumefile,
				  parmetry.writetocsvkolmulticountvolumefile):
	try:
		if len(tybzapisu) > 0: tybyzapisu.append(tybzapisu)
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
deflang='esperanto'
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
	'fulladrlangchosen':  {'pracy':'f', 'kolczyraz':'k','adrlangczy':'c'},
	'fulladrlanglocal':   {'pracy':'f', 'kolczyraz':'k','adrlangczy':'l'},
	'long':               {'pracy':'l', 'kolczyraz':'k'},
	'razem':              {'pracy':'l', 'kolczyraz':'r'},
	'razkomp':            {'pracy':'rk','kolczyraz':'r'},
	'user':               {'pracy':'u', 'kolczyraz':'k'},
	'adresadrlangchosen': {'pracy':'a', 'kolczyraz':'k','adrlangczy':'c'},
	'adresadrlanglocal' : {'pracy':'a', 'kolczyraz':'k','adrlangczy':'l'},
	'tabelaadrlangchosen':{'pracy':'t', 'kolczyraz':'k','adrlangczy':'c'},
	'tabelaadrlanglocal' :{'pracy':'t', 'kolczyraz':'k','adrlangczy':'l'},
	'komp':               {'pracy':'k', 'kolczyraz':'k'},
	'compressed':         {'pracy':'c', 'kolczyraz':'k'},
	'minim':              {'pracy':'m', 'kolczyraz':'k'},
	'none':               {'pracy':'n', 'kolczyraz':'n'},
	'def':                {'pracy':None}
}
foundpraca=False
for probprac in pracedicto.keys():
	if eval('parmetry.pracy'+probprac):
		pracprob=pracedicto[probprac] if not probprac=='def' else None
		pracy=pracprob['pracy'] if not probprac=='def' else defpracy
		setkolczyrazowdefpracy = set([kcre['kolczyraz'] for kcre in pracedicto.values() if kcre['pracy']==pracy]) if probprac=='def' else None
		assert setkolczyrazowdefpracy is None or len(setkolczyrazowdefpracy)==1, 'setkolczyrazowdefpracy: %s'%str(setkolczyrazowdefpracy)
		kolczyraz=pracprob['kolczyraz'] if not probprac=='def' else (list(setkolczyrazowdefpracy)[0] if setkolczyrazowdefpracy is not None else None)
		if not probprac=='def':
			if 'adrlangczy' in pracprob: adrlangczy=pracprob['adrlangczy']
		else:
			setadrlangczow = set(['adrlangczy' in alce for alce in pracedicto.values() if alce['pracy']==pracy])
			assert len(setadrlangczow)==1,'setadrlangczow: %s'%str(setadrlangczow)
			if list(setadrlangczow)[0]: adrlangczy=defadrlangczy
		foundpraca=True
		break
if not foundpraca:
	pracy=defpracy
	setkolczyrazowdefpracy = set([kcre['kolczyraz'] for kcre in pracedicto.values() if kcre['pracy']==pracy])
	assert len(setkolczyrazowdefpracy)==1, 'setkolczyrazowdefpracy: %s'%str(setkolczyrazowdefpracy)
	kolczyraz=list(setkolczyrazowdefpracy)[0] if setkolczyrazowdefpracy is not None else None
	setadrlangczow = set(['adrlangczy' in alce for alce in pracedicto.values() if alce['pracy']==pracy])
	assert len(setadrlangczow)==1,'setadrlangczow: %s'%str(setadrlangczow)
	if list(setadrlangczow)[0]: adrlangczy=defadrlangczy


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
	try: print 'Otóż jest on stringiem "%s"' % str(kolczyraz) ; raise ValueError
	except TypeError:
		print 'Otóź nie jest on nawet stringiem. Jego wartość to:'
		print kolczyraz
		raise TypeError


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
