#coding=UTF-8
import os
from loadSysten import *
from Hamming import *
from ControlBit import *
from EndMsg import *
data = LoadFile()
arrayF = data.openFile('ascii.csv')
word = raw_input('digite a palavra:\n\n')
par = input('Informe a paridade para controle de erro:\n0(Paridade par) - 1(Paridade impar):\n\n')
#dataBin = Hamming()
#dtB = dataBin.strToArray(word)
#print dtB
#print dataBin.lenMsg
#print dataBin.parityBits
msg = EndMsg()
msg.loadMsg(word)
eMsg = msg.loadMsgOrigInEnd()
print eMsg
ct = ControlBit()
dicBit = ct.calBitsCont(eMsg, msg.parBit)
#pt =ct.loadParityBit(msg.parBit,dicBit,par)
#print ('bits de paridade final'), pt
ax=ct.calcParityBit(dicBit,par, eMsg,msg.parBit)
print ax
fM = msg.fullMsg(ax,eMsg)
print ('Mensagem final '),fM
