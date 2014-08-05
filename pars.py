# -*- coding: utf-8 -*-
class pars:
	'To jest klasa odczytywania plików pobranych ze Źródła'
	import re
#	rowerky = 0
#	rowery = 0
	def __init__(self, skund, stacyjka, lan):
		import re
		self.lan = lan
		self.skund = skund
		self.stacyjka = stacyjka
		odnaleziono = re.search(r'w na stacji.*szt', skund, re.S)
		wynalezione = odnaleziono.group()
		odnalezione = str(wynalezione)
		stacjowystring = re.sub(r'\D',"",stacyjka)
		stacja = int(stacjowystring)
		comaszukac = 'th.*szt'
		renaleziono = re.search(comaszukac, odnalezione, re.S)
		renalezione = renaleziono.group()
		reodnalezione = re.sub(r'built-in method group of ',"",renalezione)
		rowerki = re.sub(r'\D',"",reodnalezione)
		rowery = int(rowerki)
		self.rowery = rowery
		stacjinazwa = stacyjka
#		rowery = rowerky
#		def rowery(self):
#
#		rowery = rowerky
	def rowerry(self):
		return self.rowery