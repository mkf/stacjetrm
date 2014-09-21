# -*- coding: utf-8 -*-
class pars:
	'To jest klasa odczytywania plików pobranych ze Źródła'
	import re
#	rowerky = 0
#	rowery = 0
	def __init__(self, skund, stacyjka, landictu):
		self.landictu = landictu
		self.skund = skund
		self.stacyjka = stacyjka
		stacjowystring = re.sub(r'\D',"",stacyjka)
		stacja = int(stacjowystring)
		
		if skund == "Download failed":
			rowery = "Download failed"
		else:
			import re
			odnaleziono = re.search(r'w na stacji.*szt', skund, re.S)
			wynalezione = odnaleziono.group()
			odnalezione = str(wynalezione)
			comaszukac = 'th.*szt'
			renaleziono = re.search(comaszukac, odnalezione, re.S)
			renalezione = renaleziono.group()
			reodnalezione = re.sub(r'built-in method group of ',"",renalezione)
			rowerki = re.sub(r'\D',"",reodnalezione)
			rowery = int(rowerki)
#			rowery = rowerky
#			def rowery(self):
#
#			rowery = rowerky
		self.rowery = rowery
		stacjinazwa = stacyjka
	def rowerry(self):
		return self.rowery