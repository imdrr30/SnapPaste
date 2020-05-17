import os
import time
import socket
from os.path import expanduser
import shutil
import multiprocessing
from tkinter import *
import clipboard
import pyqrcode
import webbrowser
import validators
from PIL import ImageTk, Image
home = expanduser("~")
a=1
def serve():
    os.system("php -S 0.0.0.0:1111")
def trans():
    while True:
        try:
            clipclr = open("Clipboards/clipcl.txt","r")
            try:
                a=clipclr.read()
                if validators.url(a):
                    webbrowser.open(a,new=2)
                clipboard.copy(a)
            except TypeError:
                a=1
            clipclr.close()
            os.remove("Clipboards/clipcl.txt")
        except FileNotFoundError:
            a=0
        f1 = open("Clipboards/clippc.txt","r")
        if clipboard.paste()!=f1.read():
            f2 = open(r"Clipboards/clippc.txt", "w+")
            f2.write(clipboard.paste())
            f2.close()
        if os.path.isfile("uploads/toClip.jpg"):
            os.system("clip.exe clipboard copyimage uploads/toClip.jpg")
            os.remove("uploads/toClip.jpg")
        files = os.listdir("uploads/")
        if files!=[]:
            for f in files:
                try:
                    shutil.move("uploads/"+f,home+"/Desktop/")
                except shutil.Error:
                    continue
        time.sleep(1)

def ntwrkmang():
    global sett,previp,printed,rset,previp,p1
    previp='127.0.0.1'
    sett=1
    printed=1
    p1 = multiprocessing.Process(name='p1', target=serve)
    while True:
        hostname = socket.gethostname()
        IPAddr = socket.gethostbyname(hostname)
        if str(IPAddr)!=previp:
            printed=1
            previp=str(IPAddr)
        if str(IPAddr)=='127.0.0.1':
            msg = "Waiting for network, You havent made any connections yet...."
            if printed==1:
                print(msg)
                printed=0
            sett=1
            if sett!=1:
                p1.terminate()
        else:
            if sett==1:
                msg = "Connected to Network... Enter {}:1111 in any connected device's browser to start using the service".format(IPAddr)
                print(msg)
                p1.start()
                previp=IPAddr
                sett=0
                printed=0
        time.sleep(1)




if __name__ == '__main__':
    hostname = socket.gethostname()
    IPAddr2 = socket.gethostbyname(hostname)
    multiprocessing.freeze_support()
    print("Do not close the Window.")
    print("Scan QRCode with Any QRCode scanning App.")
    p2=multiprocessing.Process(name='p2',target=trans)
    p3=multiprocessing.Process(name='p3',target=ntwrkmang)
    p2.start()
    p3.start()
    qr="http://"+IPAddr2+":1111"
    url = pyqrcode.create(qr)
    url.png('myqrcode.png', scale=6)
    root = Tk()
    root.iconbitmap("icon.ico")
    root.geometry('300x500')
    root['bg']='purple'
    root.title("SnapPaste")
    label = Label(root, text=IPAddr2+":1111",fg="yellow",bg="purple",font=("Monova", 20))
    label.pack(expand="yes")
    img = ImageTk.PhotoImage(Image.open("myqrcode.png"))
    panel = Label(root, image=img)
    panel.pack(side="bottom", expand="yes")
    root.mainloop()
    os.system("taskkill /F /IM php.exe")
    os.system("taskkill /F /IM SnapPaste.exe")
