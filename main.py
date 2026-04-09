from src.data_loader import load_data
from src.signals import generate_signals
from src.backtest import run_backtest
from src.metrics import compute_metrics
from src.plot import plot_equity_curves

import pandas as pd

def main():
    ticker = "SPY"
    df = load_data(ticker = ticker)

    windows = [10, 20, 50]
    thresholds = [0.5, 1.0, 1.5]

    results = []

    for w in windows:
        for t in thresholds:
            temp_df = generate_signals(df, window=w, z_threshold=t)
            temp_df = run_backtest(temp_df)

            metrics = compute_metrics(temp_df["strategy_returns"])

            results.append({
                "window": w,
                "threshold": t,
                "total_return": metrics["total_return"],
                "sharpe": metrics["sharpe_ratio"],
                "max_drawdown": metrics["max_drawdown"]
            })
        
    results_df = pd.DataFrame(results)
    print("\nParameter Sweep Results:\n")
    print(results_df)

    results_df.to_csv("results/parameter_sweep.csv", index=False)

if __name__ == "__main__":
    main()