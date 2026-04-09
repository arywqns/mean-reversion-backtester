import pandas as pd

def run_backtest(df: pd.DataFrame) -> pd.DataFrame:
    #Run a simple daily backtest using previous day's signal

    df = df.copy()

    df["returns"] = df["price"].pct_change()
    df["strategy_returns"] = df["position"].shift(1) * df["returns"]

    df["trades"] = df["position"].diff().abs()
    cost_per_trade = 0.001 # 0.01% per trade
    df["strategy_returns"] -= df["trades"] * cost_per_trade

    df["buy_hold_equity"] = (1 + df["returns"].fillna(0)).cumprod()
    df["strategy_equity"] = (1 + df["strategy_returns"].fillna(0)).cumprod()

    return df