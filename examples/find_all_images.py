from adbauto.adb import get_emulator_device, start_scrcpy
from adbauto.screen import find_all_images
import cv2

device_id = get_emulator_device()
scrcpy = start_scrcpy(device_id)

# Load template to get dimensions
template_path = "templates/arena_button.png"
template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
if template is None:
    raise FileNotFoundError(f"Template image not found at {template_path}")
h, w = template.shape[:2]

# Copy the original screenshot for drawing
frame = scrcpy.last_frame.copy()

# Find all image matches
centers = find_all_images(scrcpy.last_frame, template_path)
for center in centers:
    print(f"Found image at: {center}")
    top_left = (center[0] - w // 2, center[1] - h // 2)
    bottom_right = (center[0] + w // 2, center[1] + h // 2)
    cv2.rectangle(frame, top_left, bottom_right, (0, 255, 0), 2)  # Green border

# Show the result
cv2.imshow("Matched Images", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()