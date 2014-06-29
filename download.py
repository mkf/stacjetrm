# -*- coding: utf-8 -*-
class download:
	"Ta klasa będzie po prostu pobierać jeden plik jednej stacji i mówić czy succesful i z jakiego czasu pochodzi plik, ciekawe czy da się wsio w inicie"
	import urllib2
	import time
	
	def __init__(self,stacja):
		
