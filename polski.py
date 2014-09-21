# -*- coding: utf-8 -*-
class pl_natio:
	u"To jest plik języka polskiego"
	
	def __init__(self):
		lang = "pl_natio"
	def dictu(self):
		slo = {
			"badwaittime": u"Niepoprawny czas czekania",
			"badstacparam": u"Niepoprawny parametr stacji",
			"badlang": u"Niepoprawny język",
			"badpracy": u"Niepoprawny tryb pracy",
			"baddebugu": u"Niepoprawny tryb debugowania",
			"badsm": u"Niepoprawny tryb zapisu",
			"nastacji": u"Na stacji",
			"sumallnotsupported": u"Suma wszystkiego jeszcze nie obsługiwana. Kończenie.",
			"sumchonotsupported": u"Suma wybranych jeszcze nie obsługiwana. Kończenie.",
			"elektulabormodon": u"Wybierz tryb pracy",
			"sevivolasketiunprogramonfunkcias": u"jeżeli chcesz, by ten program działał",
			"najprawdopodobniejtrybpracy": u"Najprawdopodobniej tryb pracy",
			"jestnieprawidlowy": u"jest nieprawidłowy",
			"trojliterr": u"BŁĄ",
		}
		return slo
	def wyd(self, row):
		if type(row) == int and row == 0:
			wyd = u"  nie ma rowerów"
		elif type(row) == int and row == -1:
			wyd = u"najprawdopodobniej wystąpił błąd - stacja twierdzi, że jest tam -1 rower - a jest to liczba ujemna \n		 "
		elif type(row) == int and row <= 0:
			wyd = u"najprawdopodobniej wystąpił błąd - stacja twierdzi, że jest tam " + str(row) + " rowerów - a jest to liczba ujemna \n		  "
		elif type(row) == int and row == 1:
			wyd = u"jest  1  rower	"
		elif type(row) == int and row >= 2:
			if row <= 4:
				wyd = (u"są	" + str(row) + u"  rowery   ")
			elif row >= 5:
				wyd = (u"jest  " + str(row) + u"  rowerów  ")
			elif row >= 10:
				wyd = (u"jest " + str(row) + u"  rowerów   ")
			elif row >= 22:
				wyd = (u"są   " + str(row) + u"  rowery, choć to praktycznie niemożliwe, gdyż stacja tyle nie pomieści")
		elif row == "Download failed":
			wyd = u", nie wiemy ile rowerów jest na tej stacji, ponieważ pobieranie zakończyło się błędem"
		else:
			wyd = u", nie wiemy ile rowerów jest na tej stacji, ponieważ próba zdobycia informacji zakończyła się błędem, zwróciłą [typ: '%s', wartość: '%s']" % (type(row), str(row))
		return wyd
	def lanstac(self):
		lanstadict = {
			'001TOR': u'Rynek Staromiejski',
			'002TOR': u'Plac św. Katarzyny',
			'003TOR': u'Plac Rapackiego',
			'004TOR': u'ul. Bulwar Filadelfijski - Brama Klasztorna',
			'005TOR': u'ul. Szosa Chełmińska - Targowisko Miejskie',
			'006TOR': u'ul. Gagarina - Biblioteka Uniwersytecka',
			'007TOR': u'ul. Broniewskiego - Tesco',
			'008TOR': u'ul. Gen. Józefa Hallera - Polo Market',
			'009TOR': u'ul. Szosa Chełmińska - Polo Market',
			'010TOR': u'PKP Toruń Główny',
			'011TOR': u'ul. Dziewulskiego - Komisariat Policji',
			'012TOR': u'ul. Konstytucji 3 Maja - Pawilon Maciej',
		}
		return lanstadict
class pl_safe:
	"To jest plik jezyka polskiego"
	
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
			"trojliterr": "ERR",
		}
		return slo
	
	def wyd(self, row):
		if type(row) == int and row == 0:
			wyd = "  nie ma rowerow"
		elif type(row) == int and row == -1:
			wyd = "najprawdopodobniej wystapil blad - stacja twierdzi, ze jest tam -1 rower - a jest to liczba ujemna \n		 "
		elif type(row) == int and row <= 0:
			wyd = "najprawdopodobniej wystapil blad - stacja twierdzi, ze jest tam " + str(row) + " rowerow - a jest to liczba ujemna \n		  "
		elif type(row) == int and row == 1:
			wyd = "jest 1  rower	"
		elif type(row) == int and row >= 2:
			if row <= 4:
				wyd = ("sa	" + str(row) + "  rowery   ")
			elif row >= 5:
				wyd = ("jest  " + str(row) + "  rowerow  ")
			elif row >= 10:
				wyd = ("jest " + str(row) + "  rowerow   ")
			elif row >= 22:
				wyd = ("sa   " + str(row) + "  rowery, choc to praktycznie niemozliwe, gdyz stacja tyle nie pomiesci")
		elif row == "Download failed":
			wyd = ", nie wiemy ile rowerow jest na tej stacji, poniewaz pobieranie zakonczylo się bledem"
		else:
			wyd = ", nie wiemy ile rowerow jest na tej stacji, poniewaz proba zdobycia informacji zakonczyla sie bledem, zwrocila [typ: '%s', wartosc: '%s']" % (type(row), str(row))
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