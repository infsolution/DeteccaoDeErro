from ControlBit import *
from Hamming import *
class EndMsg(object):
	endMsg=[]
	parBit=[]

	def loadMsg(self,word):
		#ctb = ControlBit()
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

		
