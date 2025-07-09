import streamlit as st
from PIL import Image

st.set_page_config(layout="centered", page_title="Fire Sentinel Orbit")

st.title("🔥 Fire Sentinel: Predicting & Simulating Forest Fires")
st.markdown("---")

# Intro Section
st.markdown("""
## 🌲 Overview

**Fire Sentinel** is a two-stage geospatial intelligence system to help mitigate forest fire risk using AI and physics-based modeling.

Our project is focused on the **Similipal Biosphere Reserve**, Odisha — an ecologically sensitive and fire-prone region.

---
""")

# Stage 1
st.header("📍 Stage 1: Fire Probability Prediction")
st.markdown("""
In the first stage, we trained a deep learning model (**U-Net**) to predict the **next-day fire risk** based on:

- 🌿 **Fuel availability** (Land cover type from Sentinel/Bhuvan)
- 🧭 **Wind** (ERA5 weather data)
- 📈 **Terrain slope** (from Bhoonidhi DEM)
- 🔥 **Fire history** (VIIRS active fire detections)

We trained on multi-band raster tiles and thresholded the prediction map using an optimal cutoff (≈ 0.145) to generate a final binary risk mask.

This binary map tells us **where a fire is most likely to start tomorrow**.
""")

# Stage 1 image
try:
    stage1_img = Image.open("stage1_predicted_fire_map.png")
    st.image(stage1_img, caption="Predicted Fire Risk Map (Stage 1)", use_container_width=True)
except:
    st.warning("⚠️ Stage 1 image not found. Please upload `stage1_predicted_fire_map.png` in the app folder.")

# Stage 2
st.header("🌐 Stage 2: Fire Spread Simulation")
st.markdown("""
After predicting the ignition zones, we used a **physics-informed Cellular Automata** model to simulate how a fire would spread.

Spread dynamics consider:
- Wind speed and direction
- Terrain slope
- Local fuel availability

We simulated fire spread over **1h, 2h, 3h, 4h, 5h**, using raster-based updates at each timestep.

This animation shows how the fire progresses over terrain:
""")

# Spread GIF
try:
    spread_gif = open("fire_spread_colored.gif", "rb").read()
    st.image(spread_gif, caption="🔥 Fire Spread Simulation over Time", use_container_width=True)
except:
    st.warning("⚠️ Spread animation not found. Please upload `fire_spread_colored.gif` in the app folder.")

# Completion note
st.markdown("---")
st.success("✅ Fire Sentinel simulation complete and visualized.")

# Credits (optional)
st.markdown("""
<small>
Developed by **Team CORBETT** for HackOrbit 2025  
Powered by open datasets (Bhoonidhi, Sentinel-2, ERA5, VIIRS) and PyTorch.
</small>
""", unsafe_allow_html=True)
