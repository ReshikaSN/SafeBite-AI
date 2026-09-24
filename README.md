# SafeBite-AI
SafeBite AI is a computer-vision food safety system that tracks kitchen tools, allergen contact history, cleaning events, and workspace zones to detect potential allergen cross-contact and trigger real-time alerts using YOLO, OpenCV, and Streamlit.
# 🛡️ SafeBite AI

**SafeBite AI** is an AI-powered food safety prototype designed to prevent **potential allergen cross-contact in kitchens**.

The system combines **computer vision, object tracking, spatial zones, and contact-history memory** to track food-contact tools such as knives and determine whether they may carry allergen residue from one preparation area to another.

### 🔍 How It Works

Kitchen Camera
      ↓
YOLO Object Detection
      ↓
Object Tracking
      ↓
Tool–Ingredient Contact Detection
      ↓
AllergenTrace Memory
      ↓
Zone Transition Analysis
      ↓
Risk Assessment
      ↓
🚨 Cross-Contact Alert


### 🧠 AllergenTrace

The core engine maintains a digital history for each food-contact tool.

Example:


Knife-01
   ↓
Contacts peanut-containing ingredient
   ↓
Potential Allergen Carryover
   ↓
Enters Allergen-Free Zone
   ↓
🚨 HIGH-RISK ALERT
   ↓
Cleaning Event
   ↓
CLEAN


### ⚙️ Technology Stack

* Python
* YOLO / Ultralytics
* OpenCV
* Streamlit
* PyTorch
* NumPy
* Pandas
* Roboflow datasets

### 🎯 Prototype Features

* Real-time kitchen object detection
* Food-contact tool tracking
* Allergen contact history
* Allergen-free zone monitoring
* Potential cross-contact risk detection
* Cleaning-event state reset
* Risk scoring and event logging
* Interactive Streamlit dashboard

### ⚠️ Scientific Scope

SafeBite AI does **not claim to chemically detect allergens** using RGB cameras. Instead, it identifies **potential allergen carryover based on object interaction history, spatial movement, and recorded cleaning events**.

### 🚀 Vision

SafeBite AI aims to provide an affordable, scalable computer-vision-based safety layer for **institutional kitchens, cafeterias, hospitals, schools, hotels, and food-service environments** where preventing accidental allergen cross-contact is critical.

