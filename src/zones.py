import cv2


class ZoneManager:

    def __init__(self):
        self.zones = {
            "ALLERGEN": [],
            "ALLERGEN_FREE": [],
            "CLEANING": []
        }

        self.current_zone = "ALLERGEN"
        self.drawing = False
        self.start = None

    def mouse_callback(self, event, x, y, flags, param):

        if event == cv2.EVENT_LBUTTONDOWN:
            self.drawing = True
            self.start = (x, y)

        elif event == cv2.EVENT_LBUTTONUP:
            self.drawing = False

            end = (x, y)

            x1, y1 = self.start
            x2, y2 = end

            self.zones[self.current_zone] = [
                (min(x1, x2), min(y1, y2)),
                (max(x1, x2), max(y1, y2))
            ]

    def set_zone(self, zone):
        self.current_zone = zone

    def draw(self, frame):

        for name, points in self.zones.items():

            if len(points) != 2:
                continue

            (x1, y1), (x2, y2) = points

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                (255, 255, 255),
                2
            )

            cv2.putText(
                frame,
                name,
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255, 255, 255),
                2
            )

        return frame

    def get_zone(self, x, y):

        for name, points in self.zones.items():

            if len(points) != 2:
                continue

            (x1, y1), (x2, y2) = points

            if x1 <= x <= x2 and y1 <= y <= y2:
                return name

        return None