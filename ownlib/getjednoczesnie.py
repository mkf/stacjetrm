# -*- coding: utf-8 -*-
class getjednoczesnie:
	"""To jest klasa pobierania jednoczesnego"""
	# import time

	def __init__(self, stacje, pracy, debugu, lan, jezadr, lanchar, iwri, idis):
		import Queue, threading
		self.lan=lan;self.jezadr=jezadr;self.lanchar=lanchar;ssa=0;ssw=0;stacdict={};slownikczasow=();q=Queue.Queue();self.pracy=pracy
		def kolejka(q, s, iwri, idis): q.put(self.si(s, iwri, idis))
		for s in stacje:
			sa = 0 ; sw = 0 ; a = self.si(s, iwri, idis) ; assert a is not None, "Cannot be None"  #; print a  #debug
			if a[0] == 'a': sa = 1 ; ssa = 1
			elif a[0] == 'w': sw = 1 ; ssw = 1
			else: t = threading.Thread(target=kolejka, args=(q, s, iwri, idis)) ; t.daemon = True ; t.start()
	def si(self, s, iwri, idis):
		lan = self.lan ; sa = 0 ; sw = 0
		assert int(s) ==0 or int(s)==100 or int(s)<0 or int(s)<=13, "%s: %s" % (lan.dictu['badstacparam'],str(s))
		if int(s) == 0: sa = 1 ; a = 'a' ; return a
		elif int(s) == 100: sw = 1 ; a = 'w' ; return a
		elif int(s) < 0: o = int(s) * (-1) ; a = self.si(o, iwri, idis) ; return a
		elif int(s) <= 13:
			from ownlib.download import download
			a = download(int(s), lan.dictu).raz()
			if iwri == 1: print "instawrite"
			if idis == 1: self.praca(int(s), int(a[0]), int(a[1]), self.pracy) ; return a
	def praca(self, st, row, utim, pr):
		lan = self.lan ; jezadr = self.jezadr ; lanchar = self.lanchar ; from ownlib.pokaz import pokaz
		if pr == 'n': pracowanie = 'nie'
		else: pokaz(row, st, utim, pr, lan, jezadr, lanchar)
	def razpraca(self, stli, rowslo, pr, debugu):
		lan = self.lan ; lanchar = self.lanchar # ; jezadr = self.jezadr
		from ownlib.multipokaz import multipokaz
		if pr == 'n': pracowanie = 'nie'
		else: multipokaz(stli, pr, debugu, rowslo, lan, lanchar)
	def razwrajt(self, stli, rowslo, utim, pr): pass
	def kolwrajt(self, st, row, utim, pr): pass
	def wrajt(self, st, row, utim, pr): pass
	def slowstac(self): return self.stacdict
	def slowczas(self): return self.slwcza
# http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies
