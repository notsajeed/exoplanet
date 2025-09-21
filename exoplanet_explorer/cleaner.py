import pandas as pd

def clean_exoplanet_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and preprocess NASA exoplanet dataset.
    """
    # Drop unnamed / empty columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    # Convert data types safely
    dtype_map = {
        "disc_year": "Int64",
        "pl_rade": "float",
        "pl_masse": "float",
        "pl_orbper": "float",
        "pl_eqt": "float",
        "ra": "float",
        "dec": "float",
    }
    for col, dtype in dtype_map.items():
        if col in df:
            df[col] = pd.to_numeric(df[col], errors="coerce").astype(dtype)

    # Handle missing values: drop rows missing critical info
    df = df.dropna(subset=["pl_rade", "pl_orbper"], how="any")

    # Reset index after cleaning
    df = df.reset_index(drop=True)

    return df
