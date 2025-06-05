from adbauto.adb import get_ldplayer_device

'''A very simple example of a script that connects to an emulator through ADB.
    It then looks at what app is currently opened and prints the name in the console.'''

device = get_ldplayer_device()
current_activity = device.shell("dumpsys window windows | grep -E 'mCurrentFocus'")
print(current_activity)
