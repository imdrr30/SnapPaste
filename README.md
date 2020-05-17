# SnapPaste
Simple file sharing AirDrop Killer tool for PCs and other devices using python & JS. Also ClipShare, feature that allows user to share their clipboard across devices including images through local network.  Currently, This project is in beta.
## What is this for ?
This is for the people who wants to transfer their files from Phone to PC, PC to PC wirelessly through local network. This also allows user to paste image directly to PC's clipboard from Phone's camera.
## Install Application
- We have portable Application for both Windows & macOS runs fully functional without installation.
- [Download Now](https://snappaste.github.io/app)
## Instructions for macOS
- macOS additionally required php to run.
- If php is not installed, install it via homebrew.
- `brew install php@7.2`
- `php.ini` must also be configured to receive files with larger size
- Paste `php.ini` in from sourcecode to `/etc/`
## Usage via sourcecode
It requires python and php installed to run this application. This also requires proper local connection.
### Install required libraries
- Enter this in terminal or Command prompt to install required libraries:
```
pip3 install PySide2
pip3 install multiprocessing
pip3 install clipboard
```
### Get your computer's local IP Address
### macOS & linux
Open terminal
```
ipconfig getifaddr en0 #for lan
ipconfig getifaddr en1 #for wifi
```
### Set it up on your own
- Open cmd and type:
`ipconfig`
- Look for IPv4 address of your connection.
### Setting up the server
- Change directory to the project location and type:
`php -S 0.0.0.0:XXXX`
- Where XXXX is the port number (i.e)`1234`.
- Doing so we can able to setup local server to receive files and handle it.
![phpServer](https://github.com/revanrohith/SnapPaste/raw/master/assets/php.png)
### Setting up the file handler using python
- Open another terminal or command prompt window without closing the server.
- Change directory the project location.
- Type `python3 main_mac_linux_.py` for macOS and Linux
- Type `python3 main_win.py` for Windows.
![filehandler](https://github.com/revanrohith/SnapPaste/raw/master/assets/filehandler.png)
### Dont close either of the Windows
- If you are running macOS or linux computer, then just enter `php -S 0.0.0.0:XXXX & python3 main_mac_linux.py` in terminal to run two processes in same window.
## How to sent files to PC ?
![index](https://github.com/revanrohith/SnapPaste/raw/master/assets/index.png)
![filessent](https://github.com/revanrohith/SnapPaste/raw/master/assets/filessent.png)
- Open Internet browser in connected device, make sure they are in same network and type your computer's local IP and portnumber you gave while starting the server in addressbar
- (i.e)`192.168.1.100:1234`
### In browser
![clipsent](https://github.com/revanrohith/SnapPaste/raw/master/uploads/Clipsent.jpg)
![clipcopied](https://github.com/revanrohith/SnapPaste/raw/master/uploads/clipreceived.jpg)
- `BROWSE`, the files you choose will be direclty sent to PC's Desktop making it more accessible.
- `PASTE HERE`, paste the clipboard contents of your phone. It will be immediately copied to PC's clipboard.
- `CLIPBOARD BOX`, It actively displays the current content of PC's clipboard. Just Tap on that to copy it to the Phone's clipboard
- `CAPTURE`, It uses phone's camera to capture image and sent it directly to Desktop's Clipboard. Where you can paste that into any application.
### Transfer Speed
- Transfer Speed is directly proportional to the distance between the modem and the devices(Connectivity Strength).
