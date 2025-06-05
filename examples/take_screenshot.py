from adbauto.adb import get_ldplayer_device
from adbauto.screen import capture_screenshot
import cv2
'''A very simple example of a script that connects to an emulator through ADB.
    It then looks at what app is currently opened and prints the name in the console.'''

device_id = get_ldplayer_device()
img = capture_screenshot(device_id, "templates/battle.png")

# # Show the image using OpenCV
# cv2.imshow("Screenshot", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
