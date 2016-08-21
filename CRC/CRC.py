from BitXor import *
class CRC(object):
	dataBin=[]
	pGer=[]
	gGer=0
####################### gera msg######################################
	def loadData(self, msg, pG):
		self.dataBin = self.strToArray(msg)
		self.oriMsg=self.strToArray(msg)
		self.pGer = self.strToArray(pG)
		self.gGer = len(self.pGer)-1
		self.dataBin = self.calcFcs()

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
			self.res=[]
			self.sliceM = mx[len(pG):]
			#print ('msg fatiada '),self.sliceM
			self.pXor = mx[:len(pG)]
			#print ('parte para divisao'),self.pXor
			self.res = self.btX.divXor(self.pXor,pG)
			self.res = self.rmValZer(self.res)
			#print ('resto sem zeros'), self.res
			self.fcs = self.joinM(self.res,self.sliceM)
			#print ('msg da recursao'),self.fcs
			return self.opera(self.fcs,pG)
		else:
			return mx
		

	def rmValZer(self, recBit):
		self.cpRec=[]
		for self.i in range(len(recBit)):
			if recBit[self.i] == 1:
				self.cpRec = recBit[self.i:]
				return self.cpRec

	def joinM(self, rec, msg):
		if rec == None:
			if self.retMesZer(msg) == 0:
				return msg
			return self.rmValZer(msg)
		else:
			return rec+msg
	
	def retMesZer(self, msg):
		self.lenMsg=0		
		for i in msg:
			self.lenMsg=self.lenMsg+i
		return self.lenMsg
	
	def fullMsg(self, msg, fcs, pG):
		self.somZer=[]
		self.lenM = len(pG)-1
		if len(fcs)<len(pG):
			self.dif=len(pG)-len(fcs)-1
			for i in range(self.dif):
				self.somZer.append(0)
		return msg+self.somZer+fcs

	
