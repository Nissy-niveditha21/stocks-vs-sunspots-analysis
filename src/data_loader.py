import pandas as pd

def load_stock_data(stock_path: str) -> pd.DataFrame:
    df = pd.read_csv(stock_path)
    
    # Ensure date is parsed
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    
    # Drop rows with missing dates
    df = df.dropna(subset=['Date'])
    return df


def load_sunspot_data(sunspot_path: str) -> pd.DataFrame:
    df = pd.read_csv(sunspot_path)
    
    # Sunspot dataset typically has Year, Month columns OR a YYYY-MM timestamp
    if 'Month' in df.columns:
        # Example format: 1749 Jan
        df['Month'] = pd.to_datetime(df['Month'], errors='coerce')
        df = df.rename(columns={'Month': 'Date'})
    elif 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    else:
        # Fallback: combine Year + Month
        df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))
    
    df = df.dropna(subset=['Date'])
    return df
