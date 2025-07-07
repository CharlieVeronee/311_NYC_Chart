from pathlib import Path

#Socrata/API settings
DATA_URL = "data.cityofnewyork.us" #NYC OpenData URL
DATASET_CODE = "erm2-nwe9" #code for 311 complaints
LIMIT = 10000 #limit for number of rows fetched by API
TIMEOUT = 500 #seconds before API request fails

#Path Names
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR.parent / "data"
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"
AESTHETICS = DATA_DIR / "aesthetics"
VISUALS_DIR = DATA_DIR.parent / "visual_output"

#Filters
COMPLAINT_LIST = ['Noise'] #list of keywords for complaints
AGENCY_LIST = ['NYPD'] #list of agencies to include