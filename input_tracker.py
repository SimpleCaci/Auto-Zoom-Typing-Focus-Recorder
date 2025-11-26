#for keyboard 

from pynput import keyboard

typing = False

def on_press(key):
    global typing
    typing = True

def on_release(key):
    pass  # do nothing for now

def start_listener():
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()


# for mouse

import pyautogui

def get_cursor_pos():
    pos = pyautogui.position()
    return (pos.x, pos.y)
