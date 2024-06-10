from DATAPREP.dataretrieval import get_historical_data
from DATAPREP.database import load_data_sql

stock = 'AAPL'
period = '1mo'
interval = '1d'
test = get_historical_data(stock,period,interval)
load_data_sql(test)
print(test)
