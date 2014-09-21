# -*- coding: utf-8 -*-
class eo_safe:
	u"Tio estas la pakagxo de la esperanta lingvo."
	
	def __init__(self):
		lang='eo-safe'
	def dictu(self):
		slo = {
			"badwaittime": "Malkorektan atendtempon",
			"badstacparam": "Malkorektan staciparametron",
			"badlang": "Malkorektan lingvon",
			"badpracy": "Malkorektan labormodon",
			"baddebugu": "Malkorektan senfusxmodon",
			"badsm": "Malkorektan skribamodon",
			"nastacji": "Al la biciklastacion",
			"sumallnotsupported": "La sumo de la cxio ne estas [supported] jam. [Exiting].",
			"sumchonotsupported": "La sumo de la [wybrane] ne estas [supported] jam. [Exiting].",
			"elektulabormodon": "Elektu labormodon",
			"sevivolasketiunprogramonfunkcias": "se vi volas ke tiun programon funkcias",
			"najprawdopodobniejtrybpracy": "Plej eble ke la labormodo",
			"jestnieprawidlowy": "estas malkorekta.",
			"niepoprwartosc": "Malkorekta valoro",
			"downfail": "Malsargxi malsukcesis",
			"trojliterr": "ERR",
		}
		return slo
	def wyd(self, row):
		if type(row) == int and row == 0:
			wyd = "estas neniu bicikloj"
		elif type(row) == int and row == -1:
			wyd = "okazis iun eraron, cxar gxi transdonas ke tie estas -1 biciklo - kaj tio estas negativa kvanto \n		 "
		elif type(row) == int and row <= 0:
			wyd = "okazis iun eraron, cxar gxi transdonas ke tie estas " + str(row) + " bicikloj - kaj tio estas negativa kvanto \n		  "
		elif type(row) == int and row == 1:
			wyd = "estas 1  biciklo	"
		elif type(row) == int and row >= 2:
			if row <= 9:
				wyd = ("estas " + str(row) + "  bicikloj   ")
			if row >= 10:
				wyd = ("estas " + str(row) + " bicikloj   ")
		elif row == "Download failed":
			wyd = ", ni ne scias kiom bicikloj estas tie, cxar dum la malsargxon de la biciklokvanto malsukcesis"
		else:
			wyd = ", ni ne scias kiom bicikloj estas tie, cxar dum la akiroprovon de la biciklokvanto okazis la eraro, tion gavis [tipon: '%s', valoron: '%s']" % (type(row), str(row))
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
		#powyzsze trzeba bedzie przetlumaczyc na esperanto w bezpiecznym alfabecie metoda x
class eo_natio:
	u"Tio estas la pakaĝo de la esperanta lingvo."
	
	def __init__(self):
		lang='eo-natio'
	def dictu(self):
		slo = {
			"badwaittime": "Malkorektan atendtempon",
			"badstacparam": "Malkorektan staciparametron",
			"badlang": "Malkorektan lingvon",
			"badpracy": "Malkorektan labormodon",
			"baddebugu": "Malkorektan senfuŝmodon",
			"badsm": "Malkorektan skribamodon",
			"nastacji": "Al la biciklastacion",
			"sumallnotsupported": "La sumo de la ĉio ne estas elportita jam. Elirata.",
			"sumchonotsupported": "La sumo de la elektita ne estas elportita jam. Elirata.",
			"elektulabormodon": "Elektu labormodon",
			"sevivolasketiunprogramonfunkcias": "se vi volas ke tiun programon funkcias",
			"najprawdopodobniejtrybpracy": "Plej eble ke la labormodo",
			"jestnieprawidlowy": "estas malkorekta.",
			"niepoprwartosc": "Malkorekta valoro",
			"downfail": "Malsarĝi malsukcesis",
			"trojliterr": "ERR",
		}
		return slo
	def wyd(self, row):
		if type(row) == int and row == 0:
			wyd = "estas neniu bicikloj"
		elif type(row) == int and row == -1:
			wyd = "okazis iun eraron, ĉar ĝi transdonas ke tie estas -1 biciklo - kaj tio estas negativa kvanto \n		 "
		elif type(row) == int and row <= 0:
			wyd = "okazis iun eraron, ĉar ĝi transdonas ke tie estas " + str(row) + " bicikloj - kaj tio estas negativa kvanto \n		  "
		elif type(row) == int and row == 1:
			wyd = "estas 1  biciklo	"
		elif type(row) == int and row >= 2:
			if row <= 9:
				wyd = ("estas " + str(row) + "  bicikloj   ")
			if row >= 10:
				wyd = ("estas " + str(row) + " bicikloj   ")
		elif row == "Download failed":
			wyd = ", ni ne scias kiom bicikloj estas tie, ĉar dum la malsarĝon de la biciklokvanto malsukcesis"
		else:
			wyd = ", ni ne scias kiom bicikloj estas tie, ĉar dum la akiroprovon de la biciklokvanto okazis la eraro, tion gavis [tipon: '%s', valoron: '%s']" % (type(row), str(row))
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
		#powyzsze trzeba bedzie przetlumaczyc na esperanto ze znaczkami