# -*- coding: utf-8 -*-
class getkol:
	"To jest klasa pobierania kolejno bez odstępu czasowego"
	from download import *
#	import datetime
	import datetime
#	from download import *
		
	def __init__(self,stacje,pracy):
		sa = 0
		ssa = 0
		sw = 0
		ssw = 0
		stacdict = {}
		slownikczasow = {}
		for s in stacje:
			sa = 0
			sw = 0
			a = self.si(s)
			if a[0] == 'a':
				sa = 1
				ssa = 1
			elif a[0] == 'w':
				sw = 1
				ssw = 1
			else:
				stacdict[int(s)] = int(a[0])
				slownikczasow[int(s)] = int(a[1])
				self.praca(int(s),int(a[0]),int(a[1]),pracy)
		if ssa == 1:
			stacdictal = {}
			allesstac = 0
			for j in range(1,13):
				try:
					allone = stacdict[j]
				except:
					allone = self.si(j)
				stacdictal[j] = int(allone)
				allesstac = allesstac + allone
		if ssw == 1:
			allerstac = 0
			for u in stacdict.keys():
				allerstac = allerstac + int(stacdict[u])
		if ssa == 1:
			stacdict[0] = allesstac
		if ssw == 1:
			stacdict[0] = allerstac
		self.stacdict = stacdict
		self.slwcza = slownikczasow
	def si(self,s):
		sa = 0
		sw = 0
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
		elif int(s) < 13:
			download(int(s))
			a = download.raz()
			return a
		else:
			print "Malkorekta biciklstacio: %s" % str(s)
			quit()
	def praca(self,st,row,utim,pr):
		from pokaz import *
		if pr == 'n':
			pracowanie='nie'
		#elif pr == 'f' or pr == 'l' or pr == 'u' or pr == 'a' or pr == 't' or pr == 'k' or pr == 'c' or pr == 'm':
		else:
			pokaz(row,st,utim,pr)
	def slowstac(self):
		return self.stacdict
	def slowczas(self):
		return self.slwcza
#	def pobierz(self):
#		
#	def
