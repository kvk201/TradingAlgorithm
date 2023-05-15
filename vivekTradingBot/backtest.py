from backtest import Backtest
from localMax import find_local_max
from localMin import find_local_min


def strategy(data):
    buy_signals = []
    sell_signals = []

    # Calculate local maxima and minima
    highs = data['high']
    lows = data['low']
    maxima = find_local_max(highs)
    minima = find_local_min(lows)

    # Generate buy and sell signals
    for i in range(len(maxima)):
        if i < len(minima):
            if maxima[i][0] > minima[i][0]:
                buy_signals.append(maxima[i][0])
            elif maxima[i][0] < minima[i][0]:
                sell_signals.append(minima[i][0])

    return buy_signals, sell_signals
