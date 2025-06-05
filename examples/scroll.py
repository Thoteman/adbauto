from adbauto.input import scroll
from adbauto.adb import get_ldplayer_device

device_id = get_ldplayer_device()
scroll(device_id, direction="down", amount=600)