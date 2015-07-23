# -*- coding: utf-8 -*-
class zapis:
	"""To jest klasa sluzaca do zapisu m.in. do csv, ale chyba do baz danych tez"""

	def __init__(self, gdzie, row, stac, unx, dz, cz):
		#self.gdzie = gdzie
		self.row = row
		self.stac = stac
		self.unx = unx
		self.dz = dz
		self.cz = cz
		ad = {
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
			'012TOR': 'ul. Konstytucji 3 Maja - Pawilon Maciej',
			'013TOR': 'ul. Dabrowskiego - Dworzec autobusowy',
                        '014TOR': 'ul. Waly gen. Sikorskiego - Urzad Miasta',
                        '015TOR': 'ul. Gen. Jozefa Bema - Tor-Tor',
                        '016TOR': 'ul. Przysiecka - Barbarka',
                        '017TOR': 'ul. Bazynskich - basen',
                        '018TOR': 'PKP Torun Wschodni',
                        '019TOR': 'ul. Kosciuszki / ul. Swietopelka',
                        '020TOR': 'ul. Mickiewicza / ul. Tujakowskiego',
                        '021TOR': 'ul. Gagarina - Od Nowa',
                        '022TOR': 'ul. Rydygiera / ul. Donimirskiego',
                        '023TOR': 'ul. Kolankowskiego / ul. Kosynierow',
                        '024TOR': 'ul. Sw. Klemensa / ul. Sw. Jozefa',
                        '025TOR': 'ul. Legionow - Rondo Czadcy',
                        '026TOR': 'ul. Zolkiewskiego - Atrium Copernicus'
		}
		self.ad = ad
		self.stac = stac
