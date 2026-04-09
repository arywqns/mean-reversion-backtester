# Mean Reversion Backtester

## Overview
This project tests a simple mean reversion trading strategy on historical price data using Python.

## Motivation
I built this project to better understand how rule-based trading strategies are designed, tested, and evaluated on real market data.

## Strategy
The strategy computes a rolling moving average and rolling standard deviation, then calculates a z-score:

z = (price - moving average) / rolling standard deviation

- Go long when z-score < -1
- Go short when z-score > 1
- Stay flat otherwise

## Data
Historical daily price data is downloaded using `yfinance`.

Example ticker tested:
- SPY

## Metrics
The backtest evaluates:
- total return
- annualized return
- volatility
- Sharpe ratio
- max drawdown

## Results
The strategy can perform better in range-bound conditions but tends to struggle during strong trends. This suggests mean reversion may be sensitive to market regime.

## Limitations
This project does not include:
- transaction costs
- slippage
- position sizing rules
- production-level execution assumptions

## Next Steps
Potential improvements:
- add transaction costs
- test multiple tickers
- add volatility filters
- compare parameter choices