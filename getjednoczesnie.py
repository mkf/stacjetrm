# -*- coding: utf-8 -*-
class getjednoczesnie:
	"To jest klasa pobierania jednoczesnego"
	from download import * 
#	import time
	from pars import *
import Queue
import threading

	def __init__(self,stacje,pracy,lang,jezadr,lanchar):
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
	def pobierzjedno(self, q, s):
		
