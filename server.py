#!/usr/bin/env python
import socket
from threading import Thread
import tkinter as tk
from tkinter import filedialog
from tkinter import *
from PIL import ImageTk,Image
from tkinter import ttk



TCP_IP = 'localhost'
TCP_PORT = 9001
BUFFER_SIZE = 1024

def chooseFile():
    root = tk.Tk()
    root.withdraw()

    filename = filedialog.askopenfilename()
    return filename






class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for " + ip + ":" + str(port))

    def run(self):

        root = tk.Tk()
        root.iconbitmap('send.jpg')
        root.title('Files Transfer')
        my_img = ImageTk.PhotoImage(Image.open("send.jpg"))
        my_label = Label(image=my_img)
        my_label.pack()
        myButton = Button(root, text="Choose a file", command=chooseFile)
        myButton.place(anchor=CENTER)
        myButton.pack()

        my_progress = ttk.Progressbar(root, orient=HORIZONTAL, len=300, mode='determinate')
        my_progress.pack()

        root.geometry("400x250")

        root.eval('tk::PlaceWindow . center')

        """filename='IngeHack.jpg'"""
        f = open(chooseFile(), 'rb')

        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)
                print('Sending .... ', repr(l))
                l = f.read(BUFFER_SIZE)
                root.update_idletasks()

            if not l:
                f.close()
                self.sock.close()
                break


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for clients connections !!!")
    (conn, (ip, port)) = tcpsock.accept()
    print('Got client connection :', (ip, port))
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    root.mainloop()
    threads.append(newthread)


for t in threads:
    t.join()

