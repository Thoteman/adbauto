
# adbauto

**ADB-based automation for Android emulators like LDPlayer**

`adbauto` is a Python library that simplifies automation for Android games and apps running in emulators. It provides tools to connect to an emulator, capture screenshots, match UI elements visually, and simulate input like taps and scrolls.

---

## 🚀 Features

- Connect to LDPlayer or other Android emulators via ADB  
- Capture screenshots directly from the device  
- Locate UI elements via OpenCV template matching  
- Simulate taps and scrolling actions  
- Designed for building automation scripts for games  

---

## 📦 Installation

```
pip install adbauto
```

> **Note:** Make sure [ADB](https://developer.android.com/tools/adb) is installed and available in your system's PATH.

---

## 🧪 Example Usage

```python
from adbauto import adb, screen, input

# Connect to emulator
device_id = adb.get_ldplayer_device()

# Take a screenshot
img = screen.capture_screenshot(device_id)

# Find a button on screen
center = screen.find_template(img, "button_template.png")

# Tap it if found
if center:
    input.tap(device_id, *center)
```

---

## 📂 Project Structure

```
adbauto/
├── adb.py       # ADB device connection and shell utilities
├── screen.py    # Screenshot capture and template matching (OpenCV)
├── input.py     # Tap and scroll input simulation
└── __init__.py  # Module exports
```

---

## ✅ Requirements

- Python 3.8+  
- ADB installed and on PATH  
- `opencv-python`  
- `numpy`  

---

## 📃 License

MIT License © Thomas Knoops
