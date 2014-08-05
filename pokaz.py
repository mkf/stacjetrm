# -*- coding: utf-8 -*-
class pokaz:
	"Klasa pokazujaca pojedynczo"
	from orzeczim import orzeczim
	import datetime
	
	def __init__(self,row,stac,unix,pracy,lang,jezadr,lanchar):
		from orzeczim import orzeczim
		#if stac #dokonczyc watek myslowy
		orze = orzeczim(row,int(stac),unix,pracy,lang,jezadr,lanchar)
	
