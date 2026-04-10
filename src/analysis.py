import pandas as pd

def compute_autocorrelation(df: pd.DataFrame):
    df = df.copy()

    df["returns"] = df["price"].pct_change()

    autocorr = df["returns"].autocorr(lag = 1)

    print(f"Autocorrelation (lag = 1): {autocorr:.4f}")