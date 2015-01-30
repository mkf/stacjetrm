# -*- coding: utf-8 -*-
class zapisujkolejno:
	"""To jest klasa zapisujaca wszystkie stacje po kolei"""

	def __init__(self, plik, typ='csv', czyplik=True, debugu):
		if typ=='csv': import csv
		if czyplik: import os.path
		self.plik = plik
		self.typ = typ
		self.czyplik = czyplik
		#self.pracy = pracy
		self.debugu = debugu
		if czyplik and os.path.isfile(plik): 
			with open(plik,'rb') as cfile:
				if typ='csv': assert csv.reader(plik)[0][0]=='Stacja',"Plik nie jest w tym typie"
			cfile.close()
		if typ=='csv': with open(plik,'a') as csvfile:
			writer = csv.DictWriter(csvfile,fieldnames=['Stacja','Rowery',"CzasUNIX"])
			writer.writeheader()
			self.writer = writer
	def entry(self,stacja,rowery,czasunix):
		if self.czyplik and self.typ=='csv':
			assert (str(stacja)[0]=='0') and (str(stacja)[-3:]=='TOR'), "Zapis: niepoprawna nazwa stacji [%s], ma byc 0**TOR" % str(stacja)
			self.writer.writerow({'Stacja':str(stacja),'Rowery':int(rowery),"CzasUNIX":int(czasunix)})
