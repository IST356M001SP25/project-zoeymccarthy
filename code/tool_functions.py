import pandas as pd
import numpy as np
import datetime as dt
import requests

def clean_stock_data(df):
    #rename columns for readability
    df.columns = [
        "date","open", "high", "low", "close",
        "adjusted_close", "volume", "dividend_amount"]
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

def call_stock_data_api(symbol):
    lower_symbol = symbol.lower()
    stock_data = ac.get_symbol_stock_data(symbol)
    #print out the first 5 rows of the data
    print(stock_data.head())
    # Save to CSV
    csv_name = f"data/raw_{lower_symbol}_data.csv"
    stock_data.to_csv(csv_name, index=True)
    print(f"Data saved to {csv_name}")

if __name__ == "__main__":
    df = pd.read_csv("data/raw_stock_data.csv")
    df = clean_stock_data(df)
    df.to_csv('data/cleaned_stock_data.csv', index=False)
    print("Data saved to cleaned_stock_data.csv")