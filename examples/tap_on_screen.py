from adbauto.adb import get_ldplayer_device
from adbauto.screen import capture_screenshot, tap_image

device_id = get_ldplayer_device()
screenshot = capture_screenshot(device_id)

tap_image(device_id, screenshot, "templates/home_page.png")