# fire_sentinel_orbit
## 🔥 Forest Fire Spread Simulation using AI/ML  
*Hackathon Progress Tracker – Similipal Biosphere Reserve*

---

## 🚀 Problem Statement

Model the *next-day forest fire probability* and simulate *short-term fire spread* (1/2/3/6/12 hours) using geospatial, weather, and land cover data — powered by AI/ML techniques like U-Net and Cellular Automata.

---

## 📍 Study Area: Similipal Biosphere Reserve, Odisha, India

- *Bounding Box*:  
  - Latitude: 21.68° N to 22.00° N  
  - Longitude: 86.00° E to 86.42° E

- *Fire Event Timeline*:  
  - February–March 2021 (based on VIIRS records)

---

## ✅ Datasets Acquired & Shared

All data required for modeling has been successfully downloaded and processed.

📦 Access the full dataset bundle here:  
🔗 [Google Drive – Fire Sentinel Dataset](https://drive.google.com/drive/folders/1LekZLEqd4SlbBx_4DsO4C0qKodEHtEXL?usp=sharing)

| Dataset                   | Source                        | Format   | Status         |
|---------------------------|-------------------------------|----------|----------------|
| Digital Elevation Model   | Bhoonidhi (CartoDEM v3 R1)    | .tif   | ✅ Downloaded  |
| Slope & Aspect            | Derived from DEM              | .tif   | ✅ Generated   |
| LULC / Fuel Raster        | ESA WorldCover (10m, 2020)    | .tif   | ✅ Downloaded  |
| VIIRS Fire Points         | NASA FIRMS (Feb–Mar 2021)     | .csv   | ✅ Under Review |
| ERA5 Weather Data         | Copernicus CDS (Hourly)       | .nc    | ✅ Requested    |

---

## 🔧 Preprocessing Pipeline (Completed Phase 1)

### 1. DEM → Slope & Aspect
- [x] Extract slope (°) and aspect (°) using NumPy gradients
- [x] Output raster aligned to 30 m resolution

### 2. AOI Definition
- [x] GeoJSON + Bounding Box defined for Similipal region
- [x] KML backup created for FIRMS/Bhoonidhi uploads

### 3. VIIRS Request
- [x] Submitted request to FIRMS using AOI (Feb–Mar 2021)
- [ ] Convert downloaded CSV to binary fire/no-fire rasters

---

## 🧠 Next Steps

- [ ] Reclassify LULC into fuel scores
- [ ] Stack all features (slope, aspect, fuel, weather, fire history)
- [ ] Train U-Net on binary fire labels
- [ ] Simulate fire spread using Cellular Automata
- [ ] Build interactive visualization and animation tools

---

## 🛠 Tools & Libraries

- Python, NumPy, Rasterio, GeoPandas, PyTorch
- Geoportals: Bhoonidhi, ESA WorldCover, NASA FIRMS, Copernicus CDS

---


---

## 👥 Team CORBETT
- Leader: Anurag Sharma
- Members: Anurag Sharma, Jayesh Kapoor, Nityansh Pant, Maittri Tripathi
- Hackathon: HackOrbit 2025

---

> ✅ Checkpoint 2 Status: Data acquisition complete. Modeling phase begins.
