# -*- coding: utf-8 -*-
class generatornazwyplikuzdata:
	"To jest generator nazw plików dla celów dzielenia plików zapisu na wolumeny czasowe"

	def __init__(self):
		import datetime
		import time
		czasdatu = datetime.datetime()
		self.czescdatowa = str(time.time()) + "-" + "local" + str(czasdatu.now()) + "-" + "utc" + str(czasdatu.utcnow())

	@staticmethod
	def name(poczateknazwy):
		nazwa = str(poczateknazwy) + "-" + self.czescdatowa
		return nazwa
