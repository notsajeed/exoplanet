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
    if "pl_rade" not in df.columns:
        raise KeyError("Column 'pl_rade' (planet radius) not found in dataset")

    query = pd.Series([True] * len(df))
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
    if "pl_masse" not in df.columns:
        raise KeyError("Column 'pl_masse' (planet mass) not found in dataset")

    query = pd.Series([True] * len(df))
    if min_m is not None:
        query &= df["pl_masse"] >= min_m
    if max_m is not None:
        query &= df["pl_masse"] <= max_m
    return df[query]


def planet_summary(df, planet_name):
    """
    Return key properties of a planet by name.
    
    Parameters:
        df (pd.DataFrame)
        planet_name (str): exoplanet name (e.g., 'Kepler-186 f')
    
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


def star_summary(df, star_name):
    """
    Return info about a host star and its planets.
    
    Parameters:
        df (pd.DataFrame)
        star_name (str): host star name
    
    Returns:
        dict
    """
    system = df[df["hostname"].str.lower() == star_name.lower()]
    if system.empty:
        raise ValueError(f"Star '{star_name}' not found in dataset")

    planets = system["pl_name"].tolist()
    star_info = {
        "Host Star": star_name,
        "Number of Planets": len(planets),
        "Planets": planets,
        "Discovery Years": system["disc_year"].dropna().unique().tolist(),
    }
    return star_info
