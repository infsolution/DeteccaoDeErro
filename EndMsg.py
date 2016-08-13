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
