import cv2

def smooth_zoom(frame, center, zoom_factor=1.6):
    h, w, _ = frame.shape
    cx, cy = center

    # Calculate zoomed region size
    box_w = int(w / zoom_factor)
    box_h = int(h / zoom_factor)

    # Boundaries of zoom window
    x1 = max(0, cx - box_w // 2)
    y1 = max(0, cy - box_h // 2)
    x2 = min(w, x1 + box_w)
    y2 = min(h, y1 + box_h)

    # Crop + scale back up
    zoomed = frame[y1:y2, x1:x2]
    zoomed = cv2.resize(zoomed, (w, h))

    return zoomed
