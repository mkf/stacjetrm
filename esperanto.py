# -*- coding: utf-8 -*-
class eo_safe:
	u"""Tio estas la pakagxo de la esperanta lingvo."""

	def __init__(self):
		lang = 'eo-safe'

	@property
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

	@staticmethod
	def wyd(row):
		if type(row) == int and row == 0:
			wyd = "estas neniu bicikloj"
		elif type(row) == int and row == -1:
			wyd = "okazis iun eraron, cxar gxi transdonas ke tie estas -1 biciklo - kaj tio estas negativa kvanto \n		 "
		elif type(row) == int and row <= 0:
			wyd = "okazis iun eraron, cxar gxi transdonas ke tie estas " + str(
				" {:2d} ".format(row)) + " bicikloj - kaj tio estas negativa kvanto \n		  "
		elif type(row) == int and row == 1:
			wyd = "estas  1  biciklo    "
		elif type(row) == int and row >= 2:
			if row <= 9:
				wyd = ("estas " + str("{:2d} ".format(row)) + " bicikloj   ")
			if row >= 10:
				wyd = ("estas " + str("{:2d} ".format(row)) + " bicikloj   ")
		elif row == "Download failed":
			wyd = ", ni ne scias kiom bicikloj estas tie, cxar dum la malsargxon de la biciklokvanto malsukcesis"
		else:
			wyd = ", ni ne scias kiom bicikloj estas tie, cxar dum la akiroprovon de la biciklokvanto okazis la eraro, tion gavis [tipon: '%s', valoron: '%s']" % (
				type(row), str(" {:2d} ".format(row)))
		return wyd

	@property
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
			'013TOR': 'ul. Dabrowskiego — Dworzec autobusowy'
		}
		return lanstadict

	# powyzsze trzeba bedzie przetlumaczyc na esperanto w bezpiecznym alfabecie metoda x


class eo_natio:
	u"""Tio estas la pakaĝo de la esperanta lingvo."""

	def __init__(self):
		lang = 'eo-natio'

	@property
	def dictu(self):
		slo = {
			"badwaittime": u"Malkorektan atendtempon",
			"badstacparam": u"Malkorektan staciparametron",
			"badlang": u"Malkorektan lingvon",
			"badpracy": u"Malkorektan labormodon",
			"baddebugu": u"Malkorektan senfuŝmodon",
			"badsm": u"Malkorektan skribamodon",
			"nastacji": u"Al la biciklastacion",
			"sumallnotsupported": u"La sumo de la ĉio ne estas elportita jam. Elirata.",
			"sumchonotsupported": u"La sumo de la elektita ne estas elportita jam. Elirata.",
			"elektulabormodon": u"Elektu labormodon",
			"sevivolasketiunprogramonfunkcias": u"se vi volas ke tiun programon funkcias",
			"najprawdopodobniejtrybpracy": u"Plej eble ke la labormodo",
			"jestnieprawidlowy": u"estas malkorekta.",
			"niepoprwartosc": u"Malkorekta valoro",
			"downfail": u"Malsarĝi malsukcesis",
			"trojliterr": u"ERR",
		}
		return slo

	@staticmethod
	def wyd(row):
		if type(row) == int and row == 0:
			wyd = u"estas neniu bicikloj"
		elif type(row) == int and row == -1:
			wyd = u"okazis iun eraron, ĉar ĝi transdonas ke tie estas -1 biciklo - kaj tio estas negativa kvanto \n		 "
		elif type(row) == int and row <= 0:
			wyd = u"okazis iun eraron, ĉar ĝi transdonas ke tie estas " + str(
				" {:2d} ".format(row)) + " bicikloj - kaj tio estas negativa kvanto \n		  "
		elif type(row) == int and row == 1:
			wyd = u"estas  1  biciklo    "
		elif type(row) == int and row >= 2:
			if row <= 9:
				wyd = (u"estas" + str(" {:2d} ".format(row)) + u" bicikloj   ")
			if row >= 10:
				wyd = (u"estas" + str(" {:2d} ".format(row)) + u" bicikloj   ")
		elif row == "Download failed":
			wyd = u", ni ne scias kiom bicikloj estas tie, ĉar dum la malsarĝon de la biciklokvanto malsukcesis"
		else:
			wyd = u", ni ne scias kiom bicikloj estas tie, ĉar dum la akiroprovon de la biciklokvanto okazis la eraro, tion gavis [tipon: '%s', valoron: '%s']" % (
				type(row), str(" {:2d} ".format(row)))
		return wyd

	@property
	def lanstac(self):
		lanstadict = {
			'001TOR': u'Rynek Staromiejski',
			'002TOR': u'Plac sw. Katarzyny',
			'003TOR': u'Plac Rapackiego',
			'004TOR': u'ul. Bulwar Filadelfijski - Brama Klasztorna',
			'005TOR': u'ul. Szosa Chelminska - Targowisko Miejskie',
			'006TOR': u'ul. Gagarina - Biblioteka Uniwersytecka',
			'007TOR': u'ul. Broniewskiego - Tesco',
			'008TOR': u'ul. Gen. Jozefa Hallera - Polo Market',
			'009TOR': u'ul. Szosa Chelminska - Polo Market',
			'010TOR': u'PKP Torun Glowny',
			'011TOR': u'ul. Dziewulskiego - Komisariat Policji',
			'012TOR': u'ul. Konstytucji 3 Maja - Pawilon Maciej',
			'013TOR': u'ul. Dabrowskiego - Dworzec autobusowy'
		}
		return lanstadict
		# powyzsze trzeba bedzie przetlumaczyc na esperanto ze znaczkami