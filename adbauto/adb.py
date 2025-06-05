# adbauto/adb.py
import subprocess

def run_adb_command(args):
    """Run an adb command and return its stdout as string."""
    result = subprocess.run(["adb"] + args, capture_output=True, text=True)
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

def get_ldplayer_device():
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
