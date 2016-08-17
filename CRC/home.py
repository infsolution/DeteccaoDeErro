from CRC import *
msCrc = CRC()
inMsg = raw_input('Digite a mensagem:\n')
pg = raw_input('informe o polinomio gerador\n')
print msCrc.strToArray(inMsg, pg)
