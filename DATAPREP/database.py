from sqlalchemy import create_engine
import os
import pandas as pd

path = f'{os.getcwd()}/raw_data/stock_data.db'
engine = create_engine(f'sqlite:///{path}')

def load_data_sql(data):
    data.to_sql('stock_data_table', con=engine, if_exists='replace', index=False)

def add_data_sql(data):
    data.to_sql('stock_data_table', con=engine, if_exists='append', index=False)

def retrieve_close_data(stock):
    query = f"""
    SELECT date, close FROM stock_data_table
    WHERE symbol = '{stock.upper()}'
    ORDER BY date;
    """
    df = pd.read_sql(query, con = engine)
    return df
