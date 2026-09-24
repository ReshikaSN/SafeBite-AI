import streamlit as st
import cv2
from ultralytics import YOLO
from src.state_engine import ToolStateEngine

# -----------------------------
# PAGE SETUP
# -----------------------------
st.set_page_config(
    page_title="SafeBite AI",
    page_icon="🛡️",
    layout="wide"
)
model = YOLO("yolo11n.pt")

st.title("🛡️ SafeBite AI")
st.subheader("AllergenTrace — Real-Time Cross-Contact Prevention")

# -----------------------------
# CREATE MEMORY ENGINE
# -----------------------------
if "engine" not in st.session_state:
    st.session_state.engine = ToolStateEngine()

engine = st.session_state.engine

tool_id = "Knife-01"

# Get current tool state
state = engine.get_state(tool_id)

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🧠 AllergenTrace Memory")

st.sidebar.write("**Tool ID:**", tool_id)
st.sidebar.write("**State:**", state["state"])
st.sidebar.write(
    "**Last allergen:**",
    state["last_allergen"] if state["last_allergen"] else "None"
)
st.sidebar.write(
    "**Cleaning events:**",
    state["cleaning_events"]
)

# Status indicator
if state["state"] == "POTENTIAL_ALLERGEN_CARRYOVER":
    st.sidebar.error("🚨 POTENTIAL ALLERGEN CARRYOVER")
else:
    st.sidebar.success("✅ TOOL CLEAN")

# -----------------------------
# MAIN DASHBOARD
# -----------------------------
st.divider()

st.header("🔬 AllergenTrace Control Panel")

col1, col2, col3 = st.columns(3)

# -----------------------------
# PEANUT CONTACT
# -----------------------------
with col1:
    if st.button("🥜 Peanut Contact", use_container_width=True):

        engine.allergen_contact(
            tool_id,
            "peanut"
        )

        st.session_state.message = (
            "🥜 Knife-01 contacted a peanut-containing ingredient."
        )

        st.rerun()

# -----------------------------
# ALLERGEN-FREE ZONE
# -----------------------------
with col2:
    if st.button(
        "➡️ Enter Allergen-Free Zone",
        use_container_width=True
    ):

        result = engine.check_zone_entry(
            tool_id,
            "ALLERGEN_FREE"
        )

        if result["alert"]:
            st.error("🚨 HIGH RISK — CROSS-CONTACT WARNING")
            st.warning(result["message"])

        else:
            st.success("✅ No cross-contact risk detected.")

# -----------------------------
# CLEANING
# -----------------------------
with col3:
    if st.button(
        "🧼 Cleaning Completed",
        use_container_width=True
    ):

        engine.cleaning_event(tool_id)

        st.session_state.message = (
            "🧼 Cleaning event recorded. Tool state reset."
        )

        st.rerun()

# -----------------------------
# RISK SCORE
# -----------------------------
st.divider()

st.header("⚠️ Cross-Contact Risk")

if state["state"] == "POTENTIAL_ALLERGEN_CARRYOVER":
    risk_score = 85
    risk_level = "HIGH"
    st.error(f"🚨 Risk Score: {risk_score}/100 — {risk_level}")
else:
    risk_score = 5
    risk_level = "LOW"
    st.success(f"✅ Risk Score: {risk_score}/100 — {risk_level}")

# -----------------------------
# CURRENT STATUS
# -----------------------------
st.divider()

st.header("📊 Current Tool Status")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Tool",
        tool_id
    )

with col2:
    st.metric(
        "Last Allergen",
        state["last_allergen"] or "None"
    )

with col3:
    if state["state"] == "CLEAN":
        st.metric("Risk Level", "LOW")
    else:
        st.metric("Risk Level", "HIGH")

# -----------------------------
# DEMO MESSAGE
# -----------------------------
if "message" in st.session_state:
    st.info(st.session_state.message)

# -----------------------------
# EXPLANATION
# -----------------------------
st.divider()

st.header("💡 How SafeBite Works")

st.write("""
SafeBite AI creates a digital contact history for food-contact tools.

A tool that contacts an allergen-containing ingredient is assigned a
Potential Allergen Carryover state.

If that tool subsequently enters an allergen-free workflow without a
validated cleaning event, SafeBite generates a high-risk warning.
""")

st.caption(
    "Prototype note: SafeBite detects potential allergen carryover "
    "from process history; it does not chemically detect allergens."
)

st.divider()
st.header("📷 Kitchen Camera")

camera = st.camera_input("Take a kitchen image")

if camera is not None:

    # Read image
    image_bytes = camera.getvalue()

    with open("camera.jpg", "wb") as f:
        f.write(image_bytes)

    frame = cv2.imread("camera.jpg")

    # YOLO detection
    results = model(frame, verbose=False)

    # Draw detections
    annotated = results[0].plot()

    st.image(
        cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB),
        caption="SafeBite AI — Object Detection",
        use_container_width=True
    )

    # Show detected objects
    st.subheader("🔎 Detected Objects")

    detected = []

    for box in results[0].boxes:
        class_id = int(box.cls[0])
        name = model.names[class_id]
        confidence = float(box.conf[0])

        detected.append(
            f"{name} — {confidence:.0%}"
        )

    if detected:
        for item in detected:
            st.write("•", item)
    else:
        st.write("No objects detected.")