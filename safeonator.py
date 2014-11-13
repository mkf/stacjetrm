# -*- coding: utf-8 -*-
class safeonator:
	"To jest klasa konwertująca znaczki natio na znaczki bezpieczne."
	self.pltoang_tab = {u'ą': 'a', u'ć': 'c', u'ę': 'e', u'ł': 'l', u'ń': 'n', u'ó': 'o', u'ś': 's', u'ż': 'z', u'ź': 'z'}

	def __init__(self):
		pass

	def zwroc(self, text):
		return ''.join(self.pltoang_tab.get(char, char) for char in text)
