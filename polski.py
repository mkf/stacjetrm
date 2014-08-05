# -*- coding: utf-8 -*-
class pl_natio:
	u"To jest plik języka polskiego"
	
	def __init__(self):
		lang = "pl_natio"
	def dictu(self):
		slo = {
			"badwaittime": "Niepoprawny czas czekania",
			"badstacparam": "Niepoprawny parametr stacji",
			"badlang": "Niepoprawny język",
			"badpracy": "Niepoprawny tryb pracy",
			"baddebugu": "Niepoprawny tryb debugowania",
			"badsm": "Niepoprawny tryb zapisu",
			"nastacji": "Na stacji",
			"sumallnotsupported": "Suma wszystkiego jeszcze nie obsługiwana. Kończenie.",
			"sumchonotsupported": "Suma wybranych jeszcze nie obsługiwana. Kończenie.",
			"elektulabormodon": "Wybierz tryb pracy",
			"sevivolasketiunprogramonfunkcias": "jeżeli chcesz, by ten program działał",
			"najprawdopodobniejtrybpracy": "Najprawdopodobniej tryb pracy",
			"jestnieprawidlowy": "jest nieprawidłowy",
		}
		return slo
	def wyd(self, row):
		if row == 0:
			wyd = "nie ma rowerów"
		elif row == -1:
			wyd = "najprawdopodobniej wystąpił błąd - stacja twierdzi, że jest tam -1 rower - a jest to liczba ujemna \n         "
		elif row <= 0:
			wyd = "najprawdopodobniej wystąpił błąd - stacja twierdzi, że jest tam " + str(row) + " rowerów - a jest to liczba ujemna \n          "
		elif row == 1:
			wyd = "jest 1  rower    "
		elif row >= 2:
			if row <= 4:
				wyd = ("są   " + str(row) + "  rowery   ")
			elif row >= 5:
				wyd = ("jest " + str(row) + "  rowerów  ")
			elif row >= 10:
				wyd = ("jest " + str(row) + " rowerów   ")
			elif row >= 22:
				wyd = ("są   " + str(row) + " rowery, choć to praktycznie niemożliwe, gdyż stacja tyle nie pomieści"
		else:
			wyd = ", nie wiemy ile rowerów jest na tej stacji, ponieważ próba pobrania informacji zakończyła się błędem"
		return wyd
	def lanstac(self):
		lanstadict = {
			'001TOR': 'Rynek Staromiejski', 
			'002TOR': 'Plac św. Katarzyny', 
			'003TOR': 'Plac Rapackiego', 
			'004TOR': 'ul. Bulwar Filadelfijski - Brama Klasztorna', 
			'005TOR': 'ul. Szosa Chełmińska - Targowisko Miejskie', 
			'006TOR': 'ul. Gagarina - Biblioteka Uniwersytecka', 
			'007TOR': 'ul. Broniewskiego - Tesco', 
			'008TOR': 'ul. Gen. Józefa Hallera - Polo Market', 
			'009TOR': 'ul. Szosa Chełmińska - Polo Market', 
			'010TOR': 'PKP Toruń Główny', 
			'011TOR': 'ul. Dziewulskiego - Komisariat Policji', 
			'012TOR': 'ul. Konstytucji 3 Maja - Pawilon Maciej',
		}
		return lanstadict
class pl_safe:
	u"To jest plik jezyka polskiego"
	
	def __init__(self):
		lang = "pl_safe"
	def dictu(self):
		slo = {
			"badwaittime": "Niepoprawny czas czekania",
			"badstacparam": "Niepoprawny parametr stacji",
			"badlang": "Niepoprawny jezyk",
			"badpracy": "Niepoprawny tryb pracy",
			"baddebugu": "Niepoprawny tryb debugowania",
			"badsm": "Niepoprawny tryb zapisu",
			"nastacji": "Na stacji",
			"sumallnotsupported": "Suma wszystkiego jeszcze nie obslugiwana. Konczenie.",
			"sumchonotsupported": "Suma wybranych jeszcze nie obslugiwana. Konczenie.",
			"elektulabormodon": "Wybierz tryb pracy",
			"sevivolasketiunprogramonfunkcias": "jezeli chcesz, by ten program dzialal",
			"najprawdopodobniejtrybpracy": "Najprawdopodobniej tryb pracy",
			"jestnieprawidlowy": "jest nieprawidlowy",
		}
		return slo
	
	def wyd(self, row):
		if row == 0:
			wyd = "nie ma rowerow"
		elif row == -1:
			wyd = "najprawdopodobniej wystapil blad - stacja twierdzi, ze jest tam -1 rower - a jest to liczba ujemna \n         "
		elif row <= 0:
			wyd = "najprawdopodobniej wystapil blad - stacja twierdzi, ze jest tam " + str(row) + " rowerow - a jest to liczba ujemna \n          "
		elif row == 1:
			wyd = "jest 1  rower    "
		elif row >= 2:
			if row <= 4:
				wyd = ("sa   " + str(row) + "  rowery   ")
			elif row >= 5:
				wyd = ("jest " + str(row) + "  rowerow  ")
			elif row >= 10:
				wyd = ("jest " + str(row) + " rowerow   ")
			elif row >= 22:
				wyd = ("sa   " + str(row) + " rowery, choc to praktycznie niemozliwe, gdyz stacja tyle nie pomiesci"
		else:
			wyd = ", nie wiemy ile rowerow jest na tej stacji, poniewaz proba pobrania informacji zakonczyla się bledem"
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
			'012TOR': 'ul. Konstytucji 3 Maja - Pawilon Maciej',
		}
		return lanstadict