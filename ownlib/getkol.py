# -*- coding: utf-8 -*-
class getkol:
	"""To jest klasa pobierania kolejno bez odstępu czasowego"""
	#	import datetime
	#	from ownlib.download import *
        from ownlib.db import *
	def __init__(self,stacje,pracy,debugu,lan,jezadr,lanchar,iwri,idis,czyzapis=False,zapisu='n',czydb=True,plikdb='trmdata.db'):
		self.lan = lan ; self.jezadr = jezadr ; self.lanchar = lanchar
		ssa=0;ssw=0  #te bardziej stałe odpowiedniki sa i sw. To co w sa i sw idzie też tu, ale sa i sw są zerowane po jednej pętli.
		stacdict={};slownikczasow={}
                self.czydb = czydb
                self.plikdb = plikdb
                #TODO
		for s in stacje:
			sa=0;sw=0
			a = self.si(s)
			if a[0] == 'a': sa=1;ssa=1
			elif a[0] == 'w': sw=1;ssw=1
			else:
				try: stacdict[int(s)] = int(a[0])
				except ValueError: stacdict[int(s)] = a[0] if a[0]=="Download failed" else int(a[0])
				slownikczasow[int(s)] = int(a[1])
				try: self.praca(int(s),int(a[0]),int(a[1]),pracy)
				except ValueError: self.praca(int(s),a[0] if a[0]=="Download failed" else int(a[0]),int(a[1]),pracy)
		if ssa == 1:
			stacdictal = {} ; allesstac = 0
			for j in range(1,27):
				try: allone = stacdict[j]
				except: allone = self.si(j)
				stacdictal[j] = int(allone)
				allesstac = allesstac + allone
		if ssw == 1: 
			allerstac = 0
			for u in stacdict.keys(): allerstac += int(stacdict[u])
		if ssa == 1: stacdict[0] = allesstac
		if ssw == 1: stacdict[0] = allerstac
		self.stacdict = stacdict ; self.slwcza = slownikczasow
	def si(self,s):
		lan = self.lan
		sa = 0;sw = 0
		assert int(s) == 0 or int(s) == 100 or int(s) < 0 or int(s) <=26, "%s: %s" % (lan.dictu['badstacparam'],str(s))
		if int(s) == 0: sa = 1 ; a = 'a' ; return a
		elif int(s) == 100: sw = 1;a = 'w';return a
		elif int(s) < 0: o = int(s) * (-1) ; a = self.si(o) ; return a
		elif int(s) <= 26:
			from ownlib.download import download
			thisisthedownloadinstance = download(int(s),lan.dictu)
			a = thisisthedownloadinstance.raz()
			return a
	def praca(self,st,row,utim,pr,czyzapis=False,zapisywanie=None):
		lan = self.lan;jezadr = self.jezadr;lanchar = self.lanchar
		from ownlib.pokaz import pokaz
		if pr == 'n': pracowanie='nie'
                if self.czydb: pass #TODO
		else: pokaz(row,st,utim,pr,lan,jezadr,lanchar)
	def slowstac(self):
		return self.stacdict
	def slowczas(self):
		return self.slwcza
