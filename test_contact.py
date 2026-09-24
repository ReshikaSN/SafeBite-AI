from src.contact_engine import ContactEngine

engine = ContactEngine(required_frames=3)

tool = (100, 100, 200, 200)
peanut = (150, 150, 250, 250)

for frame in range(5):

    contact = engine.update(
        "Knife-01",
        tool,
        peanut
    )

    print(
        f"Frame {frame + 1}: "
        f"contact={contact}"
    )