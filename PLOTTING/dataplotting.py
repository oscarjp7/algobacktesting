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

def plot_performance(eval):
    plt.plot(eval['total_value'])