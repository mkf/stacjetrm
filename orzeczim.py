# -*- coding: utf-8 -*-
class orzeczim:
	"To jest klasa orzeczenia imiennego i w ogole outputu standardowego dotycząca wyświetlania kolejnego"

	def __init__(self,row,stac,unx,pracy,lang,jezadr,lanchar):
		self.row = row
		self.stac = stac
		self.unx = unx
		self.lang = lang
		import datetime
		#zrobmy dawne dz i cz z unixtime w tym miejscu
		if lang == "en":
			from english import *
			lan = english()
		elif lang == "eo":
			if lanchar == 'y':
				from esperanto import eo_natio
				lan = eo_natio()
			if lanchar == 'n':
				from esperanto import eo_safe
				lan = eo_safe()
		elif lang == "pl":
			if lanchar == 'y':
				from polski import pl_natio
				lan = pl_natio()
			if lanchar == 'n':
				from polski import pl_safe
				lan = pl_safe()
		elif lang == "de":
			if lanchar == 'y':
				from deutsch import de_natio
				lan = de_natio()
			if lanchar == 'n':
				from deutsch import de_safe
				lan = de_safe()
		else:
			print "An error occured: no such language possible as %s" % lang
			quit()
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
			if lanchar == 'e':
				ad = adrlocsafe
			elif lanchar == 'l':
				ad = adrlocnatio
			else:
				print "Gupi błondd"
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
		cz = self.cz
		dz = self.dz
		st = self.stac
		row = self.row
		print dz, cz, self.jezyu.dictu[nastacji], st, wyd

	def pisp(self):
		cz = self.cz
		dz = self.dz
		st = self.stac
		row = self.row
		print dz, cz, st, row

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
	def pisa(self):
		wyd = self.wyd
		cz = self.cz
		dz = self.dz
		st = self.stac
		ad = self.ad
		print dz, cz, self.jezyu.dictu[nastacji], st, wyd, " - ", ad[st]
	def pist(self):
		cz = self.cz
                dz = self.dz
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
			print "|",dz,cz,"|",st,"|",row,"  | ",ad[st],sp,"|"
		elif row >= 10:
			print "|",dz,cz,"|",st,"|",row," | ",ad[st],sp,"|"
