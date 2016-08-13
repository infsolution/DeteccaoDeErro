#coding=UTF-8
import os
from loadSysten import *
from Hamming import *
from ControlBit import *
from EndMsg import *
data = LoadFile()
arrayF = data.openFile('ascii.csv')
word = raw_input('digite a palavra: ')
#dataBin = Hamming()
#dtB = dataBin.strToArray(word)
#print dtB
#print dataBin.lenMsg
#print dataBin.parityBits
msg = EndMsg()
print msg.loadMsg(word)

