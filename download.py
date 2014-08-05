# -*- coding: utf-8 -*-
class download:
	"Ta klasa będzie po prostu pobierać jeden plik jednej stacji i mówić czy succesful i z jakiego czasu pochodzi plik, ciekawe czy da się wsio w inicie"
	import urllib2
	import time
	
	def __init__(self,stacja,landictu):
		if stacja == 0:
			from suma import suma
			print landictu['sumallnotsupported']
			quit()
		elif stacja == 100:
			from suma import suma
			print landictu['sumchonotsupported']
			quit()
		elif stacja < 10:
			if stacja > 0:
				na = (r'00', str(stacja), r'TOR')
			elif stacja < 0:
				print "%s: %s" % landictu['badstacparam'],str(stacja)
				quit()
		elif stacja > 9:
			if stacja > 12:
				na = (r'0', str(stacja), r'TOR')
			else:
				print "%s: %s" % landictu['badstacparam'],str(stacja)
				quit()
		else:
			print "%s: %s" % landictu['badstacparam'],str(stacja)
			quit()
		stacn = "".join(na)
		urlt = (r'trm24.pl/panel-trm/', str(stacn), r'.jsp')
		url = "".join(urlt)
		#wejs = urllib2.urlopen(url)
		#we = wejs.read()
		self.url = url
		self.st = int(stacja)
		self.stacn = stacn
	def down(self):
		import urllib2
		import time
		wejs = urllib2.urlopen(self.url)
		czas = time.time()
		self.czas = czas
		we = wejs.read()
		self.we = we
		return we
	def row(self):
		from pars import pars
		par = pars(self.down(),self.stacn)
		rowery = par.rowerry()
		self.rouwer = rowery
		return rowery
	def cza(self):
		return self.czas			
	def raz(self):
		a = (self.row(), self.czas, self.st, self.stacn)
		return a