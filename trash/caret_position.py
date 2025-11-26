from pywinauto import uia_element_info, uia_defines
from pywinauto.uia_defines import IUIA
import time

uia = IUIA()

def get_caret_position():
    try:
        # get focused UI element
        focused = uia.GetFocusedElement()
        if not focused:
            return None

        # Try to get caret range bounding rectangle
        try:
            caretRange = focused.Get_CaretRange()
            if caretRange:
                rects = caretRange.GetBoundingRectangles()
                if rects:
                    r = rects[0]
                    return (r.left, r.top, r.right, r.bottom)
        except:
            pass

        # fallback: element bounds
        rect = focused.BoundingRectangle
        return (rect.left, rect.top, rect.right, rect.bottom)

    except Exception as e:
        print("Caret error:", e)
        return None
