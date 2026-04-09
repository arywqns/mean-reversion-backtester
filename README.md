# Mean Reversion Strategy Backtester

## Overview
This project implements and evaluates a mean reversion trading strategy under realistic assumptions, including transaction costs and parameter variation, to assess robustness.

## Motivation
I built this project to explore how systematic trading strategies behave in practice, with a focus on testing assumptions, evaluating robustness, and identifying failure modes rather than optimizing performance.

## Strategy
The strategy computes a rolling moving average and rolling standard deviation, and defines a z-score:

z = (price - moving average) / rolling standard deviation

- Go long when z-score < -1  
- Go short when z-score > 1  
- Stay flat otherwise  

This framework assumes that prices revert to their recent mean.

## Data
Historical daily price data is downloaded using `yfinance`.

Assets tested:
- SPY (S&P 500 ETF)

## Metrics
The backtest evaluates:
- total return  
- annualized return  
- volatility  
- Sharpe ratio  
- maximum drawdown

## Backtesting Methodology
- Signals are applied with a one-day lag to avoid look-ahead bias  
- Transaction costs are applied when positions change
- Returns are computed using close-to-close prices (no intraday execution modeling)

## Results

| Strategy          | Total Return | Annual Return | Sharpe | Max Drawdown |
|------------------|-------------|--------------|--------|--------------|
| Mean Reversion   | -53.3%      | -10.4%       | -0.69  | -55.3%       |
| Buy & Hold (SPY) | +132.9%     | +13.0%       | 0.67   | -33.7%       |

The mean reversion strategy significantly underperforms buy-and-hold on SPY and produces negative risk-adjusted returns.

After incorporating transaction costs, performance deteriorates further, indicating that the strategy relies heavily on frequent trading and small price movements.

These results highlight an important limitation: while mean reversion strategies may work in range-bound environments, they tend to fail in strongly trending markets such as SPY. The results indicate that the strategy’s failure is structural rather than due to parameter choice, and that naive mean reversion is not effective on SPY without additional constraints.

## Parameter Sensitivity Analysis

The strategy was evaluated across multiple parameter configurations:

- Lookback windows: 10, 20, 50 days  
- Z-score thresholds: 0.5, 1.0, 1.5  

Performance remains negative across all parameter combinations, suggesting that the strategy’s failure is structural rather than due to poor parameter selection.

More conservative configurations (longer lookback windows and higher thresholds) reduce trading frequency and improve results, indicating that overtrading and transaction costs are key drivers of underperformance.

Even in the best cases, the strategy fails to generate positive risk-adjusted returns, reinforcing the importance of incorporating additional filters or constraints.

## Trend Filter Experiment

To test whether the strategy’s underperformance was driven by trading against persistent trends, a trend filter based on a 50-day moving average was introduced.

- Long trades were only allowed when price was above the 50-day moving average  
- Short trades were only allowed when price was below the 50-day moving average  

This reduced the number of trades from 417 to 100 and significantly improved performance:

| Strategy | Total Return | Sharpe | Max Drawdown |
|----------|-------------|--------|--------------|
| Baseline | -53.3%      | -0.69  | -55.3%       |
| Filtered | -17.3%      | -0.51  | -19.8%       |

The trend filter significantly improves performance, reducing losses, drawdowns, and trading frequency. This suggests that a major source of underperformance was excessive trading and taking positions against persistent market trends.

However, the strategy remains unprofitable even after filtering, indicating that naive mean reversion is not a robust standalone strategy for SPY.

## Key Insights
- Transaction costs can eliminate apparent strategy edge  
- Strategy performance is highly sensitive to trading frequency  
- SPY exhibits strong trending behavior, making it unsuitable for naive mean reversion  

## Limitations
This implementation simplifies several real-world factors:
- fixed transaction cost assumption (no slippage modeling)
- no position sizing or risk management
- single-asset testing
- no out-of-sample validation

## Next Steps
Potential improvements include:
- testing across multiple asset classes (e.g., GLD, QQQ, USO)
- adding volatility or trend filters
- performing parameter sensitivity analysis
- incorporating more realistic transaction cost models