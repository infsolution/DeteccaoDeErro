from operator import *
class CRC(object):
	msgIni=[]
	dataBin=[]
	pGer=[]
	gGer=0
	def strToArray(self,msg,pG):
		self.pGer = pG
		self.gGer = len(self.pGer)-1
		self.lenMsg = len(msg)
		self.dataBin = self.gerLis(msg)
		self.pGer = self.gerLis(pG)
		return self.dataBin
	
	def gerLis(self, val):
		self.datLis=[]
		for l in val:
			self.datLis.append(int(l))
		return self.datLis
