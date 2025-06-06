from adbauto.adb import get_emulator_device
from adbauto.screen import capture_screenshot, tap_image, tap_img_when_visible

device_id = get_emulator_device()
screenshot = capture_screenshot(device_id)

print(tap_image(device_id, screenshot, "templates/home_page.png"))
print(tap_img_when_visible(device_id, "templates/multistage_battle.png", timeout=5))
print(tap_img_when_visible(device_id, "templates/battle.png", timeout=5))
