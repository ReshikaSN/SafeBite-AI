from ultralytics import YOLO


class SafeBiteTracker:
    def __init__(self, model_path="yolo11n.pt"):
        self.model = YOLO(model_path)

    def process(self, frame):
        results = self.model.track(
            frame,
            persist=True,
            tracker="bytetrack.yaml",
            verbose=False
        )

        return results[0]