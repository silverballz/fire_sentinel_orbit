# fire_sentinel_orbit
## 🔥 Forest Fire Spread Simulation using AI/ML  
**Hackathon Progress Tracker – Similipal Biosphere Reserve**

---

## 🚀 Problem Statement

Model the **next-day forest fire probability** and simulate **short-term fire spread** (1/2/3/6/12 hours) using geospatial, weather, and land cover data — powered by AI/ML techniques like U-Net and Cellular Automata.

---

## 📍 Study Area: Similipal Biosphere Reserve, Odisha, India

- **Bounding Box**:  
  - Latitude: `21.68° N` to `22.00° N`  
  - Longitude: `86.00° E` to `86.42° E`

- **Fire Event Timeline**:  
  - February–March 2021 (based on VIIRS records)

---

## ✅ Datasets Identified & Download Progress

| Dataset                      | Source                             | Status         |
|------------------------------|------------------------------------|----------------|
| Digital Elevation Model (DEM)| Bhoonidhi (CartoDEM v3 R1, 30m)    | ✅ Downloaded  |
| LULC (Fuel Raster)           | Bhuvan (LULC 10K or 50K)           | ⏳ Submitted    |
| VIIRS Fire Points (Target)   | NASA FIRMS (Feb–Mar 2021)          | ⏳ Under Review |
| ERA5 Weather Data            | Copernicus Climate Data Store      | ❌ Pending      |

---

## 🔧 Preprocessing Pipeline (WIP)

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

- [ ] Process LULC → Reclassify to fuel scores
- [ ] Stack features (slope, aspect, fuel, weather, fire history)
- [ ] Train U-Net on binary fire labels
- [ ] Simulate fire spread using Cellular Automata

---

## 🛠 Tools & Libraries

- `Python`, `NumPy`, `Rasterio`, `GeoPandas`, `PyTorch`
- Geoportals: `Bhoonidhi`, `Bhuvan`, `NASA FIRMS`, `Copernicus CDS`

---

## 📁 Directory Structure (WIP)

