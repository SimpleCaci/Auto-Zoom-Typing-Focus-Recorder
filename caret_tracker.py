import win32gui

def get_caret_screen_pos():
    try:
        # caret position in client coords
        cx, cy = win32gui.GetCaretPos()

        # find which window owns the caret
        hwnd = win32gui.GetForegroundWindow()

        # window's top-left in screen coordinates
        wx, wy, _, _ = win32gui.GetWindowRect(hwnd)

        # caret position in screen coordinates
        return (wx + cx, wy + cy)
    except:
        return None
