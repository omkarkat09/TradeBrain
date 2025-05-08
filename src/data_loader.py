import os
import pandas as pd
from alpha_vantage.timeseries import TimeSeries
from dotenv import load_dotenv
from pathlib import Path

# Load API key from .env
load_dotenv()
API_KEY = os.getenv("38AVWOM0I961XOAL")

# Create data directory if it doesn't exist
DATA_DIR = Path("../data")
DATA_DIR.mkdir(parents=True, exist_ok=True)


def fetch_daily_stock(symbol: str, output_size: str = 'full') -> pd.DataFrame:
    """
    Fetch daily historical stock data from Alpha Vantage.

    Parameters:
        symbol (str): Stock ticker (e.g., 'AAPL', 'TSLA')
        output_size (str): 'compact' (last 100 days) or 'full' (up to 20 years)

    Returns:
        pd.DataFrame: OHLCV DataFrame indexed by date
    """
    try:
        ts = TimeSeries(key=API_KEY, output_format='pandas')
        df, meta = ts.get_daily(symbol=symbol, outputsize=output_size)
        df.rename(columns=lambda x: x.split('. ')[1].capitalize(), inplace=True)
        df.index.name = 'Date'

        # Save to CSV
        csv_path = DATA_DIR / f"{symbol}_daily.csv"
        df.to_csv(csv_path)
        print(f"[✔] Data for {symbol} saved to {csv_path}")

        return df

    except Exception as e:
        print(f"[✖] Error fetching data for {symbol}: {e}")
        return pd.DataFrame()


# Example usage
if __name__ == "__main__":
    # Fetch full historical data for Apple
    df_apple = fetch_daily_stock("AAPL", output_size='full')
    print(df_apple.head())
