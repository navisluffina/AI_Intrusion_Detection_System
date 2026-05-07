import cv2
from detector import Detector
from intrusion import IntrusionDetector
from config import LINE_Y, INTRUSION_DELAY, SAVE_PATH, WINDOW_NAME
from utils import draw_ui, save_image

detector = Detector()
intrusion = IntrusionDetector(LINE_Y, INTRUSION_DELAY)

cap = cv2.VideoCapture(0)
saved = False

print("System started. Press 'q' to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Camera error")
        break

    results = detector.detect(frame)

    if results[0].boxes is None:
        boxes = []
    else:
        boxes = results[0].boxes

    count = 0
    for box in boxes:
        if detector.model.names[int(box.cls[0])] == "person":
            count += 1

    intrusion_flag = intrusion.check_intrusion(boxes, detector.model.names)

    annotated = results[0].plot()

    status = "ALERT" if intrusion_flag else "SAFE"

    draw_ui(annotated, LINE_Y, status, count)

    if intrusion_flag and not saved:
        save_image(annotated, SAVE_PATH)
        saved = True
    elif not intrusion_flag:
        saved = False

    cv2.imshow(WINDOW_NAME, annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()