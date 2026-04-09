import matplotlib.pyplot as plt 
import pandas as pd

def plot_equity_curves(df: pd.DataFrame, output_path: str = "results/equity_curve.png") -> None:
    plt.figure(figsize=(10,6))
    plt.plot(df.index, df["buy_hold_equity"], label = "Buy and Hold")
    plt.plot(df.index, df["strategy_equity"], label = "Mean Reversion Strategy")
    plt.xlabel("Date")
    plt.ylabel("Portfolio Value")
    plt.title("Strategy vs Buy and Hold")
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close
