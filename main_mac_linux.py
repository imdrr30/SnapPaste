import os
import time
from os.path import expanduser
import shutil
import multiprocessing
from tkinter import *
import clipboard
import pyqrcode
import subprocess
import webbrowser
import validators
home = expanduser("~")
a=1
def showcon(addr):
    webbrowser.open("{}/web/index.html".format(addr),new=2)
def serve():
    os.system("php -S 0.0.0.0:1234")
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
            subprocess.run(["osascript", "-e", 'set the clipboard to (read (POSIX file "uploads/toClip.jpg") as JPEG picture)'])
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
        IPAddr = os.popen("ipconfig getifaddr en0").read()
        IPAddr = IPAddr[:-1]
        if IPAddr == '':
            IPAddr = os.popen("ipconfig getifaddr en1").read()
            IPAddr = IPAddr[:-1]
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
    #starts here
    IPAddr2=os.popen("ipconfig getifaddr en0").read()
    IPAddr2 = IPAddr2[:-1]
    if IPAddr2=='':
        IPAddr2 = os.popen("ipconfig getifaddr en1").read()
        IPAddr2 = IPAddr2[:-1]
    print(IPAddr2)
    multiprocessing.freeze_support()
    print("Do not close the Window.")
    print("Scan QRCode with Any QRCode scanning App.")
    p2=multiprocessing.Process(name='p2',target=trans)
    p3=multiprocessing.Process(name='p3',target=ntwrkmang)
    p2.start()
    p3.start()
    qr="http://"+str(IPAddr2)+":1234"
    print(qr)
    url = pyqrcode.create(qr)
    url.png('web/images/qr.png', scale=6)
    root = Tk()
    lab = Label(root,text="Serving at: {}".format(qr))
    lab.pack()
    p1 = PhotoImage(file='icon.png')
    root.iconphoto(False, p1)
    root.geometry('250x50')
    root['bg']='white'
    root.title("SnapPaste")
    def showcon1():
        showcon(qr)
    showcon(qr)
    button= Button(root,text="Show QRCode",command=showcon1)
    button.pack()
    root.mainloop()
    os.system("killall php")
    os.system("killall SnapPaste")
