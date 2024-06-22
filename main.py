from DATAPREP.dataretrieval import get_historical_data
from DATAPREP.database import load_data_sql, retrieve_close_data
from DATAPREP.find_signal import moving_average
from DATAPREP.eval import evaluate_strat
from PLOTTING.dataplotting import plot_means, plot_performance

# Choose variables
stock = 'MSFT'
short_moving_average = 5
long_moving_average = 10
init_capital = 100

# Get historical data for stock over given period
period = '1y'
interval = '1d'
print('Getting data')
stock_data = get_historical_data(stock,period,interval)
print('Done')

# Add data to sql database
print('Load into sql db')
load_data_sql(stock_data)
print('Done')

# Pull data from database into df
print('Pull from database')
df = retrieve_close_data(stock)
print('Done')

# Get moving average signals
print('Getting moving average signals')
ma_signals = moving_average(df, short_moving_average, long_moving_average)
print('Done')

# Evaluating strategy
print('Evaluating signals')
eval = evaluate_strat(df, ma_signals, init_capital)
print('Done')

plot_means(df, ma_signals)
plot_performance(eval, df, init_capital)
