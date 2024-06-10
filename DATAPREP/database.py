from sqlalchemy import create_engine
import os

path = f'{os.getcwd()}/raw_data/aapl_data.db'
engine = create_engine(f'sqlite:///{path}')

def load_data_sql(data):
    data.to_sql('appl_stock_data', con=engine, if_exists='append', index=False)
