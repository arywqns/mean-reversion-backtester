import yfinance as yf
import pandas as pd 

def load_data(ticker: str, start: str = "2018-01-01", end: str = "2025-01-01") -> pd.DataFrame:
    #Download historical adjusted close prices for a ticker

    df = yf.download(ticker, start=start, end=end, auto_adjust=True)

    if df.empty:
        raise ValueError(f"No data returned for ticker {ticker}")

    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)

    df = df[["Close"]].copy()
    df.rename(columns={"Close":"price"}, inplace = True)
    df.dropna(inplace = True)

    return df
