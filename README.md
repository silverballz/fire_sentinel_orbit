# fire_sentinel_orbit  
## 🔥 Forest Fire Spread Simulation using AI/ML  
*Hackathon Progress Tracker – Similipal Biosphere Reserve*  

---

## 🚀 Problem Statement

Model the *next-day forest fire probability* and simulate *short-term fire spread* (1/2/3/6/12 hours) using geospatial, weather, and land cover data — powered by AI/ML techniques like U-Net and Cellular Automata.

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
- [x] Currently resolving ERA5 patching to 30m grid  

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

---

> 🔗 Data on Google Drive: https://drive.google.com/drive/folders/1LekZLEqd4SlbBx_4DsO4C0qKodEHtEXL?usp=drive_link
