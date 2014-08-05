# -*- coding: utf-8 -*-
class orzeczim:
	"To jest klasa orzeczenia imiennego i w ogole outputu standardowego dotycząca wyświetlania kolejnego"

	def __init__(self,row,stac,unx,pracy,lan,jezadr,lanchar):
		self.row = row
		self.stac = stac
		self.unx = unx
		self.lan = lan
		import datetime
		hejoczasuu = []
		for itt in datetime.datetime.fromtimestamp(unx).timetuple():
			hejoczasuu.append(itt)
		dzcz = datetime.datetime(hejoczasuu[0],hejoczasuu[1],hejoczasuu[2],hejoczasuu[3],hejoczasuu[4],hejoczasuu[5]).isoformat(' ')
		self.dzcz = dzcz
		jezyczek = lan.dictu()
		jezyu = lan
		self.jezyu = jezyu
		adrlocsafe = {
			'001TOR': 'Rynek Staromiejski', 
			'002TOR': 'Plac sw. Katarzyny', 
			'003TOR': 'Plac Rapackiego', 
			'004TOR': 'ul. Bulwar Filadelfijski - Brama Klasztorna', 
			'005TOR': 'ul. Szosa Chelminska - Targowisko Miejskie', 
			'006TOR': 'ul. Gagarina - Biblioteka Uniwersytecka', 
			'007TOR': 'ul. Broniewskiego - Tesco', 
			'008TOR': 'ul. Gen. Jozefa Hallera - Polo Market', 
			'009TOR': 'ul. Szosa Chelminska - Polo Market', 
			'010TOR': 'PKP Torun Glowny', 
			'011TOR': 'ul. Dziewulskiego - Komisariat Policji', 
			'012TOR': 'ul. Konstytucji 3 Maja - Pawilon Maciej'
		}
		adrlocnatio = {
			'001TOR': 'Rynek Staromiejski', 
			'002TOR': 'Plac św. Katarzyny', 
			'003TOR': 'Plac Rapackiego', 
			'004TOR': 'ul. Bulwar Filadelfijski - Brama Klasztorna', 
			'005TOR': 'ul. Szosa Chełmińska - Targowisko Miejskie', 
			'006TOR': 'ul. Gagarina - Biblioteka Uniwersytecka', 
			'007TOR': 'ul. Broniewskiego - Tesco', 
			'008TOR': 'ul. Gen. Józefa Hallera - Polo Market', 
			'009TOR': 'ul. Szosa Chełmińska - Polo Market', 
			'010TOR': 'PKP Toruń Główny', 
			'011TOR': 'ul. Dziewulskiego - Komisariat Policji', 
			'012TOR': 'ul. Konstytucji 3 Maja - Pawilon Maciej'
		}
		if jezadr == "c":
			ad = jezyu.lanstac()
		elif jezadr == 'l':
			if lanchar == 'n':
				ad = adrlocsafe
			elif lanchar == 'y':
				ad = adrlocnatio
			else:
				print "Gupi błondd"
				print lanchar
				quit()
		else:
			print "Gupppiii bwond"
			quit()
		self.ad = ad
	def orz(self):
		row = self.row
		self.wyd = self.jezyu.wyd(row)
		wyd = self.wyd

	def pisul(self):
		wyd = self.wyd
		dzcz = self.dzcz
		#dz = self.dz
		st = self.stac
		row = self.row
		print dzcz, ":", self.jezyu.dictu()['nastacji'], st, wyd

	def pisp(self):
		dzcz = self.dzcz
		#dz = self.dz
		st = self.stac
		row = self.row
		print dzcz, st, row

	def pisc(self):
		import re
		unx = self.unx
		st = self.stac
		stn = int(re.sub(r'\D',"",st))
		row = self.row
		print unx, stn, row
	def pism(self):
		unx = self.unx
		st = self.stac
		row = self.row
		print unx, st, row
	def pisfa(self):
		wyd = self.wyd
		dzcz = self.dzcz
		#dz = self.dz
		st = self.stac
		ad = self.ad
		print dzcz, ":", self.jezyu.dictu()['nastacji'], st, wyd, " - ", ad[st]
	def pist(self):
		dzcz = self.dzcz
        #dz = self.dz
		st = self.stac
		row = self.row
		ad = self.ad
		dl = len(ad[st])
		ds = 43 - dl
#		print ds
#		sp = spacje(ds)
                spac = " "
                for i in range(ds):
                        spac = spac + ' '
#		s = " "
#		sp = s * ds
		sp = spac
#		for sp in range (0, ds):
#			s = s + " "
		if row <= 9:
			print "|",dzcz,"|",st,"|",row,"  | ",ad[st],sp,"|"
		elif row >= 10:
			print "|",dzcz,"|",st,"|",row," | ",ad[st],sp,"|"
