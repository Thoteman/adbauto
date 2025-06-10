from adbauto.adb import get_emulator_device, start_scrcpy
from adbauto.screen import tap_image
import time

device_id = get_emulator_device()
scrcpy = start_scrcpy(device_id)

print(tap_image(device_id, scrcpy.last_frame, "templates/home_page.png"))
time.sleep(3)
print(tap_image(device_id, scrcpy.last_frame, "templates/multistage_battle.png"))
time.sleep(3)
print(tap_image(device_id, scrcpy.last_frame, "templates/battle.png"))