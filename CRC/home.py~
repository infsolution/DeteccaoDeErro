from CRC import *
from BitXor import *
from Receptor import *
crc = CRC()
#btXor = BitXor()
inMsg = raw_input('Digite a mensagem:\n')
pg = raw_input('informe o polinomio gerador\n')
crc.loadData(inMsg, pg)
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
