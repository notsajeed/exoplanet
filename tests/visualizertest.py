from exoplanet_explorer import loader

# Load from local CSV
try:
    df = loader.load_exoplanet_data(source="csv", path="data/exoplanet-data.csv")
    df = df.drop_duplicates(subset=["pl_name"])
    print(f"CSV Data Loaded: {len(df)} records")
except Exception as e:
    print("CSV load failed:", e)

from exoplanet_explorer import visualization as viz


viz.plot_discovery_trends(df)
viz.plot_habitable_planets(df)
viz.plot_size_vs_orbit(df)
viz.plot_mass_vs_radius(df)
viz.plot_sky_map(df)
# viz.plot_system(df,"CoRoT-12")

# print(df.head())