# adbauto/adb.py
import subprocess
from ppadb.client import Client as AdbClient

def start_adb_server():
    """Start the ADB server if it's not already running."""
    try:
        subprocess.run(["adb", "start-server"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print("ADB server started (or already running).")
    except subprocess.CalledProcessError as e:
        raise RuntimeError("Failed to start ADB server. Make sure ADB is installed and in your PATH.") from e

def get_ldplayer_device():
    """Start ADB and return the first connected LDPlayer device."""
    start_adb_server()

    client = AdbClient(host="127.0.0.1", port=5037)
    devices = client.devices()

    if not devices:
        raise RuntimeError("No devices/emulators found. Is LDPlayer running and ADB debugging enabled?")
    
    device = devices[0]
    print(f"Connected to device: {device.serial}")
    return device

