# -*- coding: utf-8 -*-
class paramdemonwszystkich:
	u"To jest klasa parametrów demonwszystkich"
	import sys
	import re
	defpracy = "a"
	defdebugu = "n"
	defsm = "n"
	deft = 60
	deflang = "e"
	dictstacyjeistnieje = 0
	wstacyjejestrange = 0
	dictstacyjeposiada = 0
	stacyjeistnieje = 0
	parametrstacjibyl = 0
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
				except:
					from esperanto import *
					espera = esperanto()
					from english import *
					engli = english()
					from polish import *
					polsk = polski()
					from deutsch import *
					deuts = deutsch()
					for badlang in ((espera.badlang()), (engli.badlang()), (polsk.badlang()), (deuts.badlang())):
						print "%s: %s"(badlang,at[1:])
					quit()
				self.lang = lang
			elif at[0] == "t":
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
			elif at[0] == "
		if parametrstacjibyl = 1:
			if wstacyjejestrange = 1:
				stacje = stacyje.tuple()
			elif dictstacyjeposiada = 1:
				for znaczek in self.char_range(a,l)
					stacyje.append(stacyjedict[znaczek])
				stacje = stacyje.tuple()
					
	def char_range(c1, c2):
		for c in xrange(ord(c1), ord(c2)+1):
			yield chr(c)
	def lng(self):
		return self.lang
