import numpy as np

def find_local_max(prices, window):
    ma = np.convolve(prices, np.ones(window) / window, mode='valid')
    maxima = np.where((prices > ma[:-1]) & (prices > ma[1:]))[0] + window//2
    return maxima
