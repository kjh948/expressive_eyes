# Expressive Eyes


![24 images of different expressive eyes](https://git.brl.ac.uk/ca2-chambers/expressive-eyes/raw/524a6cc95a393120c11053bedd9a0a74a6e1a2f7/doc/Face_Images/All_faces_no_colour.png)


## Requirements


- Python 3.8.3
- numpy
- scipy
- pycozmo (see below)

- **Install the requirements for pycozmo:**
- [Pillow 6.0.0](https://github.com/python-pillow/Pillow) - Python image library
- [FlatBuffers](https://github.com/google/flatbuffers) - serialization library
- [dpkt](https://github.com/kbandla/dpkt) - TCP/IP packet parsing library

Install my copy of pycozmo (do not use pip install pycozmo):
- `git clone https://git.brl.ac.uk/ca2-chambers/pycozmo`
- `cd pycozmo`
- `python3 setup.py install --user`


## To install/use on a Linux machine


- Install from source:
- `git clone https://git.brl.ac.uk/b2-kaya/expressive-eyes-improved`
- `cd expressive-eyes-improved`
- `python3 setup.py install --user`

- Run demo file:
- `cd examples`
- `python3 demo.py`


## To install/use on the Jolla phone

- SSH on the phone
- `cd /media/sdcard/7318-A0DD/src/expressive-eyes` (clone the repo first if needed)
- `git pull`
- `python3 setup.py install --user`

The first time, you need to install the app to make it accessible from the shell:
- `ln -s /media/sdcard/7318-A0DD/src/expressive-eyes /usr/share/expressive_eyes`
- `cp qml/expressive-eyes.desktop /usr/share/applications/`
- `cp qml/expressive_eyes.png /usr/share/icons/hicolor/86x86/apps/`
