from adbauto.adb import get_emulator_device, shell
'''A very simple example of a script that connects to an emulator through ADB.
    It then looks at what app is currently opened and prints the name in the console.'''

device_id = get_emulator_device()
activity = shell(device_id, "dumpsys window windows | grep -E 'mCurrentFocus'")
print(activity)