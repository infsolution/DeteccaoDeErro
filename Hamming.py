from ControlBit import *
class Hamming(object):
	parityBits=[]
	dataBin=[]
	bits={}
	lenMsg=0
	def strToArray(self,msg):
		self.lenMsg = len(msg)
		for l in msg:
			self.dataBin.append(int(l))
		self.parityBit(self.lenMsg)
		return self.dataBin

	def parityBit(self,lm):
		self.parBit=1
		self.i=0
		while(self.lenMsg>=self.parBit):
			if self.parBit == 2**self.i:
				self.parityBits.append(self.parBit)
				self.i+=1
				self.lenMsg+=1
			self.parBit+=1
		print self.parityBits
