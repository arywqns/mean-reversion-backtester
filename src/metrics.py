import pandas as pd
import numpy as np

def compute_metrics(returns: pd.Series) -> dict:
    #Compute common backtest performance metrics

    returns = returns.dropna()

    total_return = (1 + returns).prod() - 1
    annualized_return = (1 + total_return) ** (252 / len(returns)) - 1
    volatility = returns.std() * np.sqrt(252)

    if volatility == 0:
        sharpe = np.nan
    else:
        sharpe = annualized_return / volatility
    
    equity_curve = (1 + returns).cumprod()
    running_max = equity_curve.cummax()
    drawdown = (equity_curve - running_max) / running_max
    max_drawdown = drawdown.min()

    return{
        "total return": total_return,
        "annualized return": annualized_return,
        "volatility": volatility,
        "sharpe ratio": sharpe,
        "max drawdown": max_drawdown
    }