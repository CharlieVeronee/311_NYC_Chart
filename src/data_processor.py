import pandas as pd
import re
import geopandas as gpd
from config import COMPLAINT_LIST, AGENCY_LIST

def clean_coordinates(df, lat="latitude", lon="longitude"):
    """
    Drops rows without coordinates
    Ensures coordinates are numeric
    Drop rows with invalid (non-numeric) coordinates
    """
    processed = df.copy()
    processed = processed.dropna(subset=["latitude", "longitude"])
    processed['latitude'] = pd.to_numeric(processed['latitude'], errors='coerce')
    processed['longitude'] = pd.to_numeric(processed['longitude'], errors='coerce')
    processed = processed.dropna(subset=['latitude', 'longitude'])
    return processed

def filter_complaints(df, complaints=None):
    """Filter by complaint keywords"""
    if complaints is None:
        complaints = COMPLAINT_LIST
    pattern = '|'.join([fr"\b{re.escape(c)}\b" for c in complaints])  #word-boundary match
    return df[df['complaint_type'].str.contains(pattern, case=False, na=False)]

def filter_agencies(df, agencies=None):
    """Filter by agency"""
    if agencies is None:
        agencies = AGENCY_LIST
    return df[df["agency"].isin(agencies)]

def preprocess_data(df, complaints=None, agencies=None):
    """Cleans coordinates and filters by complaints and agencies"""
    df = clean_coordinates(df)
    df = filter_complaints(df, complaints)
    df = filter_agencies(df, agencies)
    return df

def df_to_gdf(df):
    """Converts coordinates to geom points"""
    gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude), crs="EPSG:4326")
    return gdf
