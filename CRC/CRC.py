from BitXor import *
class CRC(object):
	dataBin=[]
	pGer=[]
	gGer=0
####################### gera msg######################################
	def loadData(self, msg, pG):
		self.dataBin = self.strToArray(msg)
		self.pGer = self.strToArray(pG)
		self.gGer = len(self.pGer)-1
		#self.dataBin = self.calcFcs()

	def strToArray(self,msg):
		self.data = self.gerLis(msg)
		return self.data
	
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
##############################Divisao####################################
	def opera(self, mx, pG):
		self.btX = BitXor()
		if len(mx)>=len(pG):
			self.sliceM = mx[len(pG)+1:]
			self.pXor = mx[:len(pG)]
			self.res = self.btX.divXor(self.pXor,pG)
			######
		else:
			return mx
		

	def rmValZer(self, recBit):
		self.cpRec=[]
		for self.i in range(len(recBit)):
			if recBit[self.i] == 1:
				self.cpRec = recBit[self.i:]
				return self.cpRec

#	def sliceM(self, msg, pos):
#		return msg[pos:]
	def joinM(self, rec, msg):
		return rec+msg





		
