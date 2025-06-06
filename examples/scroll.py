from adbauto.input import scroll
from adbauto.adb import get_emulator_device

device_id = get_emulator_device()
scroll(device_id, direction="down", amount=600)