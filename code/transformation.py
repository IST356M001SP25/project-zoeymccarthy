import pandas as pd
import numpy as np
import datetime as dt
import api_calls as ac
import tool_functions as tf
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#uses the clean_stock_data function from tool_functions.py to clean the data and save it to a new csv file
'''
#aapl data
tf.clean_stock_data("AAPL")

#jpm data
tf.clean_stock_data("JPM")

#spy data
tf.clean_stock_data("SPY")

#xlre data
tf.clean_stock_data("XLRE")
'''

#gets all the rows in fed data that are after feb 2020 and contain "treasury_bonds" as the value under security_desc

#read the CSV file into a DataFrame
df = pd.read_csv("cache/fed_data.csv") 

#filter rows where 'security_desc' contains 'Treasury Bond' (case-insensitive)
df_filtered = df[df['security_desc'].str.contains('Treasury Bonds', case=False, na=False)]

#save the filtered DataFrame to a new CSV file
df_filtered.to_csv('cache/bond_rates.csv', index=False)

print("Filtered data saved to 'bond_rates.csv'.")


#shorten the stock data to only include post-covid data