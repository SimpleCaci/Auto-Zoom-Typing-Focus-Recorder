import cv2
import input_tracker

from input_tracker import start_listener, get_cursor_pos, update_zoom_state
from zoom import smooth_zoom
from capture import grab_frame_full
from config import MONITOR, ZOOM_FACTOR
from focused_field import get_focused_field_center


def main():
    start_listener()
    print("Recording... press Q to stop.")

    cv2.namedWindow("AutoZoom Preview", cv2.WINDOW_NORMAL)

    isCursorFocus = True

    while True:

        # --- Key handling ---
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        if key == ord('m'):
            isCursorFocus = not isCursorFocus

        # update typing zoom timeout logic
        update_zoom_state()

        # --- Zoom active: use direct crop capture ---
        if input_tracker.zoom_active:

            # find the zoom target center
            try:
                center = get_focused_field_center()
            except:
                center = get_cursor_pos()

            if isCursorFocus:
                center = get_cursor_pos()

            # smooth, real zoom (no upscaling)
            frame = smooth_zoom(center, ZOOM_FACTOR, MONITOR)

            # resize window to match cropped frame dimensions
            cv2.resizeWindow("AutoZoom Preview", frame.shape[1], frame.shape[0])

        else:
            # normal mode: full-screen capture
            frame = grab_frame_full(MONITOR)

        # display frame
        cv2.imshow("AutoZoom Preview", frame)

    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
