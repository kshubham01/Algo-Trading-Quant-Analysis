import yfinance as yf
import datetime as dt
import pandas as pd

stocks = ["COALINDIA.NS", "HAL.NS", "GOOG", "MSFT", "AMZN"]

start = dt.datetime.today() - dt.timedelta(30)
end = dt.datetime.today()



