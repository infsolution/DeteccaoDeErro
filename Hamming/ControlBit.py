class ControlBit(object):
	control = []
	bits = {}
	
	def calBitsCont(self,msg, bitCont):
		self.control = msg
		self.bit = bitCont
		for self.j in self.bit:
			self.btF=[]
			self.btC=[]
			for self.i in range(1,len(self.control)+1):
				self.btC=self.definBits(self.i,self.bit)
				if self.j in self.btC:
					if self.i != self.j:
						self.btF.append(self.i)					
			self.bits[self.j] = self.btF
		return self.bits

	def definBits(self, posi, bitCont):
		self.bitsOk=[]
		self.bitVer=posi
		self.bitInver = bitCont[len(bitCont)::-1]
		i=0
		while(self.bitVer != 0):
			if self.bitVer >= self.bitInver[i]:
				self.bitVer = self.bitVer - self.bitInver[i]
				self.bitsOk.append(self.bitInver[i])
			i+=1
		return self.bitsOk

	def calcParity(self, bit, parity):
		self.parBit = 0
		if parity == 1:
			if bit % 2 == 0:
				self.parBit = 1
		elif parity == 0:
			if bit % 2 != 0:
				self.parBit = 1
		return self.parBit
	
	def calcParityBit(self, dic, parity, msg,parBit):
		self.parity=parity
		self.dicC = self.convertDic(dic,msg)
		self.parBitEnd=[]
		for self.j in parBit:
			self.bitC=0
			for self.i in self.dicC[self.j]:
				self.bitC=self.bitC+self.i
			self.parBitEnd.append(self.calcParity(self.bitC,parity))
		return self.parBitEnd

	def convertDic(self, dic, msg):
		self.rDic={}
		for i in dic:
			self.aux=[]
			for j in dic[i]:
				self.aux.append(msg[j-1])
			self.rDic[i]=self.aux
		return self.rDic




