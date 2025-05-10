import pandas as pd
import numpy as np
import datetime as dt
import requests

def clean_stock_data(df):
    #rename columns for readability
    df.columns = [
        "date","open", "high", "low", "close",
        "adjusted_close", "volume", "dividend_amount"
    ]
    #convert "date" column to datetime
    df["date"] = pd.to_datetime(df["date"])
    #convert the other data types
    df["open"] = pd.to_numeric(df["open"], errors='coerce')
    df["high"] = pd.to_numeric(df["high"], errors='coerce')
    df["low"] = pd.to_numeric(df["low"], errors='coerce')
    df["close"] = pd.to_numeric(df["close"], errors='coerce')
    df["adjusted_close"] = pd.to_numeric(df["adjusted_close"], errors='coerce')
    df["volume"] = pd.to_numeric(df["volume"], errors='coerce', downcast='integer')
    df["dividend_amount"] = pd.to_numeric(df["dividend_amount"], errors='coerce')
    return df

if __name__ == "__main__":
    df = pd.read_csv("data/raw_stock_data.csv")
    df = clean_stock_data(df)
    df.to_csv('data/cleaned_stock_data.csv', index=False)
    print("Data saved to cleaned_stock_data.csv")