# -*- coding: utf-8 -*-
class download:
	"""Ta klasa będzie po prostu pobierać jeden plik jednej stacji i mówić czy succesful
	i z jakiego czasu pochodzi plik, ciekawe czy da się wsio w inicie"""

	def __init__(self, stacja, landictu,tor,tordown):
		self.landictu = landictu ; self.tor=tor;self.tordown=tordown
		if stacja == 0:

			print landictu['sumallnotsupported']
			quit()
		elif stacja == 100:

			print landictu['sumchonotsupported']
			quit()
		elif stacja < 10:
			if stacja > 0:
				na = (r'00', str(stacja), r'TOR')
			elif stacja < 0:
				print "in_elif: %s: %s" % (landictu['badstacparam'], str(stacja))
				quit()
		elif stacja > 9:
			if stacja <= 26:
				na = (r'0', str(stacja), r'TOR')
			else:
				print "in_else_min: %s: %s" % (landictu['badstacparam'], str(stacja))
				quit()
		else:
			print "in_else_max: %s: %s" % (landictu['badstacparam'], str(stacja))
			quit()
		stacn = "".join(na)
		urlt = (r'http://trm24.pl/panel-trm/', str(stacn), r'.jsp')
		url = "".join(urlt)
		# wejs = urllib2.urlopen(url)
		# we = wejs.read()
		self.url = url
		self.st = int(stacja)
		self.stacn = stacn

	def down(self):
		import urllib2
		import time

		try:
			if self.tor==0:
				wejs = urllib2.urlopen(self.url)
				czas = time.time()
				self.czas = czas
				we = wejs.read()
				self.we = we
			elif self.tor==1:
				wejs = self.tordown.pobierz(self.url)
				czas = time.time()
				self.czas = czas
				we = wejs.read()
				self.we = we
			return we
		except:
			czas = time.time()
			self.czas = czas
			we = "Download failed"
			self.we = we
			return we

	def row(self):
		from ownlib.pars import pars

		par = pars(self.down(), self.stacn, self.landictu)
		rowery = par.rowerry()
		self.rouwer = rowery
		return rowery

	def cza(self):
		return self.czas

	def raz(self):
		a = (self.row(), self.czas, self.st, self.stacn)
		return a
