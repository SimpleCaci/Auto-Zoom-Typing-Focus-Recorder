# active_window.py

import win32gui

def get_active_window_rect():
    try:
        hwnd = win32gui.GetForegroundWindow()
        l, t, r, b = win32gui.GetWindowRect(hwnd)
        return l, t, r, b
    except:
        return None
