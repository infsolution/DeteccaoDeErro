from CRC import *
from BitXor import *
msCrc = CRC()
btXor = BitXor()
inMsg = raw_input('Digite a mensagem:\n')
pg = raw_input('informe o polinomio gerador\n')
msg = msCrc.strToArray(inMsg, pg)
print btXor.divXor(msg,msCrc.pGer)
fcs = msCrc.calcFcs()
print msCrc.opera(fcs,msCrc.pGer)
