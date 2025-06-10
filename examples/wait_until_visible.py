from adbauto.adb import get_emulator_device, start_scrcpy
from adbauto.screen import tap_image, tap_img_when_visible

device_id = get_emulator_device()
scrcpy = start_scrcpy(device_id)

print(tap_img_when_visible(device_id, scrcpy, "templates/home_page.png"))
print(tap_img_when_visible(device_id, scrcpy, "templates/multistage_battle.png", timeout=5))
print(tap_img_when_visible(device_id, scrcpy, "templates/battle.png", timeout=5))
