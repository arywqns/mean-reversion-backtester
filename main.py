from src.data_loader import load_data
from src.signals import generate_signals
from src.backtest import run_backtest
from src.metrics import compute_metrics
from src.plot import plot_equity_curves


def main():
    ticker = "SPY"
    df = load_data(ticker = ticker)

    # Baseline strategy
    baseline_df = generate_signals(df, window = 20, z_threshold = 1.0, use_trend_filter = False)
    baseline_df = run_backtest(baseline_df)
    baseline_metrics = compute_metrics(baseline_df["strategy_returns"])

    # Trend filited strategy
    filtered_df = generate_signals(df, window = 20, z_threshold = 1.0, use_trend_filter = True, trend_window = 50)
    filtered_df = run_backtest(filtered_df)
    filtered_metrics = compute_metrics(filtered_df["strategy_returns"])

    # Buy and Hold
    buy_hold_metrics = compute_metrics(filtered_df["returns"])

    print(f"\nResults for {ticker}\n")

    print("Baseline Mean Reversion:")
    for key, value in baseline_metrics.items():
        print(f"{key}: {value:.4f}")

    print("\nTrend-Filtered Mean Reversion:")
    for key, value in filtered_metrics.items():
        print(f"{key}: {value:.4f}")

    print("\nBuy-and-Hold:")
    for key, value in buy_hold_metrics.items():
        print(f"{key}: {value:.4f}")

    print("\nBaseline number of trades:", baseline_df["trades"].sum())
    print("Trend-filtered number of trades:", filtered_df["trades"].sum())
    
    plot_equity_curves(baseline_df, output_path="results/baseline_equity_curve.png")
    plot_equity_curves(filtered_df, output_path="results/trend_filtered_equity_curve.png")

if __name__ == "__main__":
    main()