def evaluate_strat(data, signals, init_capital):
    data['signal'] = signals['positions']
    data['daily_returns'] = data['Close'].pct_change()
    data['strat_return'] = 0.0
    data['total_value'] = float(init_capital)

    buysell = 0
    for i in range(1,len(data)):
        if data.loc[i-1, 'signal'] == 1:
            buysell = 1
        elif data.loc[i-1, 'signal'] == -1:
            buysell = 0

        data.loc[i, 'strat_return'] = data.loc[i, 'daily_returns'] * buysell
        data.loc[i, 'total_value'] = data.loc[i-1, 'total_value'] * (1 + data.loc[i, 'strat_return'])

    return data
