class ControlBit(object):
	control = []
	bits = {}
	def controlBit(self, bit, lenWord, parBitCont):
		self.parityBit = bit
		self.control = parBitCont
		for self.i in range(lenWord):
			if self.i in parBitCont:
				pass
			else:
				if self.calBitsCont():
					self.bits.append(self.i)
		return self.bits
				

	def calBitsCont(self):
		self.lortnoc = self.control[len(self.control)::-1]
		self.bit=self.parityBit
		for self.i in self.lortnoc:
			if self.i < self.bit:
				self.bit = self.bit-self.i
			elif self.bit == self.i:
				return True
			else:
				return False
