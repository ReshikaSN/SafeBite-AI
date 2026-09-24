import cv2
from src.zones import ZoneManager

zones = ZoneManager()

cap = cv2.VideoCapture(0)

window = "SafeBite AI - Zone Setup"

cv2.namedWindow(window)
cv2.setMouseCallback(window, zones.mouse_callback)

print("""
SafeBite AI Zone Setup

1 = Allergen Zone
2 = Allergen-Free Zone
3 = Cleaning Zone

Drag mouse to draw a zone.
Press Q to quit.
""")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = zones.draw(frame)

    cv2.putText(
        frame,
        f"Current: {zones.current_zone}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 255),
        2
    )

    cv2.imshow(window, frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("1"):
        zones.set_zone("ALLERGEN")

    elif key == ord("2"):
        zones.set_zone("ALLERGEN_FREE")

    elif key == ord("3"):
        zones.set_zone("CLEANING")

    elif key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()