from CRC import *
class Receptor(object):
	msgRcb=[]
	pGer=[]
	def verif(self, msg, pG):
		self.crc = CRC()
		self.fcs=self.crc.opera(msg,pG)
		if sum(self.fcs)==0:
			return 'Mensagem ok'
		else:
			return 'Mensagem com erro' 
