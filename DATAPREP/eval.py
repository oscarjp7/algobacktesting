def evaluate_strat(data, signals, init_capital):
    data['signal']=signals['positions']
    data['daily_returns'] = data['Close'].pct_change()
    data['strat_return'] = data['daily_returns'] * data['signal'].shift()
    data['total_value'] = init_capital * (1+data['strat_return']).cumprod()
    return data
