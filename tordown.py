# -*- coding: utf-8 -*-
class tordown:
	"To jest klasa pobierania za pośrednictwem sieci Tor, bazowana na https://stem.torproject.org/tutorials/to_russia_with_love.html "
	
	def __init__(self, debugu):
		self.debugu = debugu
		if debugu == "y" or debugu == "f":
			debug = 1
		elif debugu == "n":
			debug = 0
		import StringIO
		import socket
		import urllib

		import socks  # SocksiPy module
		import stem.process

		from stem.util import term

		SOCKS_PORT = 7000

		# Set socks proxy and wrap the urllib module

		socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '127.0.0.1', SOCKS_PORT)
		socket.socket = socks.socksocket

		# Perform DNS resolution through the socket

		def getaddrinfo(*args):
			return [(socket.AF_INET, socket.SOCK_STREAM, 6, '', (args[0], args[1]))]

		socket.getaddrinfo = getaddrinfo





		# Start an instance of Tor configured to only exit through Russia. This prints
		# Tor's bootstrap information as it starts. Note that this likely will not
		# work if you have another Tor instance running.

		def print_bootstrap_lines(line):
			if "Bootstrapped " in line and self.debug == 1 :
				print term.format(line, term.Color.BLUE)


		if self.debug == 1:
				print term.format("Starting Tor:\n", term.Attr.BOLD)

		self.tor_process = stem.process.launch_tor_with_config(
														config = {
															   'SocksPort': str(SOCKS_PORT),
															   'ExitNodes': '{pl}',
															   'EntryNodes': '{pl}',
														},
														init_msg_handler = print_bootstrap_lines,
		)

	def pobierz(self, url):
		if self.debugu == 'f':
			print "pobieram"
			def query(self, url):
				"Uses urllib to fetch a site using SocksiPy for Tor over the SOCKS_PORT."
					try:
						return urllib.urlopen(url).read()
					except:
						return "Unable to reach %s" % url
			print term.format("\nChecking our endpoint:\n", term.Attr.BOLD)
			print term.format(query("https://www.atagar.com/echo.php"), term.Color.BLUE)
		return urllib.urlopen(url)

	
	def zabij(self):
		self.tor_process.kill()  # stops tor