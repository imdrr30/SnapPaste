import os
import time
from os.path import expanduser
import shutil
import subprocess
import clipboard
home = expanduser("~")
a=1

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


if __name__ == '__main__':
    multiprocessing.freeze_support()
    print("Do not close this Window.")
    p2=multiprocessing.Process(name='p2',target=trans)
    p3=multiprocessing.Process(name='p3',target=serve)
    trans()
