# main.py — Final Cinematic Build

import cv2
import numpy as np
import win32gui
import win32api
import win32con

from capture import grab_frame_full
from zoom import cinematic_zoom
from active_window import get_active_window_rect
from config import MONITOR


# ------------ helpers ------------
def lerp(a, b, t):
    return a + (b - a) * t


# ------------ mouse wheel ------------
last_wheel = 0

def get_scroll_delta():
    global last_wheel
    wheel = win32api.GetAsyncKeyState(win32con.VK_MBUTTON)
    if wheel < 0 and last_wheel >= 0:
        last_wheel = wheel
        return +1
    last_wheel = wheel
    return 0


# ------------ main program ------------
def main():
    cv2.namedWindow("AutoZoom Preview", cv2.WINDOW_NORMAL)

    desired_zoom = 1.5
    target_zoom = 1.5
    zoom_min, zoom_max = 1.0, 3.5

    outside_lerp = 0.0

    while True:

        # ------------------- ZOOM INPUT -------------------
        if get_scroll_delta():
            desired_zoom += 0.20

        if win32api.GetAsyncKeyState(ord('E')):
            desired_zoom += 0.10
        if win32api.GetAsyncKeyState(ord('Q')):
            desired_zoom -= 0.10
        if win32api.GetAsyncKeyState(ord('R')):
            desired_zoom = 1.5

        desired_zoom = max(zoom_min, min(desired_zoom, zoom_max))


        # ------------------- FRAME CAPTURE -------------------
        frame = grab_frame_full(MONITOR)
        mon_w, mon_h = MONITOR["width"], MONITOR["height"]


        # ------------------- WINDOW RECT -------------------
        rect = get_active_window_rect()
        if rect:
            wx, wy, wr, wb = rect
        else:
            wx = wy = 0
            wr = mon_w
            wb = mon_h


        # ------------------- MOUSE POSITION -------------------
        mx, my = win32gui.GetCursorPos()
        inside = (wx <= mx <= wr and wy <= my <= wb)


        # ------------------- INSIDE WINDOW -------------------
        if inside:
            outside_lerp = lerp(outside_lerp, 0.0, 0.20)
            target_zoom = lerp(target_zoom, desired_zoom, 0.15)

            win_cx = (wx + wr) // 2
            win_cy = (wy + wb) // 2

            tx = int(lerp(win_cx, mx, 0.35))
            ty = int(lerp(win_cy, my, 0.35))

            tx -= MONITOR["left"]
            ty -= MONITOR["top"]

            frame = cinematic_zoom(frame, (tx, ty), target_zoom)


        # ------------------- OUTSIDE WINDOW -------------------
        else:
            outside_lerp = lerp(outside_lerp, 1.0, 0.12)
            target_zoom = lerp(target_zoom, 1.0, 0.20)

            # compute relative crop
            cx1 = max(0, wx - MONITOR["left"])
            cy1 = max(0, wy - MONITOR["top"])
            cx2 = min(mon_w, wr - MONITOR["left"])
            cy2 = min(mon_h, wb - MONITOR["top"])

            if cx2 - cx1 > 5 and cy2 - cy1 > 5:
                window_crop = frame[cy1:cy2, cx1:cx2]
            else:
                window_crop = frame

            blurred_bg = cv2.GaussianBlur(frame, (55, 55), 0)
            output = blurred_bg.copy()

            win_h, win_w, _ = window_crop.shape

            scale = lerp(1.0, 1.09, outside_lerp)
            sw = int(win_w * scale)
            sh = int(win_h * scale)

            scaled = cv2.resize(window_crop, (sw, sh))

            off_x = (mon_w - sw) // 2
            off_y = (mon_h - sh) // 2

            px1 = max(0, off_x)
            py1 = max(0, off_y)
            px2 = min(mon_w, off_x + sw)
            py2 = min(mon_h, off_y + sh)

            sx1 = px1 - off_x
            sy1 = py1 - off_y
            sx2 = sx1 + (px2 - px1)
            sy2 = sy1 + (py2 - py1)

            output[py1:py2, px1:px2] = scaled[sy1:sy2, sx1:sx2]
            frame = output


        # ------------------- DISPLAY -------------------
        cv2.imshow("AutoZoom Preview", frame)
        if cv2.waitKey(1) & 0xFF == ord('X'):
            break

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
