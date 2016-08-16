#coding=UTF-8
import os
from loadSysten import *
from Hamming import *
from ControlBit import *
from EndMsg import *
from Receptor import *
data = LoadFile()
arrayF = data.openFile('ascii.csv')
word = raw_input('digite a palavra:\n\n')
par = input('Informe a paridade para controle de erro:\n0(Paridade par) - 1(Paridade impar):\n\n')
msg = EndMsg()
msg.loadMsg(word)
eMsg = msg.loadMsgOrigInEnd()
#print eMsg
ct = ControlBit()
dicBit = ct.calBitsCont(eMsg, msg.parBit)
ax=ct.calcParityBit(dicBit,par, eMsg,msg.parBit)
print ('bits da fullMsg'),ax
fM = msg.fullMsg(ax,eMsg)
print ('Mensagem final '),fM
rc = Receptor()
errM=[1,1,1,1,1,0,1,0,0,0,1,0,1,0,1,1,1,0,1,1,0,1]
print ('bits da Mensagem recebida'),rc.idtBitCont(errM,par)
bitRec = rc.dicBit()
print ('bits calculados '), bitRec
if ax == bitRec:
	print 'Mensagem ok'
else:
	print 'mensagem com erro'
