import pandas as pd
import numpy as np 

def generate_signals(df: pd.DataFrame, window: int = 20, z_threshold: float = 1.0) -> pd.DataFrame:
    #Generate mean reversion trading signals using a rolling z-score

    df = df.copy()

    df["ma"] = df["price"].rolling(window=window).mean()
    df["std"] = df["price"].rolling(window=window).std()
    df["z_score"] = (df["price"] - df["ma"])/df["std"]

    df["position"] = 0
    df.loc[df["z_score"] < -z_threshold, "position"] = 1
    df.loc[df["z_score"] > z_threshold, "position"] = -1

    df.dropna(inplace=True)

    return df
