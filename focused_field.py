from pywinauto import Desktop
import time

def get_focused_field_center():
    """Returns (x, y) of the center of the focused text field."""
    try:
        focused = Desktop(backend="uia")
        print(focused)
        focused  = focused.from_point(0, 0)
        print(focused)
        '''
        if not focused:
            return None

        rect = focused.rectangle()

        center_x = (rect.left + rect.right) // 2
        center_y = (rect.top + rect.bottom) // 2

        return (center_x, center_y)
        '''

    except Exception as e:
        print("UIA error:", e)
        return None
