# -*- coding: utf-8 -*-
class pokaz:
	"""Klasa pokazujaca pojedynczo"""

	def __init__(self, row, stac, unix, pracy, lang, jezadr, lanchar):
		from ownlib.orzeczim import orzeczim
		# if stac #dokonczyc watek myslowy
		orze = orzeczim(row, str(str("%03dTOR" % int(stac))), unix, pracy, lang, jezadr, lanchar)
		if pracy == 'u':
			orze.orz()
			orze.pisul()
		elif pracy == 'l':
			orze.orz()
			orze.pisul()
		elif pracy == 'p':
			orze.pisp()
		elif pracy == 'c':
			orze.pisc()
		elif pracy == 'm':
			orze.pism()
		elif pracy == 'a':
			orze.orz()
			orze.pisfa()
		elif pracy == 'f':
			orze.orz()
			orze.pisfa()
		elif pracy == 't':
			orze.pist()
		else:
			print lang.dictu["elektulabormodon"], lang.dictu["sevivolasketiunprogramonfunkcias"]
			print lang.dictu["najprawdopodobniejtrybpracy"], " ", pracy, " ", lang.dictu["jestnieprawidlowy"]
