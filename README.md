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
| Slope & Aspect            | Derived from DEM              | .tif     | ✅ Generated     |
| LULC / Fuel Raster        | ESA WorldCover (10 m, 2020)   | .tif     | ✅ Downloaded    |
| VIIRS Fire Points         | NASA FIRMS (Feb–Mar 2021)     | .csv     | ✅ Processed     |
| ERA5 Weather Data         | Copernicus CDS (Hourly)       | .grib    | ✅ Downloaded    |

---

## 🔧 Preprocessing Pipeline

### 1. DEM → Slope & Aspect  
- [x] Extract slope & aspect using NumPy gradients  
- [x] Save aligned to 30 m grid  

### 2. AOI Definition  
- [x] GeoJSON + Bounding Box for Similipal  
- [x] KML backup for uploads  

### 3. VIIRS Request  
- [x] Submitted to FIRMS  
- [x] Rasterized CSV → `labels_full.tif`  

### 4. Feature Stacking & Tiling  
- [x] Built 8-band stack (`features_full_stack.tif`)  
- [x] Tiled into 256×256 patches (`data/tiles/*.tif`)  

### 5. Normalization & Encoding  
- [x] Computed train-set mean/std → `norm_stats.json`  
- [x] Z-score normalized & one-hot encoded fuel → `data/tiles_norm/{train,val}/`  

---

## 🧠 Model Training (Next-Day Fire Probability)

- [x] DataLoader & U-Net setup  
- [x] Training loop executed (Epochs 1–10)  
- [x] Model weights saved (`models/unet_final.pth`)  

---

## 🛠 Tools & Libraries

- Python, NumPy, Rasterio, GeoPandas, PyTorch  
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
> 🔄 Checkpoint 5: Batch inference & evaluation in progress (threshold tuning and spatial analysis).  

---

> 🔗 Data on Google Drive: https://drive.google.com/drive/folders/1LekZLEqd4SlbBx_4DsO4C0qKodEHtEXL?usp=drive_link
