import yfinance as yf
import pandas as pd

def get_historical_data(stock,period,interval):
    ticker = yf.Ticker(stock)
    ticker_df = ticker.history(period=period,interval=interval)
    ticker_df.index = pd.to_datetime(ticker_df.index)
    ticker_df.sort_index(inplace=True)
    print(ticker_df.columns)
    return ticker_df
