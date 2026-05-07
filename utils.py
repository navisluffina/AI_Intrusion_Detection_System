import cv2
import time
import os

def draw_ui(frame, line_y, status, count):
    color = (0, 255, 0) if status == "SAFE" else (0, 0, 255)

    # Draw line
    cv2.line(frame, (0, line_y), (640, line_y), (255, 0, 0), 2)

    # Status
    cv2.putText(frame, f"Status: {status}", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)

    # Count
    cv2.putText(frame, f"People: {count}", (20, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

def save_image(frame, path):
    os.makedirs(path, exist_ok=True)
    filename = os.path.join(path, f"intrusion_{int(time.time())}.jpg")
    cv2.imwrite(filename, frame)