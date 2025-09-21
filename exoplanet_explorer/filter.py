# filter.py
import pandas as pd

def filter_by_host(df: pd.DataFrame, hostname: str) -> pd.DataFrame:
    """
    Return all planets belonging to a given host star.
    Case-insensitive match.
    """
    return df[df["hostname"].str.lower() == hostname.lower()]

def filter_by_planet(df: pd.DataFrame, planet_name: str) -> pd.DataFrame:
    """
    Return rows for a specific planet by name.
    Case-insensitive match.
    """
    return df[df["pl_name"].str.lower() == planet_name.lower()]

def filter_by_discovery_year(df: pd.DataFrame, year: int) -> pd.DataFrame:
    """
    Return all planets discovered in a specific year.
    """
    return df[df["disc_year"] == year]

def filter_by_radius_range(df: pd.DataFrame, min_r: float, max_r: float) -> pd.DataFrame:
    """
    Return planets within a given radius range (in Earth radii).
    """
    return df[(df["pl_rade"] >= min_r) & (df["pl_rade"] <= max_r)]

def filter_by_mass_range(df: pd.DataFrame, min_m: float, max_m: float) -> pd.DataFrame:
    """
    Return planets within a given mass range (in Earth masses).
    """
    return df[(df["pl_masse"] >= min_m) & (df["pl_masse"] <= max_m)]
