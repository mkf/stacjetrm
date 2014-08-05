# -*- coding: utf-8 -*-
class english:
	u"This is an English language file"
	
	def __init__(self):
		lang = "en"
	def dictu(self):
		slo = {
			"badwaittime": "Incorrect waiting time",
			"badstacparam": "Incorrect station parameter",
			"badlang": "Incorrect language",
			"badpracy": "Incorrect work mode",
			"baddebugu": "Incorrect debug mode",
			"badsm": "Incorrect write mode",
			"nastacji": "On the station",
			"sumallnotsupported": "The feature of sum of all of the stations isn't yet supported. Exiting.",
			"sumchonotsupported": "The feature of sum of the chosen stations isn't yet supported. Exiting.",
			"elektulabormodon": "Choose a work mode",
			"sevivolasketiunprogramonfunkcias": "if you want this program work",
			"najprawdopodobniejtrybpracy": "Most probably the work mode",
			"jestnieprawidlowy": "is incorrect",
		}
		return slo
	def wyd(self, row):
		if row == 0:
			wyd = "is no bicycles "
		elif row == -1:
			wyd = "probably encountered an error, as it shows that there is -1 bicycle, and this is a negative count \n         "
		elif row <= 0:
			wyd = "probably encountered an error, as it shows that there is " + str(row) + " bicycles, and this is a negative count \n          "
		elif row == 1:
			wyd = "is  1 bicycle  "
		elif row >= 2:
			if row <= 9:
				wyd = ("is  " + str(row) + " bicycles ")
			if row >= 10:
				wyd = ("is " + str(row) + " bicycles ")
		else:
			wyd = ", there is no data how many bicycles there are, because an attempt to get known encountered an error"
		return wyd
	def lanstac(self):
		lanstadict = {
			'001TOR': 'Rynek Staromiejski', 
			'002TOR': 'Plac sw. Katarzyny', 
			'003TOR': 'Plac Rapackiego', 
			'004TOR': 'ul. Bulwar Filadelfijski - Brama Klasztorna', 
			'005TOR': 'ul. Szosa Chelminska - Targowisko Miejskie', 
			'006TOR': 'ul. Gagarina - Biblioteka Uniwersytecka', 
			'007TOR': 'ul. Broniewskiego - Tesco', 
			'008TOR': 'ul. Gen. Jozefa Hallera - Polo Market', 
			'009TOR': 'ul. Szosa Chelminska - Polo Market', 
			'010TOR': 'PKP Torun Glowny', 
			'011TOR': 'ul. Dziewulskiego - Komisariat Policji', 
			'012TOR': 'ul. Konstytucji 3 Maja - Pawilon Maciej'
		}
		return lanstadict
		#powyzsze trzeba bedzie przetlumaczyc na angielski