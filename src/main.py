import argparse
from config import RAW_DIR, PROCESSED_DIR, AESTHETICS, VISUALS_DIR
from data_loader import make_data_dirs, fetch_311_data, save_df
from data_processor import preprocess_data, df_to_gdf
from visualization import plot_311
from config import LIMIT, COMPLAINT_LIST, AGENCY_LIST

def main():
    """write a command line execution like:python3 src/main.py --limit 1000 --complaint Noise --agency NYPD DHS"""
    p = argparse.ArgumentParser(description="311 data pipeline")
    p.add_argument("--limit", type=int, default=LIMIT)
    p.add_argument("--complaint", nargs="+", default=COMPLAINT_LIST)
    p.add_argument("--agency", nargs="+", default=AGENCY_LIST)
    args = p.parse_args()

    make_data_dirs(RAW_DIR, PROCESSED_DIR, VISUALS_DIR)

    raw = fetch_311_data(resp_limit=args.limit)
    save_df(raw, RAW_DIR, "311_raw.csv")

    proc = preprocess_data(raw, complaints=args.complaint, agencies=args.agency)
    save_df(proc, PROCESSED_DIR, "311_processed.csv")

    gdf = df_to_gdf(proc)
    plot_311(gdf, AESTHETICS / "NYC_Boroughs.geojson", save_dir=VISUALS_DIR)

if __name__ == "__main__":
    main()