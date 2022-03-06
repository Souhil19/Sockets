#!/usr/bin/env python

import socket  # from tkinter import Tk for Python 3.x
from tkinter import *

TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

with open('Recived/received_file', 'wb') as f:
    print ('file opened')
    while True:
        print('receive data...')
        data = s.recv(BUFFER_SIZE)
        print('data=%s', data)
        if not data:
            f.close()
            print ('file close()')
            break
        """Ecrire"""
        f.write(data)

print('Successfully Download')
s.close()
print('connection terminé')