# -*- coding: utf-8 -*-
class zapisujrazem:
	"""To jest klasa zapisująca wszystkie stacje razem"""

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
                                if typ=='csv': assert csv.reader(plik)[0][0]=='CzasUNIX',"Plik nie jest w tym typie"
                        cfile.close()
                if typ=='csv':
                        #with open(plik,'ab') as self.csvfile:
                        self.csvfile = open(plik,'ab')
			fildy=("CzasUNIX",'001TOR','002TOR','003TOR','004TOR','005TOR','006TOR','007TOR','008TOR','009TOR','010TOR','011TOR','012TOR','013TOR')
                        writer = csv.DictWriter(self.csvfile,fieldnames=list(fildy))
                        writer.writeheader()
                        self.writer = writer
	def entry(self,czasunix,rowedict):
		if self.czyplik and self.typ='csv':
			rowerdict = {}
			fjeld = list(fildy)
			for stacja in rowedict.keys():
				assert (str(stacja)[0]=='0') and (str(stacja)[-3:]=='TOR'), "Zapis: niepoprawna nazwa stacji [%s], ma byc 0**TOR" % str(stacja)
				assert int(str(stacja)[:3]) < 14 and int(str(stacja)[:3]) > 0 , "Niepoprawna stacja"
				rowery = rowedict[stacja]
				assert (not int(rowery) < 0) and int(rowery)<20. "Żła liczba rowerów"
				rowerdict[str(stacja)]=int(rowery)
				fjeld.remove(stacja)
			for i in fjeld: rowerdict[i]=''
			self.writer.writerow(rowerdict)
