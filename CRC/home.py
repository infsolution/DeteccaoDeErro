from CRC import *
from BitXor import *
crc = CRC()
btXor = BitXor()
inMsg = raw_input('Digite a mensagem:\n')
pg = raw_input('informe o polinomio gerador\n')
crc.loadData(inMsg, pg)
msg = crc.dataBin
pG = crc.pGer
print ('saida no home'), crc.opera(msg,pG)
