import pandas as pd

def load_data(filepath):
    """
    Load and clean HURDAT2 cyclone dataset.
    """
    df = pd.read_csv(filepath)
    
    # Normalize column names
    df.columns = df.columns.str.strip().str.lower()

    # Convert date
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Fix latitude & longitude (convert from 28.0N / 94.8W → numeric)
    def convert_lat(val):
        if isinstance(val, str) and val[-1] in ["N","S"]:
            num = float(val[:-1])
            return num if val[-1] == "N" else -num
        return pd.to_numeric(val, errors="coerce")

    def convert_lon(val):
        if isinstance(val, str) and val[-1] in ["E","W"]:
            num = float(val[:-1])
            return num if val[-1] == "E" else -num
        return pd.to_numeric(val, errors="coerce")

    if "latitude" in df.columns:
        df["latitude"] = df["latitude"].apply(convert_lat)
    if "longitude" in df.columns:
        df["longitude"] = df["longitude"].apply(convert_lon)

    return df
