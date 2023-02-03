import robin_stocks.robinhood as r
import json
import pandas as pd


# Reads data about the previous trades from a JSON file and prints it
def read_trade_history(file_name):
    print("read_trade_history()")
    with open(file_name) as json_file:
        data = json.load(json_file)
    for sell_date, event in data.items():
        print(sell_date + ": ")
        for symbol, dict in event.items():
            quantity, price, change, percent, purchase_date = str(int(float(dict.get("quantity")))), dict.get("price"), dict.get("equity_change"), dict.get("percent_change"), dict.get("purchase_date")
            print("\tSold " + quantity + " shares of "+ symbol + " at " + price + ", " + change + " (" +
                percent + "%) profit/loss, bought on " + purchase_date)

#  Writes data about a trade to a JSON file, containing the sell date, buy date, buy price sell price, etc.
def update_trade_history(symbols, holdings_data, file_name):
    print("update_trade_history()")

    with open(file_name) as json_file:
        data = json.load(json_file)
    current_time = str(pd.Timestamp("now"))
    data[current_time] = ({})
    for symbol in symbols:
        data[current_time].update({symbol: holdings_data[symbol]})
    with open(file_name, 'w') as outfile:
        json.dump(data, outfile)


# Returns the amount of money you've gained/lost through trading since the creation of your account, minus dividends
def get_total_gains_minus_dividends():
    print("get_total_gains_minus_dividends()")

    
    holding = []
    holding.append('temp')
    
    profileData = r.load_portfolio_profile()
    print(profileData)
    allTransactions = r.get_bank_transfers()
    deposits = sum(float(x['amount']) for x in allTransactions if (x['direction'] == 'deposit')) # and (x['state'] == 'completed'))
    withdrawals = sum(float(x['amount']) for x in allTransactions if (x['direction'] == 'withdraw') and (x['state'] == 'completed'))

    money_invested = deposits - withdrawals
    print(deposits)
    dividends = r.get_total_dividends()
    percentDividend = dividends/money_invested*100
    totalGainMinusDividends =float(profileData['extended_hours_equity'])-dividends-money_invested
    return totalGainMinusDividends
