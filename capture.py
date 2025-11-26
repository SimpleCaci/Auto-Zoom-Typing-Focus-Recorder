import mss
import numpy as np
import cv2

sct = mss.mss()

def grab_frame_full(mon):
    screenshot = sct.grab(mon)
    raw = np.frombuffer(screenshot.bgra, dtype=np.uint8).reshape((mon["height"], mon["width"], 4))
    frame = cv2.cvtColor(raw, cv2.COLOR_BGRA2BGR)
    return frame

def grab_crop(x, y, width, height):
    region = {"top": y, "left": x, "width": width, "height": height}
    screenshot = sct.grab(region)
    raw = np.frombuffer(screenshot.bgra, dtype=np.uint8).reshape((height, width, 4))
    frame = cv2.cvtColor(raw, cv2.COLOR_BGRA2BGR)
    return frame
