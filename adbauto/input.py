from adbauto.adb import shell

def tap(device_id, x, y):
    shell(device_id, f"input tap {x} {y}")

def scroll(
    device_id,
    direction="up",
    amount=300,
    duration=300,
    start_x=540,
    start_y=960
):
    """
    Perform a swipe in any direction on a 1080x1920 screen.

    Args:
        device_id (str): ADB device ID.
        direction (str): One of 'up', 'down', 'left', 'right',
                         'up-left', 'up-right', 'down-left', 'down-right'.
        amount (int): Total distance of the swipe (applied diagonally if needed).
        duration (int): Duration of the swipe in ms.
        start_x (int): Start X position (default: 540).
        start_y (int): Start Y position (default: 960).
    """

    dx, dy = 0, 0

    direction = direction.lower()
    if direction == "up":
        dy = -amount
    elif direction == "down":
        dy = amount
    elif direction == "left":
        dx = -amount
    elif direction == "right":
        dx = amount
    elif direction == "up-left":
        dx, dy = -amount, -amount
    elif direction == "up-right":
        dx, dy = amount, -amount
    elif direction == "down-left":
        dx, dy = -amount, amount
    elif direction == "down-right":
        dx, dy = amount, amount
    else:
        raise ValueError("Invalid direction. Use 'up', 'down', 'left', 'right', or diagonal variants.")

    x2 = start_x + dx
    y2 = start_y + dy

    shell(device_id, f"input swipe {start_x} {start_y} {x2} {y2} {duration}")