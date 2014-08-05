# -*- coding: utf-8 -*-
class pokaz:
	"Klasa pokazujaca pojedynczo"
	from orzeczim import orzeczim
	import datetime
	
	def __init__(self,row,stac,unix,pracy,lang,jezadr,lanchar):
		from orzeczim import orzeczim
		#if stac #dokonczyc watek myslowy
		orze = orzeczim(row,int(stac),unix,pracy,lang,jezadr,lanchar)
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
			print lang.dictu()["elektulabormodon"]," ",lang.dictu()["sevivolasketiunprogramonfunkcias"],"."
			print lang.dictu()["najprawdopodobniejtrybpracy"]," ", pracy, " ",lang.dictu()["jestnieprawidlowy"],"."
