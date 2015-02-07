# coding=utf-8
class writekolczyraz:
	def __init__(self,parmetry):
		try:
			if len(
				parmetry.writetocsvkolsinglefile + \
					parmetry.writetocsvkolmultiwaitbetweenloopsvolumefile + parmetry.writetocsvkolmulticountvolumefile) > 0:
				writekolczyraz = 'k'
			elif len(
				parmetry.writetocsvrazsinglefile + \
					parmetry.writetocsvrazmultiwaitbetweenloopsvolumefile + parmetry.writetocsvrazmulticountvolumefile) > 0:
				writekolczyraz = 'r'
			elif parmetry.writeno: writekolczyraz = 'n'
			else: writekolczyraz = 'n'
		except:
			try:
				if len(
					parmetry.writetocsvrazsinglefile + \
						parmetry.writetocsvrazmultiwaitbetweenloopsvolumefile + parmetry.writetocsvrazmulticountvolumefile) > 0:
					writekolczyraz = 'r'
				elif parmetry.writeno: writekolczyraz = 'n'
				else: writekolczyraz = 'n'
			except:
				if parmetry.writeno: writekolczyraz = 'n'
				else: writekolczyraz = 'n'
		self.writekolczyraz = writekolczyraz
	#def writekolczyraz(self):
	#	return self.writekolczyraz
