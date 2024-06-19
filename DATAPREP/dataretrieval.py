import yfinance as yf
import pandas as pd

def get_historical_data(stock,period,interval):
    ticker = yf.Ticker(stock)
    ticker_df = ticker.history(period=period,interval=interval)
    ticker_df.reset_index(inplace=True)
    ticker_df['Date'] = pd.to_datetime(ticker_df['Date'])
    ticker_df.sort_index(inplace=True)
    ticker_df['symbol'] = stock.upper()
    return ticker_df
