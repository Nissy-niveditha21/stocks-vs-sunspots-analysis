import pandas as pd

def load_stock_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Date"])
    return df[["Date", "Close"]]

def load_sunspot_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["Month"])
    df = df.rename(columns={"Month": "Date", "Monthly Mean Total Sunspot Number": "SunspotNumber"})
    return df[["Date", "SunspotNumber"]]
