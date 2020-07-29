from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi, os
from threading import Thread
import clipboard
import subprocess
import validators, webbrowser
from tkinter import *
import pyqrcode

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            if self.path=='/':
                with open('index.html', 'rb') as f:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(f.read())
            elif self.path=='/Clipboards/clippc.txt':
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes(clipboard.paste(),'utf-8'))
            elif self.path!='/Clipboards/clippc.txt':
                with open(self.path[1:],'rb') as f:
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(f.read())
        except:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'File not found')

    def do_POST(self):
        if self.path=='/upload.php':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            filename = form['upl'].filename
            data = form['upl'].file.read()
            open(os.environ["HOME"]+'/Desktop/'+filename, "wb").write(data)
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'Done.')
        if self.path=='/mupload.php':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            data = form['upl'].file.read()
            open('toClip.jpg', "wb").write(data)
            if os.path.isfile("toClip.jpg"):
                subprocess.run(["osascript", "-e",
                                'set the clipboard to (read (POSIX file "toClip.jpg") as JPEG picture)'])
                os.remove("toClip.jpg")
            self.send_response(200)
            self.send_header('Location','/')
            self.end_headers()
        elif self.path=='/clipp.php':
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST',
                         'CONTENT_TYPE': self.headers['Content-Type'],
                         })
            data = form['textdata'].file.read()
            clipboard.copy(data)
            if validators.url(data):
                webbrowser.open(data, new=2)
            self.send_response(301)
            self.send_header('Location','/')
            self.end_headers()

def showcon(addr):
    webbrowser.open("{}/web/index.html".format(addr),new=2)
def startt():
    httpd = HTTPServer(("0.0.0.0", 80), SimpleHTTPRequestHandler)
    httpd.serve_forever()

if __name__ == '__main__':
    IPAddr2=''
    for i in range(10):
        IPAddr2=os.popen(f'ipconfig getifaddr en{i}').read()
        if IPAddr2!='':
            break
    ss = Thread(name='p1', target=startt)
    ss.start()
    qr="http://"+str(IPAddr2)[:-1]
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