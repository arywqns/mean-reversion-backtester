import pandas as pd
import numpy as np

def generate_momentum_signals(df: pd.DataFrame, window: int = 50, threshold: float = 0.01) -> pd.DataFrame:
    """
    Generate momentum trading signals using a moving average rule with a threshold.

    Long when price is sufficiently above the moving average.
    Short when price is sufficiently below the moving average.
    """

    df = df.copy()
    df["trend_ma"] = df["price"].rolling(window=window).mean()
    df["position"] = 0

    df.loc[df["price"] > df["trend_ma"] * (1 + threshold), "position"] = 1
    df.loc[df["price"] < df["trend_ma"] * (1 - threshold), "position"] = -1

    df = df.dropna(subset=["trend_ma"])

    df["position"] = df["position"].replace(0, np.nan)
    df["position"] = df["position"].ffill().fillna(0)

    return df