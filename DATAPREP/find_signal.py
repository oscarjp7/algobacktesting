import pandas as pd
import numpy as np

def moving_average(data, short_window, long_window):
    signals = pd.DataFrame(index=data.index)
    signals['signal']= 0.0
    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    signals.loc[short_window:, 'signal'] = np.where(
        signals.loc[short_window:, 'short_mavg'] > signals.loc[short_window:, 'long_mavg'], 1.0, 0.0)
    signals['positions'] = signals['signal'].diff()
    return signals

def tema(data, short_window, long_window, medium_window):
    signals = pd.DataFrame(index=data.index)
    signals['buy_signal']= 0.0
    signals['sell_signal']= 0.0

    signals['short_mavg'] = data['Close'].rolling(window=short_window, min_periods=1, center=False).mean()
    signals['long_mavg'] = data['Close'].rolling(window=long_window, min_periods=1, center=False).mean()
    signals['med_mavg'] = data['Close'].rolling(window=medium_window, min_periods=1, center=False).mean()

    signals.loc[short_window:, 'buy_signal'] = np.where(
        (signals.loc[short_window:, 'short_mavg'] > signals.loc[short_window:, 'long_mavg']) &
        (signals.loc[short_window:, 'short_mavg'] > signals.loc[short_window:, 'med_mavg']),
        1.0, 0.0)
    signals.loc[short_window:, 'sell_signal'] = np.where(
        (signals.loc[short_window:, 'short_mavg'] < signals.loc[short_window:, 'long_mavg']) &
        (signals.loc[short_window:, 'short_mavg'] < signals.loc[short_window:, 'med_mavg']),
        1.0, 0.0)
    signals['positions'] = signals['buy_signal'] - signals['sell_signal']
    return signals
