from sodapy import Socrata
import pandas as pd
from pathlib import Path
from config import DATA_URL, DATASET_CODE, LIMIT, TIMEOUT
from config_secret import APP_TOKEN
import logging

logger = logging.getLogger(__name__)

def make_data_dirs(*dirs):
    """Makes necessary dictionaries for data if not already present"""
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)
        logger.debug(f"Created directory: {d}")

def fetch_311_data(resp_limit=None):
    """Fetches raw 311 complaints from Socrata as a DataFrame"""
    if resp_limit is None:
        resp_limit = LIMIT
    #returns first x results as JSON from API, then converted to list of python dictionaries by Socrata
    client = Socrata(DATA_URL, app_token = APP_TOKEN, timeout = TIMEOUT)
    results = client.get(DATASET_CODE, limit=resp_limit) #limit x number of rows
    results_df = pd.DataFrame.from_records(results) #convert to pandas DataFrame
    logger.info(f"Fetched {len(results_df)} records from {DATA_URL}/{DATASET_CODE}")
    return results_df

def save_df(df, path, filename):
    """Save dataframe as csv for intermediate work"""
    full_path = Path(path) / filename
    df.to_csv(full_path, index=False)
    logger.info(f"Saved DataFrame to {full_path}")
    return full_path