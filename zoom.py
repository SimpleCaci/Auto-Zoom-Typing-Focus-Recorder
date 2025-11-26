import numpy as np
from capture import grab_crop

prev_cx = None
prev_cy = None
prev_zoom = None

def smooth_zoom(center, target_zoom, MONITOR):
    global prev_cx, prev_cy, prev_zoom

    tx, ty = center
    w = MONITOR["width"]
    h = MONITOR["height"]

    # --- Smooth state initialization ---
    if prev_cx is None:
        prev_cx, prev_cy = tx, ty
    if prev_zoom is None:
        prev_zoom = target_zoom

    # --- Smooth center movement ---
    cx = prev_cx + (tx - prev_cx) * 0.18
    cy = prev_cy + (ty - prev_cy) * 0.18

    # --- Smooth zoom factor ---
    zoom = prev_zoom + (target_zoom - prev_zoom) * 0.12
    zoom = max(1.0, min(zoom, 3.0))  # limit zoom range

    prev_cx, prev_cy, prev_zoom = cx, cy, zoom

    # --- Maintain aspect ratio ---
    box_w = int(w / zoom)
    aspect = w / h
    box_h = int(box_w / aspect)

    half_w = box_w // 2
    half_h = box_h // 2

    # --- Clamp center so crop stays on-screen ---
    cx = int(min(max(cx, half_w), w - half_w))
    cy = int(min(max(cy, half_h), h - half_h))

    # --- Absolute screen coordinates for MSS ---
    x1 = MONITOR["left"] + cx - half_w
    y1 = MONITOR["top"] + cy - half_h

    # --- Fast region capture ---
    zoomed = grab_crop(x1, y1, box_w, box_h)
    return zoomed
