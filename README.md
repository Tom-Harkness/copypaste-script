# Manual paste script
Copy and paste script for greatworkethics as part of a freelancer project.

This program is intended to bypass clipboard paste blocking in Windows 10 programs by typing out clipboard contents using the Python ```keyboard``` module.

## Required Python packages
* keyboard (>=0.13.5)
* pynput (>=1.6.8)
* win32clipboard (from pywin32 301)

## Package installation: In command line enter the following commands:
* ```py -m pip install -U pip```
* ```pip install pywin32```
* ```pip install keyboard```
* ```pip install pynput```

## Script useage instructions
* Run script either from copypaste.exe or in command line with command ```python copypaste.py``` in folder containing script
* Copy with Ctrl-c as normal
* Paste in normal programs using Ctrl-c
* Force a manual paste in protected programs by using Ctrl-Shift-v
* Exit script by pressing ESC or by closing the command line interface
