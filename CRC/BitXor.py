from operator import *
class BitXor(object):
	bitDiv=[]
	bitQuo=[]
	bitRes=[]
	def divXor(self,msgPart, pGer):
		if len(msgPart)==len(pGer):
			for i in range(len(pGer)):
				self.bitRes.append(xor(msgPart[i], pGer[i]))
		return self.bitRes
