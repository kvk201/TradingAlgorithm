import robin_stocks.robinhood as r
from ta import * #Technical Analysis package
from plotData import *
from getPortfolioData import *
from historicalData import *
from tradingStatistics import *
from config import *


#Safe divide by zero division function
def safe_division(n, d):
    return n / d if d else 0

#place sell order for all holdings of a particular stock owned
def sell_holdings(symbol, holdings_data):
    print("sell_holdings()")

    shares_owned = int(float(holdings_data[symbol].get("quantity")))
    if not debug_mode:       #added debug_mode mode to protect from trade execution while building algorithm
        r.order_sell_market(symbol, shares_owned)
    print("####### Selling " , str(shares_owned) , " shares!! : " , symbol , " #######")

    """ 
        We will try to order an appropriate amount of shares such that your holdings of the stock will
        roughly match the average for the rest of your portfoilio. If the share price is too high considering the rest of your holdings and the amount of
        buying power in your account, it will not order any shares.
    """
def buy_holdings(potential_buys, profile_data, holdings_data):
    print("buy holdings()")
    
    cash = float(profile_data.get('cash'))
    portfolio_value = float(profile_data.get('equity')) - cash
    ideal_position_size = (safe_division(portfolio_value, len(holdings_data))+cash/len(potential_buys))/(2 * len(potential_buys))
    prices = r.get_latest_price(potential_buys)
    
    holding = []
    holding.append('temp')

    for i in range(0, len(potential_buys)):
        stock_price = float(prices[i])
        if(ideal_position_size < stock_price < ideal_position_size*1.5):
            num_shares = int(ideal_position_size*1.5/stock_price)
        elif (stock_price < ideal_position_size):
            num_shares = int(ideal_position_size/stock_price)
        else:
            print("####### Tried buying shares of " , potential_buys[i] , ", but not enough buying power!! #######")
            break
        print("####### Buying " , str(num_shares) , " shares of: " , potential_buys[i] , " #######")
        if not debug_mode:
            r.order_buy_market(potential_buys[i], num_shares)