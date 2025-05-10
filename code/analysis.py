import pandas as pd
import numpy as np
import datetime as dt
import requests
import json
import api_calls as ac
import tool_functions as tf



#calls the api functions in api_functions.py and saves the data to csv files
    #gets the fed data on average Interest Rates on U.S. Treasury Securities
    fed_data = get_fed_data(1052)
    print(fed_data.head())
    # Save to CSV
    fed_data.to_csv('data/fed_data.csv', index=False)
    print("Data saved to fed_data.csv")
    

    #gets data on the S&p 500 index
    sp500_data = get_symbol_stock_data("GSPC")
    print(sp500_data.head())
    # Save to CSV
    stock_data.to_csv('data/raw_sp500_data.csv', index=True)
    print("Data saved to raw_sp500_data.csv")

    #gets apple stock data
    apple_data = get_symbol_stock_data("AAPL")
    print(apple_data.head())
    # Save to CSV
    stock_data.to_csv('data/raw_sp500_data.csv', index=True)
    print("Data saved to raw_sp500_data.csv")
