from src.data_loader import load_data
from src.signals import generate_signals
from src.backtest import run_backtest
from src.metrics import compute_metrics
from src.plot import plot_equity_curves

def main():
    ticker = "SPY"

    df = load_data(ticker = ticker, start = "2018-01-01", end = "2025-01-01")
    df = generate_signals(df, window = 20, z_threshold = 1.0)
    df = run_backtest(df)

    strategy_metrics = compute_metrics(df["strategy_returns"])
    buy_hold_metrics = compute_metrics(df["returns"])

    print(f"\nResults for {ticker}\n")

    print("Strategy Metrics:")
    for key, value in strategy_metrics.items():
        print(f"{key}: {value:.4f}")

    print("\nBuy-and-Hold Metrics:")
    for key, value in buy_hold_metrics.items():
        print(f"{key}: {value:.4f}")
    
    plot_equity_curves(df)

if __name__ == "__main__":
    main()

