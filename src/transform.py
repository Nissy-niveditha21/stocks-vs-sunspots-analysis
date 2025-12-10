import pandas as pd

def convert_stock_daily_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert daily stock prices to monthly data using monthly mean closing price.
    """
    df = df.set_index('Date')
    monthly_df = df.resample('M').mean(numeric_only=True)
    monthly_df = monthly_df.reset_index()
    monthly_df['Date'] = monthly_df['Date'].dt.to_period('M').dt.to_timestamp()
    return monthly_df


def clean_sunspots(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ensure sunspots dataset is monthly and formatted as Date + SunspotNumber.
    """
    # Rename sunspot column consistently
    possible_cols = ['SunspotNumber', 'Monthly Mean Total Sunspot Number', 'Sunspots']
    for col in possible_cols:
        if col in df.columns:
            df = df.rename(columns={col: 'SunspotNumber'})
            break
    
    df = df[['Date', 'SunspotNumber']]
    df['Date'] = df['Date'].dt.to_period('M').dt.to_timestamp()
    return df


def merge_stock_sunspots(stock_df: pd.DataFrame, sunspot_df: pd.DataFrame) -> pd.DataFrame:
    """
    Merge stock and sunspot datasets based on monthly date.
    """
    merged = pd.merge(stock_df, sunspot_df, on='Date', how='inner')
    return merged
