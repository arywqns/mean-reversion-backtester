import pandas as pd
import numpy as np 

def generate_signals(
    df: pd.DataFrame, 
    window: int = 20, 
    z_threshold: float = 1.0,
    use_trend_filter: bool = False,
    trend_window: int = 50
    ) -> pd.DataFrame:
    #Generate mean reversion trading signals using a rolling z-score

    df = df.copy()

    df["ma"] = df["price"].rolling(window=window).mean()
    df["std"] = df["price"].rolling(window=window).std().replace(0, np.nan)
    df["z_score"] = (df["price"] - df["ma"])/df["std"]

    df["position"] = 0
    df.loc[df["z_score"] < -z_threshold, "position"] = 1
    df.loc[df["z_score"] > z_threshold, "position"] = -1

    if use_trend_filter:
        df["trend_ma"] = df["price"].rolling(window=trend_window).mean()

        # Only allow long trades when price is above long-term trend
        df.loc[(df["position"] == 1) & (df["price"] <= df["trend_ma"]), "position"] = 0

        # Only allow short trades when price is below long-term trend
        df.loc[(df["position"] == -1) & (df["price"] >= df["trend_ma"]), "position"] = 0

    df = df.dropna(subset=["ma", "std", "z_score"])

    return df
