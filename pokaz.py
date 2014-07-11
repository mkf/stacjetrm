# -*- coding: utf-8 -*-
class pokaz:
	"Klasa pokazujaca pojedynczo"
	from orzeczim import *
	
	def __init__(self,row,stac,unix,dz,cz,prac):
		orze = orzeczim(row, stacjinazwa, unix, dzien, czas)
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
			orze.pisa()
		elif pracy == 't':
			orze.pist()
		else:
			print "Elektu labormodo a, l, u, p, c aux m se vi volas ke tiun programon funkcas."
			print "Plej eble ke la labormodo ", pracy, " estas malbona."

	