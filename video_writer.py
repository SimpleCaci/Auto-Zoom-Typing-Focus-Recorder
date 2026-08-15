from datetime import datetime
from pathlib import Path

import cv2


class VideoRecorder:
    """Manage an OpenCV MP4 recording with an explicit start/stop lifecycle."""

    def __init__(self, output_dir="recordings", fps=30.0, codec="mp4v"):
        self.output_dir = Path(output_dir)
        self.fps = float(fps)
        self.codec = codec
        self._writer = None
        self._frame_size = None
        self.output_path = None

    @property
    def is_recording(self):
        return self._writer is not None

    def start(self, frame, output_path=None):
        if self.is_recording:
            raise RuntimeError("A recording is already active.")

        height, width = frame.shape[:2]
        self._frame_size = (width, height)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        if output_path is None:
            stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            output_path = self.output_dir / f"focus-zoom-{stamp}.mp4"
        else:
            output_path = Path(output_path)
            output_path.parent.mkdir(parents=True, exist_ok=True)

        fourcc = cv2.VideoWriter_fourcc(*self.codec)
        writer = cv2.VideoWriter(str(output_path), fourcc, self.fps, self._frame_size)
        if not writer.isOpened():
            writer.release()
            raise RuntimeError(
                "Could not open the MP4 writer. Check that OpenCV supports the mp4v codec."
            )

        self._writer = writer
        self.output_path = output_path
        return output_path

    def write(self, frame):
        if not self.is_recording:
            return False

        height, width = frame.shape[:2]
        if (width, height) != self._frame_size:
            frame = cv2.resize(frame, self._frame_size)

        self._writer.write(frame)
        return True

    def stop(self):
        if not self.is_recording:
            return None

        self._writer.release()
        self._writer = None
        saved_path = self.output_path
        self._frame_size = None
        return saved_path
