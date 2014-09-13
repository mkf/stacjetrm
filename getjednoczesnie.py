# -*- coding: utf-8 -*-
class getjednoczesnie:
	"To jest klasa pobierania jednoczesnego"
	from download import * 
#	import time
	from pars import *
import Queue
import threading

	def __init__(self,stacje,pracy,lan,jezadr,lanchar):
		self.lan = lan
		self.jezadr = jezadr
		self.lanchar = lanchar
		sa = 0
		ssa = 0
		sw = 0
		ssw = 0
		stacdict = {}
		slownikczasow = ()
		q = Queue.Queue()
		for s in stacje:
			sa = 0
			sw = 0
			a = 
			t = threading.Thread(target=self.pobierzjedno, agrs = (q,s))
			t.daemon=True
			t.start()
	

	def suma(self

	def si(self,s):
		lan = self.lan
		sa = 0
		sw = 0
		if int(s) == 0:
			sa = 1
			a = 'a'
			return a
		elif int(s) == 100:
			sw = 1
			a = 'w'
			return a
		elif int(s) < 0:
			o = int(s) * (-1)
			a = self.si(o)
			return a
		elif int(s) < 13:
			from download import download
			thisisthedownloadinstance = download(int(s),lan.dictu())
			a = thisisthedownloadinstance.raz()
			return a
		else:
			jezodict = lan.dictu()
			print "%s: %s" % jezodict[badstacparam],str(s)
			quit()			
			
	def praca(self,st,row,utim,pr):
		lan = self.lan
		jezadr = self.jezadr
		lanchar = self.lanchar
		from pokaz import pokaz
		if pr == 'n':
			pracowanie='nie'
#		elif pr == 'f' or pr == 'l' or pr == 'u' or pr == 'a' or pr == 't' or pr == 'k' or pr == 'c' or pr == 'm':
		else:
			pokaz(row,st,utim,pr,lan,jezadr,lanchar)
	def slowstac(self):
		return self.stacdict
	def slowczas(self):
		return self.slwcza
# http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies
