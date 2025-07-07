# NYC 311 Map

A Python package for loading, processing, and visualizing NYC 311 noise complaints.

## Project Structure

311_NYC_Chart/

├── data/

│ ├── raw/ ← 100 rows downloaded from NYC Open Data

│ ├── processed/ ← Processed data

│ └── aesthetics/ ← GeoJSON

├── src/

│ ├── config.py ← API settings, path names, and filter control

│ ├── data_loader.py ← Fetch 311 data and save to dataframe

│ ├── data_processor.py ← Clean coordinates, apply filters, convert to geom

│ ├── main.py ← Run code (with command line interface if wanted)

│ └── visualization.py ← Matplot visual

├── visual_output/ ← Folder that visuals are saved to

├── .gitignore

├── README.md

└── requirements.text

## Installation

### 1. Clone Repo

git clone https://github.com/CharlieVeronee/311_NYC_Chart.git

cd 311_NYC_Chart

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Configure API Keys (Optional)

Log into NYC Open Data and get a token and add it to config_secret.py in src/

APP_TOKEN = "YOUR_SOCRATA_APP_TOKEN"

### 4. Configuration (in src/config.py)

DATA_URL: Socrata domain (data.cityofnewyork.us)

DATASET_CODE: 311 dataset identifier (erm2-nwe9)

LIMIT: Number of records to fetch

RAW_DIR: Directory for raw CSVs

PROCESSED_DIR: Directory for cleaned CSVs

AESTHETICS: Folder for GeoJSON / shapefiles

VISUALS_DIR: Output folder for maps and plots

COMPLAINT_LIST: Complaint keywords list

AGENCY_LIST: Agency codes to include

# Usage

## Command Line

python3 src/main.py --limit --complaint --agency

for example:

python3 src/main.py --limit 80 --complaint Noise --agency NYPD DHS

will fetch 80 datapoints from NYC Open Data and chart all noise complaints reported to NYPD and DHS

## Manually

### 1 Fetch

raw = fetch_311_data(limit=200)

### 2 Save raw

save_df(raw, Path("data/raw"), "raw.csv")

### 3 Clean & filter

clean = preprocess_data(raw, complaints=["Noise"], agencies=["NYPD", "DHS"])

### 4 Convert to GeoDataFrame

gdf = df_to_gdf(clean)

### 5 Plot

plot_311(

gdf,

Path("data/aesthetics") / "NYC_Boroughs.geojson",

title="311 Noise Map",

save_dir=Path("visual_output")

)
