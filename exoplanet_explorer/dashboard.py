import streamlit as st
import pandas as pd
from .loader import load_exoplanet_data
from . import visualization as viz


def init_dashboard(data_source="csv", path_or_url=None):
    """
    Initialize the dashboard app.
    
    Args:
        data_source (str): "csv" or "api".
        path_or_url (str): Path to CSV or API URL.
    """
    st.set_page_config(page_title="Exoplanet Explorer", layout="wide")

    # Sidebar
    st.sidebar.title("⚡ Exoplanet Dashboard")
    st.sidebar.info("Switch data source between CSV and API easily.")

    # Load data
    df = load_exoplanet_data(data_source, path_or_url)
    if df is None or df.empty:
        st.error("No data loaded. Please check your input.")
        return

    st.session_state["df"] = df
    st.success(f"Data loaded successfully! {len(df)} records available.")
