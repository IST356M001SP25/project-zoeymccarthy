import pandas as pd
import numpy as np
import datetime as dt
import requests
import json
import api_calls as ac
import tool_functions as tf
import streamlit as st

#calls the api functions in api_functions.py and saves the data to csv files

#gets the fed data on average Interest Rates on U.S. Treasury Securities since covid began (end of feb 2020)

fed_data = ac.get_fed_data(1052)
print(fed_data.head())
# Save to CSV
fed_data.to_csv('cache/fed_data.csv', index=False)
print("Data saved to fed_data.csv")
    
#gets data on the S&p 500 index
tf.call_stock_data_api("SPY")

#gets apple stock data
tf.call_stock_data_api("AAPL")

#gets real estate sector data
tf.call_stock_data_api("XLRE")

#gets jp morgan stock data
tf.call_stock_data_api("JPM")


