class ControlBit(object):
	control = []
	bits = {}
	
	def calBitsCont(self,msg, bitCont):
		self.control = msg
		self.lortnoc = self.control[len(self.control)::-1]
		self.bit = bitCont
		for self.j in self.bit:
			self.btF=[]
			self.btC=[]
			for self.i in range()
			self.btc=self.definBits(j,bitCont)
			if self.j in self.btc:
				self.bits[j] = self.btF
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
