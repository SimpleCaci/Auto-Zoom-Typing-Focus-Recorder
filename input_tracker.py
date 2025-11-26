import keyboard
import pyautogui
import time

zoom_active = False
last_typed_time = 0
TIMEOUT = 2

KEYS = "abcdefghijklmnopqrstuvwxyz0123456789,./;'[]\\`-=!@#$%^&*()_+{}|:\"<>? "

def activate_zoom(e):
    global zoom_active, last_typed_time
    zoom_active = True
    last_typed_time = time.time()
    print(last_typed_time - time.time())

def get_cursor_pos():
    pos = pyautogui.position()
    return (pos.x, pos.y)

def start_listener():
    keyboard.on_press(activate_zoom)