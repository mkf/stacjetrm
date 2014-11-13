# -*- coding: utf-8 -*-
class safeonator:
	"""To jest klasa konwertująca znaczki natio na znaczki bezpieczne."""

	def __init__(self):
		self.pltoang_tab = {u'ą': 'a', u'ć': 'c', u'ę': 'e', u'ł': 'l', u'ń': 'n', u'ó': 'o', u'ś': 's', u'ż': 'z', u'ź': 'z'}

	def zwroc(self, text):
		return ''.join(self.pltoang_tab.get(char, char) for char in text)
