# Author: Tom Harkness
# Created: July 5, 2021

"""Script to replicate Ctrl-V paste by the following steps:
    - Use pynput to listen for Ctrl-Shift-v or ESC hotkeys
    - Once hotkey is detected, access clipboard contents with pywin32's win32clipboard module
    - Write clipboard contents with keyboard module"""

from datetime import datetime
import keyboard
import pynput
import win32clipboard
import os


def on_activate_paste():
    # get clipboard text with pywin32
    win32clipboard.OpenClipboard()
    try:
        clipboard_text = win32clipboard.GetClipboardData()
    except (NameError, TypeError):
        clipboard_text = None
    win32clipboard.CloseClipboard()

    try:
        assert(clipboard_text is not None)
        print(f"{datetime.now()} - Pasting: {clipboard_text}")
        keyboard.release('ctrl+shift+z')
        keyboard.write(clipboard_text)
    except AssertionError:
        print(f"{datetime.now()} - Nothing on clipboard.")


def on_activate_esc():
    print(f"Esc pressed... Exiting script at {datetime.now()}")
    exit()


def for_canonical(f):
    return lambda k: f(listener.canonical(k))


if __name__ == "__main__":
    os.system('cls')
    print("\n-- Copy/Paste script running --")
    print(f"-- Started at {datetime.now()}-- ")
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.CloseClipboard()
    print("-- Clipboard has been cleared --\n")
    print("Press Ctrl-c to copy highlighted text")
    print("Press Ctrl-Shift-v to paste current text using PyAutoGUI")
    print("Exit script by pressing ESC or closing this console\n")

    controller = pynput.keyboard.Controller()

    hotkey_paste = pynput.keyboard.HotKey(
        pynput.keyboard.HotKey.parse('<ctrl>+<shift>+v'),
        on_activate_paste)

    hotkey_esc = pynput.keyboard.HotKey(
        pynput.keyboard.HotKey.parse('<esc>'),
        on_activate_esc)

    # Collect hotkey events
    listener = pynput.keyboard.Listener(
            on_press=for_canonical(hotkey_paste.press),
            on_release=for_canonical(hotkey_paste.release),
            suppress=False)
    listener.start()

    listener_esc = pynput.keyboard.Listener(
            on_press=for_canonical(hotkey_esc.press),
            on_release=for_canonical(hotkey_esc.release),
            suppress=False)
    listener_esc.start()
    listener_esc.join()
