from BitXor import *
class CRC(object):
	msgIni=[]
	dataBin=[]
	pGer=[]
	gGer=0
	def strToArray(self,msg,pG):
		self.lenMsg = len(msg)
		self.dataBin = self.gerLis(msg)
		self.pGer = self.gerLis(pG)
		self.gGer = len(self.pGer)-1
		return self.dataBin
	
	def gerLis(self, val):
		self.datLis=[]
		for l in val:
			self.datLis.append(int(l))
		return self.datLis

	def calcFcs(self):
		self.rB = self.rBits()
		self.mx=self.dataBin+self.rB
		return self.mx
	
	def rBits(self):
		self.rBi=[]
		for i in range(self.gGer):
			self.rBi.append(0)
		return self.rBi

	def opera(self, mx, pG):
		print pG
		self.mxPart=[]
		self.xr = BitXor()
		for self.i in mx:
			if self.mxPart < pG:
				self.mxPart.append(self.i)
				print self.mxPart
		return self.mxPart



		
