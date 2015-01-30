# -*- coding: utf-8 -*-
class getkol:
	"""To jest klasa pobierania kolejno bez odstępu czasowego"""
	#	import datetime
	#	from ownlib.download import *
		
	def __init__(self,stacje,pracy,debugu,lan,jezadr,lanchar,iwri,idis,tor=0,czyzapis=False,zapisu='n'):
		assert tor == 0 or tor == 1, "Tor parameter variable doesn't contain 0 nor 1; Exiting."
		if tor == 1: from ownlib.tordown import tordown
		self.tor = tor
		self.torin = tordown(debugu) if tor == 1 else "nico"
		self.lan = lan
		self.jezadr = jezadr
		self.lanchar = lanchar
		sa=0;ssa=0;sw=0;ssw = 0
		stacdict={};slownikczasow={}
		for s in stacje:
			sa=0;sw=0
			a = self.si(s)
			if a[0] == 'a': sa, ssa = 1
			elif a[0] == 'w': sw, ssw = 1
			else:
				try: stacdict[int(s)] = int(a[0])
				except ValueError: stacdict[int(s)] = a[0] if a[0]=="Download failed" else int(a[0])
				slownikczasow[int(s)] = int(a[1])
				try: self.praca(int(s),int(a[0]),int(a[1]),pracy)
				except ValueError: self.praca(int(s),a[0] if a[0]=="Download failed" else int(a[0]),int(a[1]),pracy)
		if ssa == 1:
			stacdictal = {}
			allesstac = 0
			for j in range(1,14):
				try: allone = stacdict[j]
				except: allone = self.si(j)
				stacdictal[j] = int(allone)
				allesstac = allesstac + allone
		if ssw == 1:
			allerstac = 0
			for u in stacdict.keys(): allerstac += int(stacdict[u])
		if ssa == 1: stacdict[0] = allesstac
		if ssw == 1: stacdict[0] = allerstac
		self.stacdict = stacdict
		self.slwcza = slownikczasow
		if tor == 1: self.torin.zabij()
	def si(self,s):
		lan = self.lan
		sa = 0;sw = 0
		if int(s) == 0:
			sa = 1
			a = 'a'
			return a
		elif int(s) == 100:
			sw = 1
			a = 'w'
			return a
		elif int(s) < 0:
			o = int(s) * (-1)
			a = self.si(o)
			return a
		elif int(s) <= 13:
			from ownlib.download import download
			thisisthedownloadinstance = download(int(s),lan.dictu,self.tor,self.torin)
			a = thisisthedownloadinstance.raz()
			return a
		else:
			jezodict = lan.dictu
			print "%s: %s" % (jezodict['badstacparam'],str(s))
			quit()
	def praca(self,st,row,utim,pr,czyzapis=False,zapisywanie=None):
		lan = self.lan
		jezadr = self.jezadr
		lanchar = self.lanchar
		from ownlib.pokaz import pokaz
		if pr == 'n': pracowanie='nie'
		else: pokaz(row,st,utim,pr,lan,jezadr,lanchar)
	def slowstac(self):
		return self.stacdict
	def slowczas(self):
		return self.slwcza
