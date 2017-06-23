#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import os
serverName = 'localhost'
serverPort = 3600

while True:
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = input("Calculadora SOMA OU RAIZ\n Insira a <operacao> <numero> <numero2> PARA SAIR DIGITE 'sair'\n INICIE A OPERAÇÃO: ")
    if message.upper() == 'SAIR':
        os.system('clear')
        byte_msg = message.encode('utf-8')
        clientSocket.sendto(byte_msg, (serverName, serverPort))
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        print(modifiedMessage.decode('utf-8'))
        clientSocket.close()
    else:
        os.system('clear')
        byte_msg = message.encode('utf-8')
        clientSocket.sendto(byte_msg, (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    #print(result)
    print(modifiedMessage.decode('utf-8'))
    