import unittest
from unittest.mock import MagicMock, patch

import capture


class MonitorDiscoveryTests(unittest.TestCase):
    def test_list_monitors_skips_virtual_all_monitors_entry(self):
        fake_capture = MagicMock()
        fake_capture.monitors = [
            {"left": 0, "top": 0, "width": 3200, "height": 1080},
            {"left": 0, "top": 0, "width": 1920, "height": 1080},
            {"left": 1920, "top": 0, "width": 1280, "height": 1024},
        ]

        with patch.object(capture, "_sct", fake_capture):
            monitors = capture.list_monitors()

        self.assertEqual([monitor["index"] for monitor in monitors], [1, 2])
        self.assertEqual(monitors[1]["left"], 1920)

    def test_get_monitor_returns_mss_capture_geometry(self):
        fake_capture = MagicMock()
        fake_capture.monitors = [
            {"left": 0, "top": 0, "width": 3200, "height": 1080},
            {"left": -1280, "top": 40, "width": 1280, "height": 1024},
        ]

        with patch.object(capture, "_sct", fake_capture):
            monitor = capture.get_monitor(1)

        self.assertEqual(
            monitor,
            {"left": -1280, "top": 40, "width": 1280, "height": 1024},
        )

    def test_get_monitor_reports_available_indexes(self):
        fake_capture = MagicMock()
        fake_capture.monitors = [
            {"left": 0, "top": 0, "width": 1920, "height": 1080},
            {"left": 0, "top": 0, "width": 1920, "height": 1080},
        ]

        with patch.object(capture, "_sct", fake_capture):
            with self.assertRaisesRegex(ValueError, "Available monitor indexes: 1"):
                capture.get_monitor(3)


if __name__ == "__main__":
    unittest.main()
