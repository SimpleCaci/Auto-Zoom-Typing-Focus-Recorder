import cv2
import mss
import numpy as np


_sct = mss.mss()


def list_monitors():
    """Return physical monitors with stable one-based indexes."""
    return [
        {"index": index, **dict(monitor)}
        for index, monitor in enumerate(_sct.monitors[1:], start=1)
    ]


def get_monitor(index=1):
    monitors = list_monitors()
    for monitor in monitors:
        if monitor["index"] == index:
            return {
                key: monitor[key]
                for key in ("left", "top", "width", "height")
            }

    available = ", ".join(str(monitor["index"]) for monitor in monitors) or "none"
    raise ValueError(
        f"Monitor {index} is not available. Available monitor indexes: {available}."
    )


def grab_frame_full(monitor):
    shot = _sct.grab(monitor)
    array = np.frombuffer(shot.bgra, dtype=np.uint8)
    frame = array.reshape((monitor["height"], monitor["width"], 4))
    return cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)
