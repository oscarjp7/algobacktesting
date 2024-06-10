from sqlalchemy import create_engine

def load_data_sql(data):
    data.to_sql()
