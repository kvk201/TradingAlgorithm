import robin_stocks.robinhood as r
from ta import * #Technical Analysis package
from plotData import *
from getPortfolioData import *
from historicalData import *
from executeTrade import *
from tradingStatistics import *
from config import *
import numpy as np
import pandas as pd

# historical volatality 
def historical_volatility(prices, window):
    returns = np.log(prices[1:] / prices[:-1])
    vol = np.sqrt(np.sum(np.square(returns - np.mean(returns))) / (len(returns) - 1))
    return vol * np.sqrt(window)


# relative strength index

def rsi(prices, window=14):
    deltas = np.diff(prices)
    seed = deltas[:window+1]
    up = seed[seed>=0].sum()/window
    down = -seed[seed<0].sum()/window
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:window] = 100. - 100./(1.+rs)

    for i in range(window, len(prices)):
        delta = deltas[i-1] 

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(window-1) + upval)/window
        down = (down*(window-1) + downval)/window
        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi


# moving average convergence divergence
def macd(prices, fast=12, slow=26, signal=9):
    
    exp1 = prices.ewm(span=fast, adjust=False).mean()
    exp2 = prices.ewm(span=slow, adjust=False).mean()
    macd = exp1 - exp2
    signal_line = macd.ewm(span=signal, adjust=False).mean()
    histogram = macd - signal_line
    return macd, signal_line, histogram

macd(55)