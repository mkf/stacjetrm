class apixena:
	"To jest klasa analogiczna do pars.py, jednak bioraca dane z API Xena"
	
	def __init__(self,st):
		self.st = st
		import sys
		import re
		import json
		import urllib
		file = urllib.urlopen("http://xenotium.pl/workshop/index.php/api/trm/stations/format/json")
		f = file.read()
		data = json.loads(f)
		#print data['1']
		#print data[1]
		#for i in range(1,len(data)):
		#	print data[str(i)]
		rowery = 
		self.rowery = rowery
		
	def rowerry(self):
		return self.rowery
