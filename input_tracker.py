import keyboard
import pyautogui
import time

zoom_active = False
last_typed_time = 0
TIMEOUT = 1.2

KEYS = "abcdefghijklmnopqrstuvwxyz0123456789"

def activate_zoom(e):
    global zoom_active, last_typed_time
    zoom_active = True
    #print(last_typed_time - time.time())
    last_typed_time = time.time()

def get_cursor_pos():
    pos = pyautogui.position()
    return (pos.x, pos.y)

def start_listener():
    keyboard.on_press(activate_zoom)

def update_zoom_state():
    global zoom_active

    # if you haven't typed for at least TIMEOUT seconds, THEN disable zoom
    idle_time = time.time() - last_typed_time
    
    # don't toggle zoom in the middle of typing bursts
    if idle_time > TIMEOUT:
        zoom_active = False
