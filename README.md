# SnapPaste
Simple file sharing AirDrop Killer tool between PCs and other devices using python & JS. Also ClipShare, feature that allows user to share their clipboard across devices including images through local network.  Currently, This project is in beta.
## What is this for ?
This for the people who wants to transfer their files from Phone to PC or PC to PC wirelessly through local network. This also allow you to paste image directly into PCs clipboard from phone's camera.
## Usage
It requires python and php to run this application. This requires proper local connection.
### Install required libraries
- In terminal or Command prompt:
```
pip3 install PySide2
pip3 install multiprocessing
pip3 install clipboard
```
### Get your computer's local IP Address
### macOS & linux
Open terminal
```
ipconfig getifaddr en0 ///for lan
ipconfig getifaddr en1 ///for wifi
```
### Windows
- For Windows we are buliding dedicated Standalone Application that can provide features what we always wanted
- Untill then
### Setup it on your own
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
- In macOS and linux type `php -S 0.0.0.0:XXXX & python3 main_mac_linux.py` to run the process in same window.
## How to sent files to PC ?
- Open any browser on any connected device on the same network and type this in addressbar:
- Your computer's local IP and portnumber which yu already entered while starting the server
- (i.e) `192.168.1.103:1234`
![index](https://github.com/revanrohith/SnapPaste/raw/master/assets/index.jpg)
![filessent](https://github.com/revanrohith/SnapPaste/raw/master/assets/filessent.png)
### In browser
- Choose `BROWSE` and the files you choose will direclty sent to Desktop of the PC.
- In `PASTE HERE` paste the clipboard contents of your phone. It will be immediately copied to PC's clipboard.
- In `CLIPBOARD BOX`. It actively displays the current content of PC's clipboard. Just Tap on that to copy it to the Phone's clipboard
- Choose `CAPTURE`, It uses phone's camera to capture image and sent it directly to Desktop's Clipboard. Where you can paste that into any application. This is useful for the Documentation.
![clipsent](https://github.com/revanrohith/SnapPaste/raw/master/uploads/Clipsent.jpg)
![clipcopied](https://github.com/revanrohith/SnapPaste/raw/master/uploads/clipreceived.jpg)
### Transfer Speed
- Transfer Speed is directly propostional to the distance between the modem and the devices(Connectivity Strength).
