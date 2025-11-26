import keyboard
import pyautogui
import time

zoom_active = False
last_typed_time = 0
TIMEOUT = 0.3

KEYS = "abcdefghijklmnopqrstuvwxyz0123456789,./;'[]\\`-=!@#$%^&*()_+{}|:\"<>? "

def activate_zoom():
    global zoom_active, last_typed_time
    zoom_active = True
    last_typed_time = time.time()

def get_cursor_pos():
    pos = pyautogui.position()
    return (pos.x, pos.y)

def start_listener():
    keyboard.on_press(activate_zoom)

def update_zoom_state():
    global zoom_active
    if time.time() - last_typed_time > TIMEOUT:
        zoom_active = False
