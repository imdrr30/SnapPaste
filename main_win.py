import os
import time
import socket
from os.path import expanduser
import shutil
import multiprocessing
import clipboard
import sys
from PySide2 import QtWidgets, QtGui
home = expanduser("~")
a=1
def exiter():
    p2.terminate()
    p3.terminate()
    exit()

class SystemTrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        QtWidgets.QSystemTrayIcon.__init__(self, icon, parent)
        self.setToolTip(f'SnapPaste')
        menu = QtWidgets.QMenu(parent)
        exit_ = menu.addAction("Type in Connected device's Browser:")
        open_app = menu.addAction("{}:1111".format(IPAddr2))
        exit_ = menu.addAction("Exit")
        exit_.triggered.connect(lambda: exiter())

        menu.addSeparator()
        self.setContextMenu(menu)

def serve():
    os.system("php -S 0.0.0.0:1111")
def trans():
    while True:
        try:
            clipclr = open("Clipboards/clipcl.txt","r")
            try:
                clipboard.copy(clipclr.read())
            except TypeError:
                a=1
            clipclr.close()
            os.remove("Clipboards/clipcl.txt")
        except FileNotFoundError:
            a=0
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
    print("Do not close this Window.")
    p2=multiprocessing.Process(name='p2',target=trans)
    p3=multiprocessing.Process(name='p3',target=ntwrkmang)
    p2.start()
    p3.start()
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QWidget()
    tray_icon = SystemTrayIcon(QtGui.QIcon("icon.png"), w)
    tray_icon.show()
    tray_icon.showMessage('Connected', "{}:1111".format(IPAddr2))
    sys.exit(app.exec_())