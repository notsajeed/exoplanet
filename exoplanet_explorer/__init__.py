"""
Exoplanet Explorer
==================

A Python library for exploring NASA Exoplanet Archive data.
Supports both CSV and API ingestion, filtering, analysis, and visualization.
"""

# Core submodules
from . import loader
from . import analysis
from . import visualization
from . import dashboard

# Convenience imports (most used functions directly accessible)
from .loader import load_exoplanet_data, fetch_data_from_api, save_csv
from .analysis import (
    filter_habitable,
    filter_by_radius,
    filter_by_mass,
    planet_summary,
    star_summary,
)
from .visualization import (
    plot_size_vs_orbit,
    plot_mass_vs_radius,
    plot_discovery_trends,
    plot_habitable_planets,
    plot_sky_map,
    plot_system,
)

__all__ = [
    # Submodules
    "loader",
    "analysis",
    "visualization",
    "dashboard",
    # Loader
    "load_exoplanet_data",
    "fetch_data_from_api",
    "save_csv",
    # Analysis
    "filter_habitable",
    "filter_by_radius",
    "filter_by_mass",
    "planet_summary",
    "star_summary",
    # Visualization
    "plot_size_vs_orbit",
    "plot_mass_vs_radius",
    "plot_discovery_trends",
    "plot_habitable_planets",
    "plot_sky_map",
    "plot_system",
]
