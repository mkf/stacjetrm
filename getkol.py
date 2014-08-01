# -*- coding: utf-8 -*-
class getkol:
	"To jest klasa pobierania kolejno bez odstępu czasowego"
	from download import *
#	import datetime
	import datetime
#	from download import *
		
	def __init__(self,stacje,pracy,lang,jezadr,lanchar):
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
				self.praca(int(s),int(a[0]),int(a[1]),pracy,lang,jezadr,lanchar)
		if ssa == 1:
			stacdictal = {}
			allesstac = 0
			for j in range(1,13):
				try:
					allone = stacdict[j]
				except:
					allone = self.si(j,lang,jezadr,lanchar)
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
	def si(self,s,lang,jezadr,lanchar):
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
			a = self.si(o,lang,jezadr,lanchar)
			return a
		elif int(s) < 13:
			download(int(s))
			a = download.raz()
			return a
		else:
			if lang == "en":
				from english import *
				lan = english()
			elif lang == "eo":
				if lanchar == 'y':
					from esperanto import eo_natio
					lan = eo_natio()
				if lanchar == 'n':
					from esperanto import eo_safe
					lan = eo_safe()
			elif lang == "pl":
				if lanchar == 'y':
					from polski import pl_natio
					lan = pl_natio()
				if lanchar == 'n':
					from polski import pl_safe
					lan = pl_safe()
			elif lang = "de":
				if lanchar == 'y':
					from deutsch import de_natio
					lan = de_natio()
				if lanchar == 'n':
					from deutsch import de_safe
					lan = de_safe()
			else:
				print "An error occured: no such language possible as %s" % lang
				quit()
			jezodict = lan.dictu()
			print "%s: %s" % jezyczek[badstacparam],str(s)
			quit()
	def praca(self,st,row,utim,pr,lang,jezadr,lanchar):
		from pokaz import *
		if pr == 'n':
			pracowanie='nie'
		#elif pr == 'f' or pr == 'l' or pr == 'u' or pr == 'a' or pr == 't' or pr == 'k' or pr == 'c' or pr == 'm':
		else:
			pokaz(row,st,utim,pr,lang,jezadr,lanchar)
	def slowstac(self):
		return self.stacdict
	def slowczas(self):
		return self.slwcza
#	def pobierz(self):
#		
#	def
