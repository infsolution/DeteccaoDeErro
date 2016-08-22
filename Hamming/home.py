#coding=UTF-8
import os
from loadSysten import *
from Hamming import *
from ControlBit import *
from EndMsg import *
from Receptor import *
data = LoadFile()
arrayF = data.openFile('textAscii')
dtDic = data.dicTerms(arrayF)
word = raw_input('digite a palavra:\n\n')
decWord = data.decod(word, dtDic)
par = input('Informe a paridade para controle de erro:\n0(Paridade par) - 1(Paridade impar):\n\n')
msg = EndMsg()
msg.loadMsg(decWord)
eMsg = msg.loadMsgOrigInEnd()
ct = ControlBit()
dicBit = ct.calBitsCont(eMsg, msg.parBit)
ax=ct.calcParityBit(dicBit,par, eMsg,msg.parBit)
print ('bits da fullMsg'),ax
fM = msg.fullMsg(ax,eMsg)
print ('Mensagem final '),fM
rc = Receptor()
ev=raw_input('Enviar mensagem - S\nGerar erro antes de enviar - E.\n').upper()
ms=msg.toSend(ev,fM)
print ms	
bt = rc.idtBitCont(ms,par)
print ('bits da Mensagem recebida'), bt
lpb=rc.loParBit()
print ('valores dos bits da Msg receiver'), lpb
bitRec = rc.dicBit()
print ('bits calculados '), bitRec
print rc.verifi(rc.parBitVal,bitRec,bt)
