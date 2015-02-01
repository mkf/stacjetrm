#!/usr/bin/python
# -*- coding: utf-8 -*-
allsta=[1,2,3,4,5,6,7,8,9,10,11,12,13];defsta=allsta;defpracy="f";defdebugu="n";defwritemode="n";defwaitbetweenloops="singlecheck";deflang="e"
defget = "k";defadrlangczy = "l";defadrchar = 'l';defwvt = 24;defwvc = 1000
from ownlib.argparsingtrmstacli import argparsowanie
parmetry=argparsowanie(allsta,defsta,defpracy,defdebugu,defwritemode,defwaitbetweenloops,deflang,defget,defadrlangczy,defadrchar,defwvt,defwvc)

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

# —————————————————————-LANGUAGES ----————————————————————
langs = {
	'eo': {'fullname':'esperanto','natiothing':True,'lanchar_a':'n'},
	'en': {'fullname':'english','natiothing':False,'lanchar_a':'n'},
	'pl': {'fullname':'polish','natiothing':True,'lanchar_a':'y'},
	'de': {'fullname':'deutsch','natiothing':True,'lanchar_a':'y'}
}
if parmetry.langenglish:
	lang = "en"
	if lanchar == 'a': lanchar = 'n'
	from ownlib.lang.english import * ; lan = english()
elif parmetry.langesperanto:
	lang = "eo"
	if lanchar == 'a': lanchar = 'y'
	if lanchar == 'y': from ownlib.lang.esperanto import eo_natio ; lan = eo_natio()
	if lanchar == 'n': from ownlib.lang.esperanto import eo_safe ; lan = eo_safe()
elif parmetry.langpolski:
	lang = "pl"
	if lanchar == 'a': lanchar = 'y'
	if lanchar == 'y': from ownlib.lang.polski import pl_natio ; lan = pl_natio()
	if lanchar == 'n': from ownlib.lang.polski import pl_safe ; lan = pl_safe()
elif parmetry.langdeutsch:
	lang = "de"
	if lanchar == 'a': lanchar = 'y'
	if lanchar == 'y': from ownlib.lang.deutsch import de_natio ; lan = de_natio()
	if lanchar == 'n': from ownlib.lang.deutsch import de_safe ; lan = de_safe()
else:
	lang = "eo"
	if lanchar == 'a': lanchar = 'n'
	if lanchar == 'y': from ownlib.lang.esperanto import eo_natio ; lan = eo_natio()
	if lanchar == 'n': from ownlib.lang.esperanto import eo_safe ; lan = eo_safe()
#  END:___________ LANGUAGES -------------------------------


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
if parmetry.pracyfulladrlangchosen: pracy = "f" ; adrlangczy = "c" ; kolczyraz = "k"
elif parmetry.pracyfulladrlanglocal: pracy = "f" ; adrlangczy = "l" ; kolczyraz = "k"
elif parmetry.pracylong: pracy = "l" ; kolczyraz = "k"
elif parmetry.pracyrazem: pracy = "r" ; kolczyraz = "r"
elif parmetry.pracyrazkomp: pracy = "rk" ; kolczyraz = "r"
elif parmetry.pracyuser: pracy = "u" ; kolczyraz = "k"
elif parmetry.pracyadresadrlangchosen: pracy = "a" ; kolczyraz = "k" ; adrlangczy = "c"
elif parmetry.pracyadresadrlanglocal: pracy = "a" ; kolczyraz = "k" ; adrlangczy = "l"
elif parmetry.pracytabelaadrlangchosen: pracy = "t" ; kolczyraz = "k" ; adrlangczy = "c"
elif parmetry.pracytabelaadrlanglocal: pracy = "t" ; kolczyraz = "k" ; adrlangczy = "l"
elif parmetry.pracykomp: pracy = "k" ; kolczyraz = "k"
elif parmetry.pracycompressed: pracy = "c" ; kolczyraz = "k"
elif parmetry.pracyminim: pracy = "m" ; kolczyraz = "k"
elif parmetry.pracynone: pracy = "n"  ; kolczyraz = "k"
elif parmetry.pracydef: 
	pracy = defpracy ; adrlangczy = defadrlangczy ; adrchar = defadrchar
	assert pracy in ['f','l','u','a','t','k','c','m','r','rk','n']
	if pracy in ['f','l','u','a','t','k','c','m']: kolczyraz = "k"
	elif pracy == "r" or pracy == "rk": kolczyraz = "r"
	elif pracy == "n": kolczyraz = "n"
else:
	pracy = defpracy ; adrlangczy = defadrlangczy ; adrchar = defadrchar
	assert pracy in ['f','l','u','a','t','k','c','m','r','rk','n']
	if pracy in ['f','l','u','a','t','k','c','m']: kolczyraz = "k"
	elif pracy == "r" or pracy == "rk": kolczyraz = "r"
	elif pracy == "n": kolczyraz = "n"

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
		import time.sleep
		while True: getkol(sta,pracy,debugu,lan,jezadr,lanchar,instadisp,instawrite) ; time.sleep(waitbetweenloops)
elif pob == 'j':  # jednocześnie
	from ownlib.getjednoczesnie import *
	if waitbetweenloops == "singlecheck": getjednoczesnie(sta, pracy, debugu, lan, jezadr, lanchar, instadisp, instawrite)
	elif type(waitbetweenloops) == int:
		import time.sleep
		while True: getjednoczesnie(sta,pracy,debugu,lan,jezadr,lanchar,instadisp,instawrite) ; time.sleep(waitbetweenloops)
elif pob == 'w':  # kolejno-wait (getkolwait)
	pass
