from DATAPREP.dataretrieval import get_historical_data
from DATAPREP.database import load_data_sql, retrieve_close_data
from DATAPREP.find_signal import moving_average, tema
from DATAPREP.eval import evaluate_strat
from PLOTTING.dataplotting import plot_means, plot_performance

# Choose variables
stock = input('Ticker Name:')
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

# Choose strategy
print("Choose strategy:")
print('1. Moving Average')
print('2. Triple Exponential Moving Average')
choice = int(input('Enter: '))

# Get moving average signals
if choice == 1:
    short_moving_average = int(input("Enter short window: "))
    long_moving_average = int(input("Enter long window: "))
    print('Getting moving average signals')
    signals = moving_average(df, short_moving_average, long_moving_average)
    print('Done')

# Get triple moving average
if choice == 2:
    short_moving_average = int(input("Enter short window: "))
    med_moving_average = int(input("Enter medium window: "))
    long_moving_average = int(input("Enter long window: "))
    print('Getting triple exponential moving average signals')
    signals = tema(df, short_moving_average, long_moving_average, med_moving_average)
    print('Done')

# Evaluating strategy
print('Evaluating signals')
eval = evaluate_strat(df, signals, init_capital)
print('Done')

plot_means(df, signals)
plot_performance(eval, df, init_capital)
