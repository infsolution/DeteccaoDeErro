from CRC import *
from BitXor import *
crc = CRC()
btXor = BitXor()
inMsg = raw_input('Digite a mensagem:\n')
pg = raw_input('informe o polinomio gerador\n')
crc.loadData(inMsg, pg)
msg = crc.dataBin
pG = crc.pGer
fcs = crc.opera(msg,pG)
print ('saida no home'), fcs
print ('msgFull'), crc.fullMsg(crc.oriMsg,fcs,crc.pGer)
print ('origMsg'),crc.oriMsg
print ('dataBin'),crc.dataBin
