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
			
		return self.parBit
	
	def loParBit(self):
		for self.j in self.parBit:
			self.parBitVal.append(self.recMsg[self.j-1])
		return self.parBitVal

	def dicBit(self):
		self.dicBitPar=self.cBit.calBitsCont(self.recMsg, self.parBit)
		self.cBitRec = self.cBit.calcParityBit(self.dicBitPar,self.parity,self.recMsg,self.parBit)
		return self.cBitRec			

	def calcErro(self, recBit, calcBit, posBit):
		self.bit=0
		for self.i in range(len(recBit)):
			if recBit[self.i] != calcBit[self.i]:
				self.bit = self.bit + posBit[self.i]
				
		return self.bit

	def verifi(self, bitRec, bitCalc,posBit):
		if bitRec == bitCalc:
			return 'Mensagem recebida sem erros.'
		else:
			self.bitErr = self.calcErro(bitRec, bitCalc, posBit)
			return "Mensagem com erro no bit ",self.bitErr 



