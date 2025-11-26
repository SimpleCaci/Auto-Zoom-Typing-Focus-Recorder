import cv2
import time
from capture import grab_frame
from input_tracker import start_listener, zoom_active, get_cursor_pos
from zoom import smooth_zoom
from config import MONITOR, FPS, ZOOM_FACTOR

def main():
    global zoom_active
    start_listener()
    frame_delay = 1 / FPS

    print("Recording... press Q to stop.")

    cv2.namedWindow("AutoZoom Preview", cv2.WINDOW_NORMAL) #single screen instance

    while True:
        frame = grab_frame(MONITOR)

        if zoom_active:
            print("zoom_activating...")
            center = get_cursor_pos()
            frame = smooth_zoom(frame, center, ZOOM_FACTOR)

        cv2.imshow("AutoZoom Preview", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(frame_delay)


    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()