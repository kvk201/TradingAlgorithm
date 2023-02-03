# vivekTradingBot
Trading Algorithm and software
This algorithm will have a combination of two algorithms which help us reduce our risk and increase our profit compared to the traditional buy and hold strategy. 

Our algorithms operate on some of the technical stock market principles. These can be analyzed using data science as the consolidation and breakout principle which basically states that majority of the movement in a stock occurs during a short breakout period after a long consolidation period. The proposed two algorithms will use this to maximize the profits for blue chip stocks such as Facebook, Amazon, Netflix, Google, etc. 

The first algorithm will try to catch multiple stock breakouts while minimizing the time spend sitting in a stock during consolidation phase. The idea is to switch the stocks depending on certain parameters, indicator, and price data. This will utilize a lot of data science being done on past and real-time data.

The second algorithm will try to compound the stocks while in accumulation phase by trying to catch smaller upward movements based on certain parameters, conditions, and price data and then compounding these smaller movements several times. We will utilize data science to extract information, search for indicators and conditions and make an informed decision to buy, and then sell when a certain parameter, indicator or condition is reached.

Using APIs provided by Robinhood, Fidelity, Acorns or similar Brokerage platforms, will provide access to the market. The data from the API will be used for parameters. Indicators, etc and also be fed into the algorithms to make informed decisions about entries and exits for a stock.

Using historical stock market data to back-test our algorithm and software. We will use this data to calibrate our model and algorithm for a better output.


# packages required
pandas
robin-stocks
ta
matplotlib
numpy

# robinhood credentials
use config.py file for username and password

# This algorithm/software (python based) will have a combination of two algorithms (one conservative, one aggressive) to reduce  risk and increase profit compared to the traditional buy and hold strategy for blue chip stocks as well as Automated Investing and Switching based on parameters and conditions(data science involved). Additionally, there is Machine Learning based Calibration and heavy Backtesting to validate the algorithm.