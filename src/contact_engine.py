class ContactEngine:

    def __init__(self, required_frames=5):
        self.required_frames = required_frames
        self.contact_frames = {}

    @staticmethod
    def overlap(box1, box2):
        x1, y1, x2, y2 = box1
        a1, b1, a2, b2 = box2

        ix1 = max(x1, a1)
        iy1 = max(y1, b1)
        ix2 = min(x2, a2)
        iy2 = min(y2, b2)

        if ix2 <= ix1 or iy2 <= iy1:
            return False

        return True

    def update(self, tool_id, tool_box, allergen_box):
        touching = self.overlap(tool_box, allergen_box)

        if touching:
            self.contact_frames[tool_id] = (
                self.contact_frames.get(tool_id, 0) + 1
            )
        else:
            self.contact_frames[tool_id] = 0

        return self.contact_frames[tool_id] >= self.required_frames