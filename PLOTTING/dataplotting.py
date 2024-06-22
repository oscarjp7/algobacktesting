import matplotlib.pyplot as plt

def plot_means(data, signals):
    plt.plot(data['Close'], label = 'Close Price', color = 'blue')
    plt.plot(signals['short_mavg'], label = 'Short Moving Average', color = 'red')
    plt.plot(signals['long_mavg'], label = 'Long Moving Average', color = 'green')
    plt.title('Stock Price and Moving Averages')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc="best")
    plt.grid(True)
    plt.show()

def plot_performance(eval, data, init_capital):
    normalised_close = data['Close'] / data['Close'].iloc[0] * init_capital
    plt.plot(eval['total_value'], label = 'Portfolio Value')
    plt.plot(normalised_close, label = 'Adjusted Stock Price')
    plt.title('Strategy Performance')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend(loc='best')
    plt.show()
