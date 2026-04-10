from src.data_loader import load_data
from src.signals import generate_signals
from src.momentum import generate_momentum_signals
from src.backtest import run_backtest
from src.metrics import compute_metrics

import pandas as pd

def print_metrics(title: str, metrics: dict) -> None:
    print(f"\n{title}")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

def main():
    ticker = "SPY"
    df = load_data(ticker=ticker)

    # Mean Reversion
    mr_df = generate_signals(df, window = 20, z_threshold = 1.0, use_trend_filter = False)
    mr_df = run_backtest(mr_df)
    mr_metrics = compute_metrics(mr_df["strategy_returns"])

    # Trend filited strategy
    tf_df = generate_signals(df, window = 20, z_threshold = 1.0, use_trend_filter = True, trend_window = 50)
    tf_df = run_backtest(tf_df)
    tf_metrics = compute_metrics(tf_df["strategy_returns"])

    # Momentum
    mom_df = generate_momentum_signals(df, window = 50)
    mom_df = run_backtest(mom_df)
    mom_metrics = compute_metrics(mom_df["returns"])

    # Buy and hold
    buy_hold_metrics = compute_metrics(mom_df["returns"])

    print(f"\nResults for {ticker}")
    print_metrics("Mean Reversion", mr_metrics)
    print_metrics("Trend-Filtered Mean Reversion", tf_metrics)
    print_metrics("Momentum", mom_metrics)
    print_metrics("Buy-and-Hold", buy_hold_metrics)

    summary = pd.DataFrame([
        {
            "strategy": "Mean Reversion",
            "total_return": mr_metrics["total_return"],
            "annualized_return": mr_metrics["annualized_return"],
            "volatility": mr_metrics["volatility"],
            "sharpe_ratio": mr_metrics["sharpe_ratio"],
            "max_drawdown": mr_metrics["max_drawdown"],
            "trades": mr_df["trades"].sum()
        },
        {
            "strategy": "Trend-Filtered Mean Reversion",
            "total_return": tf_metrics["total_return"],
            "annualized_return": tf_metrics["annualized_return"],
            "volatility": tf_metrics["volatility"],
            "sharpe_ratio": tf_metrics["sharpe_ratio"],
            "max_drawdown": tf_metrics["max_drawdown"],
            "trades": tf_df["trades"].sum()
        },
        {
            "strategy": "Momentum",
            "total_return": mom_metrics["total_return"],
            "annualized_return": mom_metrics["annualized_return"],
            "volatility": mom_metrics["volatility"],
            "sharpe_ratio": mom_metrics["sharpe_ratio"],
            "max_drawdown": mom_metrics["max_drawdown"],
            "trades": mom_df["trades"].sum()
        },
        {
            "strategy": "Buy and Hold",
            "total_return": buy_hold_metrics["total_return"],
            "annualized_return": buy_hold_metrics["annualized_return"],
            "volatility": buy_hold_metrics["volatility"],
            "sharpe_ratio": buy_hold_metrics["sharpe_ratio"],
            "max_drawdown": buy_hold_metrics["max_drawdown"],
            "trades": 0
        }
    ])

    print("\nSummary Table:\n")
    print(summary)

    summary.to_csv("results/strategy_comparison.csv", index=False)

if __name__ == "__main__":
    main()

