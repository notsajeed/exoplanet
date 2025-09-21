import pandas as pd
import requests
from io import StringIO
from pathlib import Path
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

NASA_API_URL = (
    "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?"
    "query=select+*+from+ps&format=csv"
)

# Default columns expected in the dataset
REQUIRED_COLUMNS = ["pl_name", "hostname", "pl_rade", "pl_masse", "pl_eqt", "disc_year"]

def load_exoplanet_data(source: str = "api", path: str = None, cache: bool = True) -> pd.DataFrame:
    """
    Unified loader for exoplanet data (CSV or API).
    
    Args:
        source (str): 'api' or 'csv'
        path (str, optional): Path to CSV if source='csv'
        cache (bool): Whether to cache API response locally (default True)
        
    Returns:
        pd.DataFrame: Exoplanet dataset
    """
    if source == "api":
        df = fetch_data_from_api(cache)
    elif source == "csv":
        if path is None:
            raise ValueError("CSV path must be provided if source='csv'")
        path = Path(path)
        if not path.exists():
            raise FileNotFoundError(f"CSV file not found: {path}")
        # Skip metadata header lines starting with '#'
        df = pd.read_csv(path, comment="#")
    else:
        raise ValueError("Source must be either 'api' or 'csv'")

    # Validate required columns
    missing_cols = [col for col in REQUIRED_COLUMNS if col not in df.columns]
    if missing_cols:
        logging.warning(f"Missing expected columns: {missing_cols}")

    logging.info(f"Loaded {len(df)} records from {source.upper()}")
    return df


def fetch_data_from_api(cache: bool = True, cache_path: str = "exoplanet_cache.csv") -> pd.DataFrame:
    """
    Fetch latest exoplanet data from NASA Exoplanet Archive API.
    
    Args:
        cache (bool): Save API response locally
        cache_path (str): Local cache filename
    
    Returns:
        pd.DataFrame
    """
    # Use cached CSV if available
    cache_file = Path(cache_path)
    if cache and cache_file.exists():
        logging.info(f"Loading API data from cache: {cache_file}")
        return pd.read_csv(cache_file)

    try:
        logging.info("Fetching data from NASA API...")
        response = requests.get(NASA_API_URL, timeout=30)
        response.raise_for_status()
        df = pd.read_csv(StringIO(response.text))
        logging.info(f"Fetched {len(df)} records from API")
        
        if cache:
            df.to_csv(cache_file, index=False)
            logging.info(f"API data cached to {cache_file}")
            
        return df
    except requests.RequestException as e:
        logging.error(f"Failed to fetch data from API: {e}")
        if cache_file.exists():
            logging.warning(f"Loading last cached data from {cache_file}")
            return pd.read_csv(cache_file)
        raise RuntimeError("Could not fetch API data and no cache available.") from e


def save_csv(df: pd.DataFrame, path: str):
    """
    Save DataFrame to CSV.
    
    Args:
        df (pd.DataFrame): Data to save
        path (str): File path
    """
    df.to_csv(path, index=False)
    logging.info(f"Data saved to {path}")
