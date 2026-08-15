# Focus Zoom Recorder

A focus-aware Windows recorder that helps you stay anchored to the active task while turning real workflows into polished, shareable walkthroughs.

Focus Zoom Recorder follows the foreground window and cursor, reducing visual distraction while you work. The same attention-aware framing is captured as an MP4, making it easy to turn a coding session, design process, or repeatable workflow into a tutorial or demonstration.

> **Status:** working Windows prototype with live capture, foreground-window tracking, smooth cursor-following zoom, MP4 recording, and an OpenCV preview.

## Current capabilities

- automatic monitor discovery and capture with MSS
- active-window detection through Win32 APIs
- smooth cursor-following zoom
- blurred-background focus treatment outside the active window
- adjustable zoom level and reset controls
- OpenCV live preview
- on-demand MP4 recording for shareable tutorials and workflow walkthroughs
- attention-aware framing that keeps the active task visually prominent

## Technology

- Python
- OpenCV and NumPy
- MSS
- PyWin32
- PyAutoGUI and pynput

## Setup

This project is Windows-specific.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

```powershell
python main.py --list-monitors
python main.py --monitor 1
```

The first command prints each detected monitor with its resolution and desktop position. The second starts the recorder on the selected display. If no monitor is specified, monitor 1 is used.

Recordings are saved as timestamped MP4 files under `recordings/`.

Current controls:

- **E / Q:** increase or decrease zoom
- **R:** reset zoom
- **M:** toggle zoom mode
- **V:** start or stop MP4 recording
- **X:** stop recording and exit preview

## Privacy and safety

This application captures the configured desktop monitor. It can expose notifications, messages, credentials, personal files, or other private content visible on screen. Use a clean test desktop, disable notifications, and review every recording before sharing it.

## Known limitations

- key polling can toggle or adjust values repeatedly while a key is held
- Windows display scaling can still vary between hardware configurations
- errors from screen capture and active-window lookup are not shown clearly

## High-value next steps

- debounce hotkeys and display the current zoom/mode
- add pause, privacy mask, and notification-area exclusion controls
- add automated checks for zoom geometry and frame resizing
- capture a before/after demo using non-sensitive content

## License and authorship

Created by [SimpleCaci](https://github.com/SimpleCaci) and released under the [MIT License](LICENSE).
