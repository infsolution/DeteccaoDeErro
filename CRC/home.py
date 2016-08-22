from CRC import *
from BitXor import *
from Receptor import *
from loadSysten import *
crc = CRC()
data = LoadFile()
arrayF = data.openFile('textAscii')
dtDic = data.dicTerms(arrayF)
inMsg = raw_input('Digite a mensagem:\n')
decWord = data.decod(inMsg, dtDic)
pg = raw_input('informe o polinomio gerador\n')
crc.loadData(decWord, pg)
msg = crc.dataBin
pG = crc.pGer
fcs = crc.opera(msg,pG)
print ('saida no home'), fcs
fMsg = crc.fullMsg(crc.oriMsg,fcs,crc.pGer)
print ('msgFull'), fMsg
print ('origMsg'),crc.oriMsg
print ('dataBin'),crc.dataBin
ev=raw_input('Enviar mensagem - S\nGerar erro antes de enviar - E.\n').upper()
ms=crc.toSend(ev,fMsg)
rcp = Receptor()
print rcp.verif(ms,crc.pGer)
