from exoplanet_explorer import loader

# Load from local CSV
try:
    df = loader.load_exoplanet_data(source="csv", path="data/exoplanet-data.csv")
    print(f"CSV Data Loaded: {len(df)} records")
except Exception as e:
    print("CSV load failed:", e)

from exoplanet_explorer import analysis as an

# from exoplanet_explorer import loader, cleaner

# df = loader.load_exoplanet_data(source="csv", path="data/exoplanet-data.csv")
# df = cleaner.clean_exoplanet_data(df)

# print(f"Cleaned Data: {len(df)} records")
# print(df.dtypes.head(10))

print(df)

print("by mass")
print(an.filter_by_mass(df,100,20000000))

print(an.filter_by_radius(df,100,20000000))

print(an.filter_habitable(df))

print(an.star_summary(df,"Kepler-29"))

