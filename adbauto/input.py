from adbauto.adb import shell

def tap(device_id, x, y):
    shell(device_id, f"input tap {x} {y}")
