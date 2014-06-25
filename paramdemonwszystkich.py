# -*- coding: utf-8 -*-
class paramdemonwszystkich:
	u"To jest klasa parametrów demonwszystkich"
	import sys
	import re
	listatrybowprac = ('f', 'l', 'u', 'a', 't', 'k', 'c', 'm', 'n', 'd')
	defpracy = "a"
	listatrybowdebugu = ('f', 'y', 'n', 'd')
	defdebugu = "n"
	listatrybowzapisu = ('c', 'n', 's', 'd')
	defsm = "n"
	deft = 60
	deflang = "e"
	dictstacyjeistnieje = 0
	wstacyjejestrange = 0
	dictstacyjeposiada = 0
	stacyjeistnieje = 0
	parametrstacjibyl = 0
	parametrczasuczekaniabyl = 0
	parametrtrybowpracbyl = 0
	parametrtrybowdebugubyl = 0
	parametrtrybowzapisubyl = 0
	def __init__(self,argu)
		self.argu = argu
		for a in range(1,len(argu)):
			at = argu[a]
			if at[0] == "l":
				try:
					if at[1] == "e":
						lang = "e"
						from esperanto import *
						lan = esperanto()
					elif at[1] == "a":
						lang = "a"
						from english import *
						lan = english()
					elif at[1] == "p":
						lang = "p"
						from polski import *
						lan = polski()
					elif at[1] == "d":
						lang = "d"
						from deutsch import *
						lan = deutsch()
					else:
						self.zlyjazyk()
				except:
					self.zlyjazyk()
				self.lang = lang
			elif at[0] == "t":
				parametrczasuczekaniabyl = 1
				if at[1] == "d":
					t = deft
				else:
					tc = re.sub("\D","",at)
					try:
						t = int(tc)
					except:
						print "%s: %s"(lan.badwaittime,at)
						quit()
			elif at[0] == "s":
				parametrstacjibyl = 1
				if stacyjeistnieje = 0:
					stacyje = []
					stacyjeistnieje = 1
				if dictstacyjeistnieje = 0:
					stacyjedict = {}
					dictstacyjeistnieje = 1
				if at[1] == "w":
					stacyje.append(range(1,13))
					wstacyjejestrange = 1
				elif isinstance(at[1], self.char_range(a,l)):
					stacyjechoosestr = re.sub("\D","",at)
					stacyjedict.update((at[1])=(int(stacyjechoosestr)))
					dictstacyjeposiada = 1
				else:
					print "%s: %s"(lan.badstacparam,at)
			elif at[0] == "p":
				parametrtrybowpracbyl = 1
				if isinstance(at[1], listatrybowprac):
					if at[1] == "d":
						pracy = defpracy
					else:
						pracy = at[1]
				else:
					print "%s: %s"(lan.badpracy,at)
			elif at[0] == "b":
				parametrtrybowdebugubyl = 1
				if isinstance(at[1], listatrybowdebugu)
					if at[1] == "d":
						debugu = defdebugu
					else:
						debugu = at[1]
				else:
					print "%s: %s"(lan.baddebugu,at)
			elif at[0] == "w":
				parametrtrybowzapisubyl = 1
				if isinstance(at[1], listatrybowzapisu)
					if at[1] == "d":
						sm = defsm
					else:
						sm = at[1]
				else:
					print "%s: %s"(lan.badsm,at)
					
		if parametrstacjibyl = 1:
			if wstacyjejestrange = 1:
				stacje = stacyje.tuple()
			elif dictstacyjeposiada = 1:
				for znaczek in self.char_range(a,l)
					stacyje.append(stacyjedict[znaczek])
				stacje = stacyje.tuple()
		elif parametrstacjibyl = 0:
			stacyje = range(1,13)
			stacje = stacyje.tuple
					
	def char_range(c1, c2):
		for c in xrange(ord(c1), ord(c2)+1):
			yield chr(c)
	def lng(self):
		return self.lang
	def zlyjazyk(self):
		from esperanto import *
		espera = esperanto()
		from english import *
		engli = english()
		from polish import *
		polsk = polski()
		from deutsch import *
		deuts = deutsch()
		for badlang in ((espera.badlang()), (engli.badlang()), (polsk.badlang()), (deuts.balang())): 
			print "%s: %s"(badlang,at[1:])
		quit()

