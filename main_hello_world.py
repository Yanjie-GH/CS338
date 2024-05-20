import pandas as pd

def read_data():
    df = pd.read_csv('VET.csv')
    return df

def show_data(df):
    print(df)
