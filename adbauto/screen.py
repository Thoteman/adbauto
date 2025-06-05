# adbauto/screen.py

import cv2
import numpy as np
import os
import tempfile
import time
from adbauto.adb import shell, pull
from adbauto.input import tap

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

def find_image(screenshot, image_path, threshold=0.8):
    """
    Finds a image in the screenshot using OpenCV template matching.
    Returns the center coordinates of the matched image if found, otherwise None.
    """
    image = cv2.imread(image_path)
    result = cv2.matchTemplate(screenshot, image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if max_val >= threshold:
        h, w = image.shape[:2]
        center = (max_loc[0] + w // 2, max_loc[1] + h // 2)
        return center
    return None

def tap_image(device_id, screenshot, image_path, threshold=0.8):
    """
    Finds a image in the screenshot and taps it if found.
    Returns the coordinates of the tap or None if not found.
    """
    center = find_image(screenshot, image_path, threshold)
    if center:
        tap(device_id, center[0], center[1])
        return center
    return None

def tap_img_when_visible(device_id, image_path, threshold=0.8, timeout=10):
    """
    Continuously checks for the image on the screen and taps it when found.
    Returns the coordinates of the tap or None if not found within timeout.
    """
    start_time = time.time()

    while True:
        screenshot = capture_screenshot(device_id)
        center = find_image(screenshot, image_path, threshold)

        if center:
            tap(device_id, center[0], center[1])
            return center

        if time.time() - start_time > timeout:
            break

    return None