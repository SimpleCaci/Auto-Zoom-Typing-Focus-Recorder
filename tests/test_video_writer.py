import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np

from video_writer import VideoRecorder


class VideoRecorderTests(unittest.TestCase):
    @patch("video_writer.cv2.VideoWriter")
    @patch("video_writer.cv2.VideoWriter_fourcc", return_value=1234)
    def test_start_write_stop_lifecycle(self, _fourcc, writer_factory):
        writer = MagicMock()
        writer.isOpened.return_value = True
        writer_factory.return_value = writer
        frame = np.zeros((720, 1280, 3), dtype=np.uint8)

        with tempfile.TemporaryDirectory() as temp_dir:
            output = Path(temp_dir) / "demo.mp4"
            recorder = VideoRecorder(output_dir=temp_dir, fps=30)
            self.assertEqual(recorder.start(frame, output), output)
            self.assertTrue(recorder.is_recording)
            self.assertTrue(recorder.write(frame))
            self.assertEqual(recorder.stop(), output)

        writer.write.assert_called_once_with(frame)
        writer.release.assert_called_once()
        self.assertFalse(recorder.is_recording)

    @patch("video_writer.cv2.VideoWriter")
    def test_start_raises_when_codec_cannot_open(self, writer_factory):
        writer = MagicMock()
        writer.isOpened.return_value = False
        writer_factory.return_value = writer
        frame = np.zeros((100, 100, 3), dtype=np.uint8)

        with tempfile.TemporaryDirectory() as temp_dir:
            recorder = VideoRecorder(output_dir=temp_dir)
            with self.assertRaises(RuntimeError):
                recorder.start(frame)

        writer.release.assert_called_once()


if __name__ == "__main__":
    unittest.main()
