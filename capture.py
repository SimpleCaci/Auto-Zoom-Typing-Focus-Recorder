import mss
import numpy as np

def grab_frame(monitor):
    with mss.mss() as sct:
        frame = np.array(sct.grab(monitor))
        return frame[:, :, :3]  # strip alpha channel
