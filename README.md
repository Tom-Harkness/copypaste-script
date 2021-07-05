# Manual paste script
Copy and paste script for greatworkethics as part of a freelancer project.

This program is intended to bypass clipboard paste blocking in Windows 10 programs by typing out clipboard contents using the Python ```keyboard``` module.

# Required Python packages
* keyboard (>=0.13.5)
* pynput (>=1.6.8)
* win32clipboard (from pywin32 301)

# Instructions
* Run script either from copypaste.exe or in command line with command ```python copypaste.py``` in folder containing script
* Copy with Ctrl-c as normal
* Paste in normal programs using Ctrl-c
* Force a manual paste in protected programs by using Ctrl-Shift-v
