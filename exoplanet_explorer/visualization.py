import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sns.set(style="whitegrid", context="talk")

def plot_size_vs_orbit(df):
    df = df.copy()
    for col in ["pl_rade", "pl_orbper"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["pl_rade", "pl_orbper"])
    df = df[(df["pl_rade"] > 0) & (df["pl_orbper"] > 0)]

    if df.empty:
        raise ValueError("No valid data to plot.")

    plt.figure(figsize=(8,6))
    plt.scatter(df["pl_orbper"], df["pl_rade"], alpha=0.6)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Orbital Period (days)")
    plt.ylabel("Planet Radius (Earth radii)")
    plt.title("Planet Size vs Orbital Period")
    plt.show()

def plot_mass_vs_radius(df):
    df = df.copy()
    for col in ["pl_rade", "pl_masse"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["pl_rade", "pl_masse"])
    df = df[(df["pl_rade"] > 0) & (df["pl_masse"] > 0)]

    if df.empty:
        raise ValueError("No valid data to plot.")

    plt.figure(figsize=(8,6))
    plt.scatter(df["pl_rade"], df["pl_masse"], alpha=0.6)
    plt.xscale("log")
    plt.yscale("log")
    plt.xlabel("Planet Radius (Earth radii)")
    plt.ylabel("Planet Mass (Earth masses)")
    plt.title("Planet Mass vs Radius")
    plt.show()

def plot_discovery_trends(df):
    df = df.copy()
    df["disc_year"] = pd.to_numeric(df["disc_year"], errors="coerce")
    trend = df.groupby("disc_year").size()
    trend = trend[trend.index.notna()]

    plt.figure(figsize=(10,6))
    trend.plot(kind="bar", color="skyblue")
    plt.xlabel("Discovery Year")
    plt.ylabel("Number of Planets")
    plt.title("Exoplanet Discoveries per Year")
    plt.tight_layout()
    plt.show()

def plot_habitable_planets(df):
    df = df.copy()
    for col in ["pl_rade", "pl_eqt"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["pl_rade", "pl_eqt"])

    if df.empty:
        raise ValueError("No valid data to plot.")

    plt.figure(figsize=(8,6))
    plt.scatter(df["pl_eqt"], df["pl_rade"], c="green", alpha=0.7)
    plt.axhline(2, color="red", linestyle="--", alpha=0.6)
    plt.axhline(0.5, color="red", linestyle="--", alpha=0.6)
    plt.axvline(310, color="blue", linestyle="--", alpha=0.6)
    plt.axvline(180, color="blue", linestyle="--", alpha=0.6)
    plt.xlabel("Equilibrium Temperature (K)")
    plt.ylabel("Planet Radius (Earth radii)")
    plt.title("Potentially Habitable Planets")
    plt.show()

def plot_sky_map(df):
    df = df.copy()
    for col in ["ra", "dec"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["ra", "dec"])

    if df.empty:
        raise ValueError("No valid data to plot.")

    plt.figure(figsize=(10,5))
    plt.scatter(df["ra"], df["dec"], s=10, alpha=0.6)
    plt.xlabel("Right Ascension (deg)")
    plt.ylabel("Declination (deg)")
    plt.title("Sky Map of Exoplanets")
    plt.show()

def plot_system(df, hostname):
    df = df.copy()
    df["pl_orbper"] = pd.to_numeric(df["pl_orbper"], errors="coerce")
    df["pl_rade"] = pd.to_numeric(df["pl_rade"], errors="coerce")
    system = df[df["hostname"].str.lower() == hostname.lower()]
    system = system.dropna(subset=["pl_orbper", "pl_rade"])

    if system.empty:
        raise ValueError(f"No system found for host star '{hostname}'")

    plt.figure(figsize=(8,6))
    plt.scatter(system["pl_orbper"], system["pl_rade"], c="orange", s=80, edgecolors="k")
    for _, row in system.iterrows():
        plt.text(row["pl_orbper"], row["pl_rade"], str(row.get("pl_letter", "")), fontsize=9)
    plt.xscale("log")
    plt.xlabel("Orbital Period (days)")
    plt.ylabel("Planet Radius (Earth radii)")
    plt.title(f"Planetary System: {hostname}")
    plt.show()
