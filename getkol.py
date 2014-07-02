# -*- coding: utf-8 -*-
class getkol:
	"To jest klasa pobierania kolejno bez odstępu czasowego"
	from download import *
#	import datetime
	import datetime
#	from download import *
		
	def __init__(self,stacje):
		sa = 0
		sw = 0
		stacdict = {}
		for s in stacje:
			a = self.si(s)
			if a[0] == 'a':
				sa = 1
			elif a[0] == 'w':
				sw = 1
			else:
				
				
	def si(self,s):
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
			download(int(s))
			a = download.raz()
			return a
		else:
			print "Malkorekta biciklstacio: %s" % str(s)
			quit()
#	def pobierz(self):
#		
#	def
