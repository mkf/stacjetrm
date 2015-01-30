# -*- coding: utf-8 -*-
class zapisujkolejno:
	"""To jest klasa zapisujaca wszystkie stacje po kolei"""

	def __init__(self, plik, typ='csv', czyplik=True, debugu=True):
		if typ=='csv': import csv
		if czyplik: import os.path
		self.plik = plik
		self.typ = typ
		self.czyplik = czyplik
		#self.pracy = pracy
		self.debugu = debugu
		if czyplik and os.path.isfile(plik): 
			with open(plik,'rb') as cfile:
				if typ=='csv': assert csv.reader(plik)[0][0]=='Stacja',"Plik nie jest w tym typie"
			cfile.close()
		if typ=='csv': 
			#with open(plik,'ab') as self.csvfile:
			self.csvfile = open(plik,'ab')
			writer = csv.DictWriter(self.csvfile,fieldnames=['Stacja','Rowery',"CzasUNIX"])
			writer.writeheader()
			self.writer = writer
	def entry(self,stacja,rowery,czasunix):
		if self.czyplik and self.typ=='csv':
			assert (str(stacja)[0]=='0') and (str(stacja)[-3:]=='TOR'), "Zapis: niepoprawna nazwa stacji [%s], ma byc 0**TOR" % str(stacja)
			assert int(str(stacja)[:3]) < 14 and int(str(stacja)[:3]) > 0 , "Niepoprawna stacja"
			assert (not int(rowery) < 0) and int(rowery)<20. "Żła liczba rowerów"
			self.writer.writerow({'Stacja':str(stacja),'Rowery':int(rowery),"CzasUNIX":int(czasunix)})
