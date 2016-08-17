#coding=UTF-8
class LoadFile(object):
	wordArray=[]
	
	def openFile(self, pathFile):
		self.data = []
		self.fileData = open(pathFile)
		for self.rowDt in self.fileData:
			self.row = self.rowDt.split(';')
			self.data.append(self.row)
		self.fileData.close()
		return self.data
