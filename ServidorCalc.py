#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
from math import sqrt

def calcSoma(a, b):
    c = float(a) + float(b)
    return str(c)

def calcRaiz(a):
    return str(sqrt(float(a)))

def operCalc(operacao):
    lOperacao = operacao.decode('utf-8').split(' ')
#    print(modifiedMessage.decode('utf-8'))
    print(lOperacao[0])
    if lOperacao[0].upper() == 'SOMA':
        if lOperacao[1].isnumeric() and lOperacao[2].isnumeric():
            return calcSoma(lOperacao[1], lOperacao[2])
        else:
            sErro = 'Os valores passados não são numéricos.\n'
            return sErro
    elif lOperacao[0].upper() == 'RAIZ':
        if lOperacao[1].isnumeric():
            return calcRaiz(lOperacao[1])
        else:
            sErro = 'Os valores passados não são numéricos.\n'
            return sErro
    
    elif lOperacao[0].upper() == 'SAIR':
        sErro = 'FIM DA OPERAÇÕES\n'
        return sErro
        print('\n FIM DA CONEXÃO:  ', clientAddress)
    else:
        sErro = 'A operação passada não é válida.\n'
        return sErro
        

serverHost = 'localhost'
serverPort = 3600

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind((serverHost, serverPort))

print("Servidor Iniciado.\n")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    print('Conexão iniciada por: ', clientAddress)
    result = operCalc(message)
    print("\n", result)
    serverSocket.sendto(result.encode(), clientAddress)
