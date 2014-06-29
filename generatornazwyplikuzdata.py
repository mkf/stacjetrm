# -*- coding: utf-8 -*-
class generatornazwyplikuzdata:
	"To jest generator nazw plików dla celów dzielenia plików zapisu na wolumeny czasowe"

	import datetime
	import time
	
	def __init__(self):
		czasdatu = datetime.datetime()
		czescdatowa = str(time.time()) + "-" + "local" + str(czasdatu.now()) + "-" + "utc" + str(czasdatu.utcnow())
	def name(self, poczateknazwy):
		nazwa = str(poczateknazwy) + "-" + czescdatowa
		return nazwa
