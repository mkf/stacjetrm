# -*- coding: utf-8 -*-
class apixena:
	"""To jest klasa analogiczna do pars.py, jednak biorąca dane z API Xena"""

	def __init__(self, st):
		self.st = st
		import json
		import urllib

		filetouse = urllib.urlopen("http://xenotium.pl/workshop/index.php/api/trm/stations/format/json")
		f = filetouse.read()
		data = json.loads(f)
		# print data['1']
		#print data[1]
		#for i in range(1,len(data)):
		#	print data[str(i)]
		rowery = 0  # not yet supported
		self.rowery = rowery

	def rowerry(self):
		return self.rowery