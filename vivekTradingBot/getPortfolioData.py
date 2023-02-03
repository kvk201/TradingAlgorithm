import robin_stocks.robinhood as r
from ta import * #Technical Analysis package
from plotData import *
from historicalData import *
from tradingStatistics import *
from config import *
import pandas as pd

# returns symbol for each stock in WATCHLIST as a list
def get_watchlist_data():

    my_list_names = set()
    symbols = set()
    
    holding = []
    holding.append('temp')
    
    watchlistInfo = r.get_all_watchlists()
    for watchlist in watchlistInfo['results']:
        listName = watchlist['display_name']
        my_list_names.add(listName)

    for listName in my_list_names:
        watchlist = r.get_watchlist_by_name(name=listName)
        for item in watchlist['results']:
            symbol = item['symbol']
            symbols.add(symbol)
    print("get_watchlist_data success")
    return symbols

# returns symbol for each stock in PORTFOLIO as a list
def get_portfolio_data():
    symbols = []
    holdings_data = r.get_open_stock_positions()
    for item in holdings_data:
        if not item:
            continue
        instrument_data = r.get_instrument_by_url(item.get('instrument'))
        symbol = instrument_data['symbol']
        symbols.append(symbol)
    print("get_portfolio_data success")
    return symbols

# returns date and time of purchase for each stock in PORTFOLIO
def get_position_open_date(symbol, holdings_data):

    instrument = r.get_instruments_by_symbols(symbol)
    url = instrument[0].get('url')
    for dict in holdings_data:
        if(dict.get('instrument') == url):
            print("get_position_open_date exists")
            return dict.get('created_at')         
    print("get_position_open_date does not exist")
    return "Not found"

# retrieves holdings data
# include, append purchase date
# returns r.build_holdings + time of purchase ('purchase_date')
def get_modified_holdings():
    
    holding = []
    holding.append('temp')
    holdings = r.build_holdings()
    holdings_data = r.get_open_stock_positions()
    for symbol, dict in holdings.items():
        purchase_date = get_position_open_date(symbol, holdings_data)
        purchase_date = str(pd.to_datetime(purchase_date))
        holdings[symbol].update({'purchase_date': purchase_date})
    print("get_modified_holdings success")
    return holdings