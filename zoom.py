# zoom.py

import cv2

prev_cx = None
prev_cy = None
prev_zoom = 1.0

def cinematic_zoom(frame, center, zoom):
    global prev_cx, prev_cy, prev_zoom

    h, w, _ = frame.shape
    cx, cy = center

    if prev_cx is None:
        prev_cx, prev_cy = cx, cy

    # smooth movement
    prev_cx = prev_cx + (cx - prev_cx) * 0.15
    prev_cy = prev_cy + (cy - prev_cy) * 0.15

    # smooth zoom
    prev_zoom = prev_zoom + (zoom - prev_zoom) * 0.12

    box_w = int(w / prev_zoom)
    box_h = int(h / prev_zoom)

    x1 = int(prev_cx - box_w / 2)
    y1 = int(prev_cy - box_h / 2)

    x1 = max(0, min(x1, w - box_w))
    y1 = max(0, min(y1, h - box_h))

    crop = frame[y1:y1+box_h, x1:x1+box_w]
    return cv2.resize(crop, (w, h), interpolation=cv2.INTER_LINEAR)
