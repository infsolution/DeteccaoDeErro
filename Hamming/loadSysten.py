#coding=UTF-8
class LoadFile(object):
	wordArray=[]
	dic={}
	def openFile(self, pathFile):
		self.data = []
		self.fileData = open(pathFile)
		for self.rowDt in self.fileData:
			self.row = self.rowDt.split(';')
			self.data.append(self.row)
		self.fileData.close()
		return self.data
	def dicTerms(self, data):
		for self.dt in data:
			self.dic[self.dt[3].strip()]=self.dt[1].strip()
		return self.dic

	def decod(self, word, dic):
		self.wordArray=[]
		for self.w in word:
			self.wordArray.append(self.selVal(self.w,dic))
		return self.wordArray


	def selVal(self, val, dic):
		if val == ' ':
			return '00100000'
		return dic[val]

