# fire_sentinel_orbit  
## 🔥 Forest Fire Spread Simulation using AI/ML  
*Hackathon Progress Tracker – Similipal Biosphere Reserve*  

---

## 🚀 Problem Statement

Model the *next-day forest fire probability* and simulate *short-term fire spread* (1/2/3/6/12 hours) using geospatial, weather, and land cover data — powered by AI/ML techniques like U-Net and Cellular Automata.

---

## 🌐 Deployed App

🚀 **Live Demo**: [corbett-is-on-fire.streamlit.app](https://corbett-is-on-fire.streamlit.app)

---

## 📍 Study Area: Similipal Biosphere Reserve, Odisha, India

- **Bounding Box**:  
  - Latitude: 21.68° N to 22.00° N  
  - Longitude: 86.00° E to 86.42° E

- **Fire Event Timeline**:  
  - February–March 2021 (based on VIIRS records)

---

## ✅ Datasets Acquired & Shared

All data required for modeling has been successfully downloaded and processed.

🔗 [Google Drive – Fire Sentinel Dataset](https://drive.google.com/drive/folders/1LekZLEqd4SlbBx_4DsO4C0qKodEHtEXL?usp=drive_link)

| Dataset                   | Source                        | Format   | Status           |
|---------------------------|-------------------------------|----------|------------------|
| Digital Elevation Model   | Bhoonidhi (CartoDEM v3 R1)    | .tif     | ✅ Downloaded    |
| Slope & Aspect            | Derived via `gdaldem`         | .tif     | ✅ Generated     |
| LULC / Fuel Raster        | ESA WorldCover (10 m, 2020)   | .tif     | ✅ Reclassified  |
| VIIRS Fire Points         | NASA FIRMS (Feb–Mar 2021)     | .csv     | ✅ Rasterized    |
| ERA5 Weather Data         | Copernicus CDS (Hourly)       | .grib    | ✅ Parsed (u,v,t) |

---

## 🔧 Preprocessing Pipeline

### 1. DEM → Slope & Aspect  
- [x] Used `gdaldem slope` and `gdaldem aspect`  
- [x] Reprojected and clipped to AOI  
- [x] Created binary slope fire mask (15°–45°)

### 2. Fuel Mask from LULC  
- [x] Mapped LULC classes to fuel load levels  
- [x] Created `fuel_mask_final.tif`  

### 3. Wind-Aligned Aspect Zones  
- [x] Derived u10, v10 from ERA5  
- [x] Translated wind direction into zones  
- [x] Created aspect-wind-aligned binary mask  

### 4. Ignition Points Map  
- [x] Combined masks (slope, fuel, aspect-wind)  
- [x] Created final ignition probability raster  
- [x] Visualized over NDVI and hillshade  

---

## 📦 Feature Stack (Day 2 Checkpoint 1)

- [x] Verified and resampled slope, aspect, fuel maps  
- [x] Normalized raster transforms and resolutions  
- [x] Patching ERA5 onto 30m grid  

---

## 🧠 Model Status

### ❌ Day 1: Scrapped Model
- Original U-Net pipeline was dropped due to poor signal in labels and lack of clean separation in class predictions.

### ✅ New Direction (Day 2)
- 🔄 Working toward a hybrid model:
  - Rule-based ignition zone
  - Cellular Automata for short-term spread

---

## 🛠 Tools & Libraries

- Python, NumPy, Rasterio, GeoPandas, Matplotlib  
- GDAL, Cartopy, PyTorch, ERA5 climate APIs  
- Geoportals: Bhoonidhi, ESA WorldCover, NASA FIRMS, Copernicus CDS  
- Streamlit, Pillow (for the deployed app)

---

## 👥 Team CORBETT

- **Leader:** Anurag Sharma  
- **Members:** Anurag Sharma, Jayesh Kapoor, Nityansh Pant, Maittri Tripathi  
- **Hackathon:** HackOrbit 2025  

---

## 🕹️ Checkpoints

> ✅ Checkpoint 1: Data acquisition complete.  
> ✅ Checkpoint 2: Feature stacking & tiling complete.  
> ✅ Checkpoint 3: Normalization & encoding complete.  
> ✅ Checkpoint 4: Model training complete (Epoch 10/10).  
> ❌ Checkpoint 5: Model scrapped due to poor performance.  

> ✅ **Day 2 – Checkpoint 1:**  
> – Rebuilt terrain and fuel masks from scratch  
> – Final ignition raster visualized  
> – Hillshade and NDVI overlays added  

> ✅ **Day 2 – Checkpoint 2:**  
> - ✅ Generated training tiles (256×256 patches) from raster stack  
> - ✅ Created binary label masks from ignition points  
> - ✅ One-hot encoded categorical features (fuel) and normalized continuous layers  
> - ✅ Defined custom PyTorch `ForestFireDataset` to load .npy patches  
> - ✅ Built a minimal U-Net model for fire/no-fire binary classification  

> ✅ **Day 2 – Checkpoint 3:**  
> - ✅ Trained up to 2 epochs initially and visualized predictions  
> - ✅ Evaluated model predictions on tiles — thresholded outputs with optimal value (≈0.145)  
> - ✅ Computed prediction stats: min, max, avg-max  
> - ✅ Visualized predicted masks and compared with ground truth labels  
> - ✅ Saved binarized fire/no-fire `.tif` masks from U-Net predictions  
> - ✅ Evaluated performance metrics:  
>   - 🔹 Recall: 1.0000  

> ✅ **Day 2 – Checkpoint 4:**  
> - ✅ Completed Cellular Automata-based fire spread simulation  
> - ✅ Simulated fire progression at 1h, 2h, 3h, 4h, and 5h intervals  
> - ✅ Saved spread masks as GeoTIFFs and logged burned area counts per timestep  
> - ✅ Generated animated GIF over colored DEM and fuel overlays for visualizing spread dynamics  

---

## 🖼️ Final Streamlit App Overview

The Streamlit web app serves as a demo of both stages:

### 📍 Stage 1: Fire Probability Prediction
- AI-driven U-Net model predicts ignition-prone zones based on geospatial and meteorological inputs.
- Resulting fire probability map is thresholded and visualized as a binary mask.

### 🌐 Stage 2: Fire Spread Simulation
- A physics-inspired Cellular Automata algorithm simulates fire propagation using:
  - Terrain slope
  - Fuel availability
  - Wind direction

- The animated fire spread progression is overlaid on DEM + fuel layers for intuitive understanding.

🛰️ Hosted App: [corbett-is-on-fire.streamlit.app](https://corbett-is-on-fire.streamlit.app)

---

> 🔗 Data on Google Drive: https://drive.google.com/drive/folders/1LekZLEqd4SlbBx_4DsO4C0qKodEHtEXL?usp=drive_link
