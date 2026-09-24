import cv2
from src.tracker import SafeBiteTracker

tracker = SafeBiteTracker()

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Camera not available")
    exit()

print("✅ SafeBite AI tracking started")
print("Press Q to quit")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    result = tracker.process(frame)

    annotated = result.plot()

    cv2.imshow("SafeBite AI - Tracking", annotated)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()