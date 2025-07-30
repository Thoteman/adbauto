# adbauto/adb.py
import subprocess
import time
import sys, os
import importlib.resources as resources
import adbauto.scrcpy as scrcpy

## UTILS
def get_adb_path():
    """Gets the path to where the adb.exe is installed."""
    if sys.platform == "win32":
        return str(resources.files("adbauto").joinpath("bin/adb.exe"))
    else:
        raise RuntimeError("adbauto currently only bundles adb.exe for Windows")
    
def hidden_run(*args, **kwargs):
    if sys.platform == "win32":
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        if "startupinfo" not in kwargs:
            kwargs["startupinfo"] = si
    return subprocess.run(*args, **kwargs)

## END OF UTILS

def run_adb_command(args):
    """Run an adb command and return its stdout as string."""
    adb_path = get_adb_path()
    adb_dir = os.path.dirname(adb_path)
    result = hidden_run([adb_path] + args, capture_output=True, text=True, cwd=adb_dir)
    if result.returncode != 0:
        raise RuntimeError(f"ADB command failed: {' '.join(args)}\n{result.stderr.strip()}")
    return result.stdout.strip()

def start_adb_server():
    """Start the ADB server if it's not already running."""
    run_adb_command(["start-server"])
    print("ADB server started (or already running).")

def list_devices():
    """Return a list of connected device IDs."""
    output = run_adb_command(["devices"])
    lines = output.splitlines()
    return [line.split()[0] for line in lines[1:] if "device" in line]

def get_emulator_device():
    """Start ADB and return the ID of the first connected device."""
    start_adb_server()
    devices = list_devices()

    if not devices:
        raise RuntimeError("No devices/emulators found. Is LDPlayer running and ADB debugging enabled?")
    
    device_id = devices[0]
    print(f"Connected to device: {device_id}")
    return device_id

def shell(device_id, command):
    """Run a shell command on the target device and return its output."""
    return run_adb_command(["-s", device_id, "shell", command])

def pull(device_id, remote_path, local_path=None):
    """Pull a file from the device to the local machine."""
    return run_adb_command(["-s", device_id, "pull", remote_path, local_path])

def start_scrcpy(device_id):
    scrcpyClient = scrcpy.Client(device=device_id)
    scrcpyClient.max_fps = 5
    scrcpyClient.bitrate = 8000000
    scrcpyClient.start(daemon_threaded=True)
    time.sleep(3)
    while scrcpyClient.last_frame is None:
        time.sleep(0.1)
    return scrcpyClient

def stop_scrcpy(scrcpyClient):
    """Stop the scrcpy client."""
    scrcpyClient.stop()
    print("scrcpy client stopped.")
    return True