from adbauto.adb import get_emulator_device, start_scrcpy
import cv2
'''A very simple example of a script that connects to an emulator through ADB.
    It then looks at what app is currently opened and prints the name in the console.'''

device_id = get_emulator_device()
device_id = get_emulator_device()
scrcpy = start_scrcpy(device_id)
img = scrcpy.last_frame

# Show the image using OpenCV
cv2.imshow("Screenshot", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
