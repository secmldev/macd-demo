import pandas as pd
import pandas_datareader as web

def get_stock_csv(folder_name, symbol, index_col):
    """ 
    This is a method for reading stock data 
    Input Argument: 
    Folder name 
    Stock name 
    Column for indexing
    Output: 
    Stock data with date as index 
    """ 
    file_name = folder_name + "/" + symbol + ".csv" 
    data = pd.read_csv(file_name) 
    data[index_col] = pd.to_datetime(data[index_col]) 
    data = data.set_index(index_col)
    print("stock name: ", symbol) 
#     print("Stock data variables: ", data.columns) 
#     print(data.head()) 
    return data


def get_price_yahoo(symbol, data_source, start_date = "1/1/2010", end_date = "1/1/2011"):
    """
    Get stock data from yahoo
    Input Argument:
    Symbol name
    data source
    start date
    end date
    Output:
    Stock data with open, high, low, close, adj close price
    """
    data = web.DataReader(name = symbol, data_source = data_source, start = start_date, end = end_date)
    print("stock name: ", symbol) 
#     print("Stock data variables: ", data.columns) 
#     print(data.head()) 
    return data

