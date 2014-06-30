# -*- coding: utf-8 -*-
class multipokaz:
	"Ta klasa bedzie pokazywala wszystkie stacje w jednej linijce, w formie ludzkiej tabelki oraz w formie bardziej kompowej"
	import datetime
	from time import gmtime, strftime
	
	#def __init__(self,rowerdict,pracy,debugu,unix,dz,cz):
	def __init__(self,pracy,debugu,stacje):
		self.stacje = stacje
		self.debugu = debugu
		self.pracy = pracy
		
	def header(self):
		headdown = "_______________________"
		stacjetab = " "
		stacje = self.stacje
		for sh in stacje:
			if int(sh) == 0:
				#print "Error: station %s"(str(sh))
				#quit()
				st = "Sum| "
				ht = "_____"
			elif int(sh) < 10:
				st = str(sh) + "  | "
				ht = "_____"
			elif int(sh) < 13:
				st = str(sh) + " | "
				ht = "_____"
			else:
				print "Error: station %s"(str(sh))
				quit()
			stacjetab = stacjetab + st
			headdown = headdown + ht
#		print stacjetab
		print '| Czas:      Stacje-> |',(str(stacjetab)) # <- to jeszcze wróci, ale dla debugu testujemy na linię wyżej
	def stacprint(self,stacdict,unixtime):
#		if stacdict.keys() == stacje
#			self.pstacprint(stacdict,unixtime)
#		else:
		stacje = self.stacje
		ifcheck1 = []
		ifcheck2 = []
		for ifs in stacdict.keys():
			ifcheck1.append(int(ifs))
		for ifs2 in stacje:
			ifcheck2.append(int(ifs2))
		if ifcheck1 == ifcheck2:
			self.pstacprint(stacdict,unixtime)
		else:
			print "Error: ifcheck1 doesn't equal ifcheck2. Exiting. --multipokaz"
			quit()
		#datetime.format
		czasu = datetime.datetime()
		datum = czasu.fromtimestamp(unixtime)
		data = strftime("%Y-%m-%d %H:%M:%S", datua)
		print "| %s |%s"(str(data),rowerostring)
	def pstacprint(self,stacdict,unixtime):
		tsh = " "
		for s in stacdict.keys():
			ts = stacdict[s]
			its = int(ts)
			tts = self.ppstacprint(its,s)
	def morethansto(self,its,s):
		#while its > 100:
		#	its = its - 100
		#its = 
		if its > 999:
			while its > 1000:
				its = its - 1000
			tss = self.ppstacprint(its,s)
		elif its < 1000:
			if int(s) == 0:
				tss = str(its) + " | "
			else:
				tss = str(its) + "? "
		return tss
	def ppstacprint(self,its,s):
		if its < 0:
			its = its * -1
		if its < 0:
			if int(s) == 0:
				print "Error: bikes count %s on station SUM"(str(its))
			else:
				print "Error: bikes count %s on station %s"(str(its),str(s))
			quit()
		elif its < 10:
			if int(s) == 0:
				tss = str(its) + "   | "
			else:
				tss = str(its) + "  | "
		elif its < 20:
			if int(s) == 0:
				tss = str(its) + "  | "
			else:
				tss = str(its) + " | "
		elif its > 19:
			if its < 100:
				if int(s) == 0:
					tss = str(its) + "  | "
				else:
					tss = str(its) + "?| "
			elif its > 100:
				tss = self.morethansto(its,s)
		return tss
		
