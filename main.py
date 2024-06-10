from DATAPREP.dataretrieval import get_historical_data

stock = 'AAPL'
period = '1mo'
interval = '1d'
test = get_historical_data(stock,period,interval)
print(test)
