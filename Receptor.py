from ControlBit import *
class Receptor(object):
	recMsg=[]
	dicBitPar={}
	parBit=[]
	parBitVal=[]
	parity=0
	cBit = ControlBit()

	def idtBitCont(self, msg,par):
		self.parity=par
		self.recMsg=msg
		self.exp=0
		for self.i in range(1,len(self.recMsg)+1):
			if self.i == 2**self.exp:
				self.bitPos = 2**self.exp
				self.parBit.append(self.bitPos)
				self.exp+=1
		#print ('posicoes'),self.parBit		
		return self.parBit
	
	def dicBit(self):
		self.dicBitPar=self.cBit.calBitsCont(self.recMsg, self.parBit)
		self.cBitRec = self.cBit.calcParityBit(self.dicBitPar,self.parity,self.recMsg,self.parBit)
		return self.cBitRec			
