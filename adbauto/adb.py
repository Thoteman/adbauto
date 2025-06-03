# adbauto/adb.py
import subprocess

def adb_shell(command: str) -> str:
    result = subprocess.run(
        ["adb", "shell"] + command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    return result.stdout.strip()

def adb_exec_out(command: str) -> bytes:
    result = subprocess.run(
        ["adb", "exec-out"] + command.split(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout
