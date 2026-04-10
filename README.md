# Mean Reversion & Momentum Strategy Backtester

## Overview

This project implements and evaluates systematic trading strategies on historical market data to analyze how different assumptions about price behavior impact performance. The goal is to test whether markets exhibit mean reversion or momentum and assess the robustness of simple rule-based strategies under realistic conditions.

## Motivation

I built this project to understand how quantitative trading strategies are designed, backtested, and evaluated. Rather than optimizing for performance, the focus is on testing hypotheses, identifying limitations, and explaining why strategies succeed or fail.

## Strategies

### Mean Reversion

The mean reversion strategy computes a rolling moving average and standard deviation, then defines a z-score:

z = (price − moving average) / rolling standard deviation

* Long when z-score < -1
* Short when z-score > 1
* Flat otherwise

This assumes prices revert to their recent average.

---

### Trend-Filtered Mean Reversion

To avoid trading against persistent trends, a trend filter is introduced:

* Long trades allowed only when price is above the 50-day moving average
* Short trades allowed only when price is below the 50-day moving average

---

### Momentum

A momentum strategy is implemented using a moving average rule with a threshold:

* Long when price is more than 1% above the 50-day moving average
* Short when price is more than 1% below the 50-day moving average

Positions are held until a new signal is generated to reduce noise and overtrading.

---

## Data

Historical daily price data is downloaded using `yfinance`.

Assets tested:

* SPY (S&P 500 ETF)

## Backtesting Methodology

* Signals are applied with a one-day lag to avoid look-ahead bias
* Transaction costs are applied when positions change
* Strategies are evaluated on total return, annualized return, volatility, Sharpe ratio, and maximum drawdown

---

## Results

| Strategy                      | Total Return | Annual Return | Sharpe | Max Drawdown | Trades |
| ----------------------------- | ------------ | ------------- | ------ | ------------ | ------ |
| Mean Reversion                | -53.3%       | -10.4%        | -0.69  | -55.3%       | 417    |
| Trend-Filtered Mean Reversion | -17.3%       | -2.7%         | -0.51  | -19.8%       | 100    |
| Momentum                      | +138.4%      | +13.7%        | 0.70   | -33.7%       | 87     |
| Buy & Hold (SPY)              | +138.4%      | +13.7%        | 0.70   | -33.7%       | 0      |

---

## Autocorrelation Analysis

To evaluate whether mean reversion is present in SPY, the autocorrelation of daily returns was computed.

* Autocorrelation (lag 1): -0.1356

This indicates mild mean-reverting behavior in returns. However, the signal is weak and not sufficient to produce profitable trading after accounting for transaction costs and noise.

---

## Key Insights

* **Mean reversion strategies perform poorly on SPY**, even after filtering, due to strong market trends
* **Transaction costs and overtrading significantly reduce performance**
* **Momentum strategies produce positive returns**, but largely replicate buy-and-hold performance
* **SPY exhibits strong upward drift**, causing simple momentum rules to maintain long exposure
* **The presence of a statistical signal does not imply profitability**
* **Strategy performance depends heavily on underlying market structure**

---

## Limitations

This implementation simplifies several real-world factors:

* Fixed transaction cost assumption (no slippage modeling)
* No position sizing or portfolio construction
* Single-asset analysis
* No out-of-sample validation

---

## Next Steps

Potential extensions include:

* Testing across multiple asset classes (e.g., QQQ, GLD, commodities)
* Incorporating volatility or regime filters
* Performing out-of-sample validation
* Exploring cross-sectional strategies across multiple assets

---

## Conclusion

This project demonstrates that simple trading strategies are highly sensitive to market structure. While mean reversion fails in trending markets like SPY, naive momentum strategies collapse into buy-and-hold behavior. These results highlight the importance of aligning strategy design with underlying market dynamics rather than relying on isolated statistical signals.
