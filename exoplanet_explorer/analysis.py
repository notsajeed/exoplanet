import pandas as pd

def filter_habitable(df):
    """
    Return planets in an approximate habitable zone.
    
    Criteria:
        - 0.5 <= pl_rade <= 2 (Earth radii)
        - 180 <= pl_eqt <= 310 (K)
    
    Parameters:
        df (pd.DataFrame): Exoplanet dataset
    
    Returns:
        pd.DataFrame
    """
    df = df.drop_duplicates(subset=["pl_name"]).copy()
    
    # Ensure numeric
    df["pl_rade"] = pd.to_numeric(df["pl_rade"], errors="coerce")
    df["pl_eqt"] = pd.to_numeric(df["pl_eqt"], errors="coerce")
    
    # Drop invalid data
    df = df.dropna(subset=["pl_rade", "pl_eqt"])
    
    habitable = df[
        (df["pl_rade"].between(0.5, 2, inclusive="both")) &
        (df["pl_eqt"].between(180, 310, inclusive="both"))
    ]
    return habitable


def filter_by_radius(df, min_r=None, max_r=None):
    """
    Filter planets by radius (Earth radii).
    
    Parameters:
        df (pd.DataFrame)
        min_r (float, optional): minimum radius
        max_r (float, optional): maximum radius
    
    Returns:
        pd.DataFrame
    """
    df = df.drop_duplicates(subset=["pl_name"]).copy()
    
    if "pl_rade" not in df.columns:
        raise KeyError("Column 'pl_rade' not found in dataset")
    
    df["pl_rade"] = pd.to_numeric(df["pl_rade"], errors="coerce")
    df = df.dropna(subset=["pl_rade"])
    
    query = pd.Series(True, index=df.index)
    if min_r is not None:
        query &= df["pl_rade"] >= min_r
    if max_r is not None:
        query &= df["pl_rade"] <= max_r
    return df[query]


def filter_by_mass(df, min_m=None, max_m=None):
    """
    Filter planets by mass (Earth masses).
    
    Parameters:
        df (pd.DataFrame)
        min_m (float, optional): minimum mass
        max_m (float, optional): maximum mass
    
    Returns:
        pd.DataFrame
    """
    df = df.drop_duplicates(subset=["pl_name"]).copy()
    
    if "pl_masse" not in df.columns:
        raise KeyError("Column 'pl_masse' not found in dataset")
    
    df["pl_masse"] = pd.to_numeric(df["pl_masse"], errors="coerce")
    df = df.dropna(subset=["pl_masse"])
    
    query = pd.Series(True, index=df.index)
    if min_m is not None:
        query &= df["pl_masse"] >= min_m
    if max_m is not None:
        query &= df["pl_masse"] <= max_m
    return df[query]

# ------------------ Summaries ------------------

def planet_summary(df, planet_name):
    """
    Return key properties of a planet by name.
    
    Parameters:
        df (pd.DataFrame)
        planet_name (str): exoplanet name
    
    Returns:
        dict
    """
    planet = df[df["pl_name"].str.lower() == planet_name.lower()]
    if planet.empty:
        raise ValueError(f"Planet '{planet_name}' not found in dataset")
    
    row = planet.iloc[0]
    summary = {
        "Name": row.get("pl_name"),
        "Host Star": row.get("hostname"),
        "Discovery Year": row.get("disc_year"),
        "Radius (Earth radii)": row.get("pl_rade"),
        "Mass (Earth masses)": row.get("pl_masse"),
        "Orbital Period (days)": row.get("pl_orbper"),
        "Equilibrium Temp (K)": row.get("pl_eqt"),
    }
    return summary


def star_summary(df, hostname):
    """
    Summarize planets around a given star.
    
    Parameters:
        df (pd.DataFrame)
        hostname (str): host star name
    
    Returns:
        dict
    """
    df = df.drop_duplicates(subset=["pl_name"]).copy()
    system = df[df["hostname"].str.lower() == hostname.lower()]
    
    if system.empty:
        return {"Host Star": hostname, "Number of Planets": 0, "Planets": [], "Discovery Years": []}
    
    # Deduplicate planets by name
    unique_planets = system.drop_duplicates(subset=["pl_name"])
    planets = unique_planets["pl_name"].tolist()
    years = unique_planets["disc_year"].dropna().unique().tolist()
    
    return {
        "Host Star": hostname,
        "Number of Planets": len(planets),
        "Planets": planets,
        "Discovery Years": sorted(years),
    }
