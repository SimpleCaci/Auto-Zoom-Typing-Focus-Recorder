import pywinauto
from pywinauto import Desktop
import time

def get_focused_field_center():
    """Returns (x, y) of the center of the focused text field."""
    try:
        windows = Desktop(backend="uia").windows()
        for window in windows:
            if window.is_active():
                focused_window = window
                print("Focused Window is")
                print(focused_window)

        if not focused_window:
            return None

        rect = focused_window.rectangle()

        center_x = (rect.left + rect.right) // 2
        center_y = (rect.top + rect.bottom) // 2

        return (center_x, center_y)

    except Exception as e:
        print("UIA error:", e)
        return None
