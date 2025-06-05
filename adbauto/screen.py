# adbauto/screen.py

import cv2
import numpy as np
import os
import tempfile
from adbauto.adb import shell, pull

def capture_screenshot(device_id, local_path=None):
    """
    Captures a screenshot from the device and returns it as an OpenCV image (BGR).
    Optionally saves it to local_path.
    """
    # Create a temporary path if none is given
    if local_path is None:
        tmp_dir = tempfile.gettempdir()
        local_path = os.path.join(tmp_dir, "screen.png")

    remote_path = "/sdcard/screen.png"

    # Take screenshot on device
    shell(device_id, f"screencap -p {remote_path}")

    # Pull screenshot to PC
    pull(device_id, remote_path, local_path)

    # Read with OpenCV
    image = cv2.imread(local_path)

    if image is None:
        raise RuntimeError(f"Failed to read screenshot at {local_path}")

    return image
