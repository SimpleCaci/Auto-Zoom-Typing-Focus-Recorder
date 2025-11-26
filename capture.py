# capture.py

import mss
import numpy as np
import cv2

_sct = mss.mss()

def grab_frame_full(mon):
    shot = _sct.grab(mon)
    arr = np.frombuffer(shot.bgra, dtype=np.uint8)
    frame = arr.reshape((mon["height"], mon["width"], 4))
    return cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
