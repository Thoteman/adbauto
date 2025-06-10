from adbauto.adb import get_emulator_device, start_scrcpy
from adbauto.screen import capture_screenshot, tap_image

device_id = get_emulator_device()
scrcpy = start_scrcpy(device_id)
print(scrcpy.resolution)

#tap_image(device_id, screenshot, "templates/home_page.png")