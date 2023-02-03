import robin_stocks.robinhood as r
from ta import * #Technical Analysis package
from plotData import *
from getPortfolioData import *
from historicalData import *
from executeTrade import *
from tradingStatistics import *
from config import *
import pandas as pd
import numpy as np
import ta as ta


# Determine if a golden/death cross has occured for a specified stock in the last X trading days
# A golden cross suggests a long-term bull market going forward, while a death cross suggests a long-term bear market.
# The golden cross occurs when a short-term moving average crosses over a major long-term moving average to the upside
# The death cross occurs when a short-term moving average crosses over a major long-term moving average to the downside
""".
    Return:
        1 if the short-term indicator crosses above the long-term one
        0 if there is no cross between the indicators
        -1 if the short-term indicator crosses below the long-term one
        False if direction == "above" and five_year_check(stockTicker) returns False : stock fundamental issues
"""
def golden_death_cross(stockTicker, n1, n2, days, direction=""):
    print("golden_death_cross()")
    
    if(direction == "above" and not five_year_check(stockTicker)):
        return False
    
    history = get_historical_data(stockTicker, "day", "year", "regular")

    #Couldn't get pricing data
    if(history is None or None in history):
        return False
    
    closingPrices = []
    dates = []
    for item in history:
        closingPrices.append(float(item['close_price']))
        dates.append(item['begins_at'])
    price = pd.Series(closingPrices)
    dates = pd.Series(dates)
    dates = pd.to_datetime(dates)
    sma1 = ta.volatility.bollinger_mavg(price, int(n1), False)
    sma2 = ta.volatility.bollinger_mavg(price, int(n2), False)
    series = [price.rename("Price"), sma1.rename("Indicator1"), sma2.rename("Indicator2"), dates.rename("Dates")]
    df = pd.concat(series, axis=1)
    cross = get_last_crossing(df, days, symbol=stockTicker, direction=direction)
    
    if(cross) and plot:
        show_plot(price, sma1, sma2, dates, symbol=stockTicker, label1=str(n1)+" day SMA", label2=str(n2)+" day SMA")
    return cross


# Searches for a crossing between two indicators for a given stock
# df(pandas.core.frame.DataFrame): Dataframe -pandas, with columns containing the stock's prices, both indicators, and the dates
# direction(str): "above" if we are searching for an upwards cross, "below" if we are searching for a downwaords cross
# Returns: 1 if the short-term indicator crosses above the long-term one, 0 if there is no cross, -1 if the short-term indicator crosses below the long-term one.
def get_last_crossing(df, days, symbol="", direction=""):
    print("get_last_crossing()")
    
    prices = df.loc[:,"Price"]
    shortTerm = df.loc[:,"Indicator1"]
    LongTerm = df.loc[:,"Indicator2"]
    dates = df.loc[:,"Dates"]
    lastIndex = prices.size - 1
    index = lastIndex
    found = index
    recentDiff = (shortTerm.at[index] - LongTerm.at[index]) >= 0
    if((direction == "above" and not recentDiff) or (direction == "below" and recentDiff)):
        return 0
    index -= 1
    while(index >= 0 and found == lastIndex and not np.isnan(shortTerm.at[index]) and not np.isnan(LongTerm.at[index]) \
                        and ((pd.Timestamp("now", tz='UTC') - dates.at[index]) <= pd.Timedelta(str(days) + " days"))):
        if(recentDiff):
            if((shortTerm.at[index] - LongTerm.at[index]) < 0):
                found = index
        else:
            if((shortTerm.at[index] - LongTerm.at[index]) > 0):
                found = index
        index -= 1
    if(found != lastIndex):
        if((direction == "above" and recentDiff) or (direction == "below" and not recentDiff)):
            print(symbol + ": Short SMA crossed" + (" ABOVE " if recentDiff else " BELOW ") + "Long SMA at " + str(dates.at[found]) \
                +", which was " + str(pd.Timestamp("now", tz='UTC') - dates.at[found]) + " ago", ", price at cross: " + str(prices.at[found]) \
                + ", current price: " + str(prices.at[lastIndex]))
        return (1 if recentDiff else -1)
    else:
        return 0


# Figure out if a stock has risen or been created within the last five years.
# returns true if stock price is greater now than 5 years ago, or is IPO within last 5 years
def five_year_check(stockTicker):
    print("five_year_check()")

    instrument = r.get_instruments_by_symbols(stockTicker)
    if(instrument is None or len(instrument) == 0):
        return True
    list_date = instrument[0].get("list_date")
    if ((pd.Timestamp("now") - pd.to_datetime(list_date)) < pd.Timedelta("5 Y")):
        return True
    fiveyear =  get_historical_data(stockTicker, "day", "5year", "regular")
    if (fiveyear is None or None in fiveyear):
        return True
    closingPrices = []
    for item in fiveyear:
        closingPrices.append(float(item['close_price']))
    recent_price = closingPrices[len(closingPrices) - 1]
    oldest_price = closingPrices[0]
    return (recent_price > oldest_price)

