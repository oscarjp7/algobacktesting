from DATAPREP.dataretrieval import get_historical_data
from DATAPREP.database import load_data_sql, retrieve_close_data
from DATAPREP.find_signal import moving_average
from DATAPREP.eval import evaluate_strat
from PLOTTING.dataplotting import plot_means

# Get historical data for stock over given period
print('Getting data')
stock = 'AAPL'
period = '1y'
interval = '1d'
aapl_data = get_historical_data(stock,period,interval)
print('Done')

# Add data to sql database
print('Load into sql db')
load_data_sql(aapl_data)
print('Done')

# Pull data from database into df
print('Pull from database')
df = retrieve_close_data('aapl')
print('Done')

# Get moving average signals
print('Getting moving average signals')
ma_signals = moving_average(df, 10, 20)
print('Done')

# Evaluating strategy
print('Evaluating signals')
eval = evaluate_strat(df, ma_signals, 100)
print('Done')

plot_means(df, ma_signals)
