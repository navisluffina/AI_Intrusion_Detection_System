import time

class IntrusionDetector:
    def __init__(self, line_y, delay):
        self.line_y = line_y
        self.delay = delay
        self.start_time = None
        self.confirmed = False

    def check_intrusion(self, boxes, names):
        intrusion_now = False

        for box in boxes:
            cls = int(box.cls[0])

            if names[cls] == "person":
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                cy = (y1 + y2) // 2

                if cy > self.line_y:
                    intrusion_now = True

        if intrusion_now:
            if self.start_time is None:
                self.start_time = time.time()
            elif time.time() - self.start_time > self.delay:
                self.confirmed = True
        else:
            self.start_time = None
            self.confirmed = False

        return self.confirmed