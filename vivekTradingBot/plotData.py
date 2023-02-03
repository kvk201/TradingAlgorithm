import robin_stocks.robinhood as r
import matplotlib.ticker as plticker
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ta as ta


# Displays a chart of the price and indicators for a stock
def show_plot(price, firstIndicator, secondIndicator, dates, symbol="", label1="", label2=""):
    print("show_plot()")
    plt.figure(figsize=(10,5))
    plt.title(symbol)
    plt.plot(dates, price, label="Closing prices")
    print('plot')
    plt.plot(dates, firstIndicator, label=label1)
    plt.plot(dates, secondIndicator, label=label2)
    plt.yticks(np.arange(price.min(), price.max(), step=((price.max()-price.min())/15.0)))
    plt.legend()
    plt.show()

# Displays a pie chart of portfolio holdings
def get_equity_data():
    print("get_equity_data()")
    holdings_data = r.build_holdings()
    equity_data = {}
    for key, value in holdings_data.items():
        equity_data[key] = {}
        equity_data[key][name] = value.get('name')
        equity_data[key][percentage] = value.get("percentage")
        equity_data[key][type]
    fig1, ax1 = plt.subplots()
    ax1.pie(equities, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.show()
