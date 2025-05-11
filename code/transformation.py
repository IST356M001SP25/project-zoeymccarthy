import pandas as pd
import numpy as np
import datetime as dt
import api_calls as ac
import tool_functions as tf
import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

#uses the clean_stock_data function from tool_functions.py to clean the data and save it to a new csv file

#aapl data
tf.clean_stock_data("AAPL")

#jpm data
tf.clean_stock_data("JPM")

#spy data
tf.clean_stock_data("SPY")

#xlre data
tf.clean_stock_data("XLRE")
