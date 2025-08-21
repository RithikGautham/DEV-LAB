import streamlit as st
import pandas as pd
from utils import load_data
from plots import plot_cyclone_path, plot_intensity
from streamlit_folium import st_folium

DATA_PATH = "hurdat2.csv"   # Adjust path if inside /data
df = load_data(DATA_PATH)

st.title("🌪 Cyclone Path & Intensity Dashboard")

cyclone_names = df["storm_name"].dropna().unique()
selected_cyclone = st.sidebar.selectbox("Select a Cyclone:", sorted(cyclone_names))

st.subheader(f"Path of Cyclone: {selected_cyclone}")
m = plot_cyclone_path(df, selected_cyclone)
st_folium(m, width=700, height=500)

st.subheader("Cyclone Intensity Over Time")
fig = plot_intensity(df, selected_cyclone)
if fig:
    st.plotly_chart(fig)
else:
    st.warning("No date column found for plotting intensity.")
