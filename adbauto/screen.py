# adbauto/screen.py
import numpy as np
import cv2
from .adb import adb_exec_out

def get_screenshot() -> np.ndarray:
    raw = adb_exec_out("screencap -p")
    image = cv2.imdecode(np.frombuffer(raw, np.uint8), cv2.IMREAD_COLOR)
    return image
