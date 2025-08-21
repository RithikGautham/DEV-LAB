import folium
import plotly.express as px

def plot_cyclone_path(df, cyclone_name):
    """
    Create Folium map for a selected cyclone.
    """
    cyclone_data = df[df["storm_name"].str.upper() == cyclone_name.upper()]

    if cyclone_data.empty:
        return folium.Map(location=[20, 80], zoom_start=3)

    start_coords = [cyclone_data["latitude"].iloc[0], cyclone_data["longitude"].iloc[0]]
    m = folium.Map(location=start_coords, zoom_start=4)

    coords = list(zip(cyclone_data["latitude"], cyclone_data["longitude"]))
    folium.PolyLine(coords, color="red", weight=3, opacity=0.8).add_to(m)

    for _, row in cyclone_data.iterrows():
        folium.CircleMarker(
            location=[row["latitude"], row["longitude"]],
            radius=4,
            popup=f"{row['storm_name']} | {row['maximum_sustained_wind_knots']} kt",
            color="blue",
            fill=True
        ).add_to(m)

    return m


def plot_intensity(df, cyclone_name):
    """
    Create Plotly chart of cyclone wind speed over time.
    """
    cyclone_data = df[df["storm_name"].str.upper() == cyclone_name.upper()]

    if "date" not in cyclone_data.columns:
        return None

    fig = px.line(
        cyclone_data,
        x="date",
        y="maximum_sustained_wind_knots",
        title=f"Wind Speed Over Time - {cyclone_name}",
        labels={"maximum_sustained_wind_knots": "Wind Speed (kt)"}
    )
    return fig
