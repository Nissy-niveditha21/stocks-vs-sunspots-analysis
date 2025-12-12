import pandas as pd

def convert_daily_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    df = df.set_index("Date")
    monthly = df.resample("M").mean().reset_index()
    return monthly

def merge_datasets(stocks: pd.DataFrame, sunspots: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(stocks, sunspots, on="Date", how="inner")
    return merged
