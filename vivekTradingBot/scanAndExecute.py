import robin_stocks.robinhood as r
from ta import * #Technical Analysis package
from plotData import *
from getPortfolioData import *
from historicalData import *
from executeTrade import *
from patterns import *
from indicators import *
from tradingStatistics import *
from config import *
import pandas as pd
import numpy as np
import ta as ta
from pandas.plotting import register_matplotlib_converters

# Robinhood Log in:
login = r.login(username,password)

# sell from portfolio if certain conditions are met
# buy from watchlist if certain conditions are met
# update tradehistory.txt after trade is executed + profit/loss info
def scanStocks_findTrade_execute():
    print("scanStocks_findTrade_execute()")

    if debug_mode: 
        print("============ DEBUG MODE ===============\n")
    else:

        print("=============== WARNING: EXECUTE MODE =================\n")
        print("------------ POTENTIAL TRADES WILL BE EXECUTED---------------\n")

    print("----- Scanning -----\n")
    register_matplotlib_converters()
    watchlist_symbols = get_watchlist_data()
    portfolio_symbols = get_portfolio_data()
    holdings_data = get_modified_holdings()
    holding = []
    holding.append('temp')
    potential_buys = []
    sells = []
    print("Current Portfolio: " + str(portfolio_symbols) + "\n")
    print("Current Watchlist: " + str(watchlist_symbols) + "\n")

    print("\n================ Scanning portfolio for stocks to sell ================\n")
    for symbol in portfolio_symbols:
        cross = golden_death_cross(symbol, n1=50, n2=200, days=30, direction="below")
        if(cross == -1):
            #this is the execute trade command, set it up after algorithm is complete
            #sell_holdings(symbol, holdings_data)       
            sells.append(symbol)
    profile_data = r.build_user_profile()


    print("\n================== Scanning watchlist to buy =====================\n")
    for symbol in watchlist_symbols:
        if(symbol not in portfolio_symbols):
            print("\nxxxxxxxxx=",symbol,"xxxxxxxxxxxxxxx\n")
            cross = golden_death_cross(symbol, n1=50, n2=200, days=10, direction="above")
            if(cross == 1):
                potential_buys.append(symbol)

    if(len(potential_buys) > 0):
        #this is the execute trade command, set it up after algorithm is complete
        # buy_holdings(potential_buys, profile_data, holdings_data)
        print("bought holdings in potential buys!!!")

    if(len(sells) > 0):
        update_trade_history(sells, holdings_data, "tradehistory.txt")
    print("=x=x=x=x=x=x=x=x=x= Scanning completed =x=x=x=x=x=x=x=x=x=\n")

    if debug_mode:
        print("=x=x=x=x=x=x=x=x=x= DEBUG MODE END =x=x=x=x=x=x=x=x=x=\n")

#execute the scan
scanStocks_findTrade_execute()
