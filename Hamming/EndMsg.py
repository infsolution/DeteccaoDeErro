from ControlBit import *
from Hamming import *
class EndMsg(object):
	endMsg=[]
	parBit=[]

	def loadMsg(self,word):
		dataBin = Hamming()
		self.dtB = dataBin.strToArray(word)
		self.parBit=dataBin.parityBits
		self.lenEndMsg = len(self.dtB)+len(self.parBit)
		for j in range(self.lenEndMsg):
			self.endMsg.append(0)
		return self.endMsg

	def loadMsgOrigInEnd(self):
		ps=1
		ps1=0
		exp=0
		for i in range(len(self.endMsg)):
			if ps == 2**exp:
				pass
				exp+=1
			else:
				self.endMsg[i]=self.dtB[ps1]
				ps1+=1
			ps+=1
		return self.endMsg
	def fullMsg(self, parBit,msg):
		self.fMsg=msg
		self.ps =1
		self.ps1=0
		self.exp=0
		for self.i in range(len(self.fMsg)):
			if self.ps == 2**self.exp:
				self.fMsg[self.i]=parBit[self.ps1]
				self.ps1+=1
				self.exp+=1
			self.ps+=1
		return self.fMsg

	def toSend(self,answer,msg):
		if answer == 'S':
			return msg
		elif answer == 'E':
			er=input('Informe o bit onde sera gerado o erro!\n')
			return self.errGen(msg,er)
		else:
			return 'Valor invalido!'

	def errGen(self, msg, eBit):
		msg[eBit-1] = self.valBit(msg[eBit-1])
		return msg
			
	def valBit(self, bit):
		if bit == 0:
			return 1
		if bit == 1:
			return 0



