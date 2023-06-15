import robin_stocks.robinhood as r
from ta import * #Technical Analysis package
from plotData import *
from tradingStatistics import *
from config import *

# retrieves historical data for a particular stock during a particular time
def get_historical_data(ticker, intervalArg, spanArg, boundsArg):
    history = r.get_stock_historicals(ticker,interval=intervalArg,span=spanArg,bounds=boundsArg)

    #If it's not a stock ticker, try as a crypto ticker
    if(history is None or None in history):
        history = r.get_crypto_historicals(ticker,interval=intervalArg,span=spanArg,bounds=boundsArg)
    print("get_historical_data success")
    return history




