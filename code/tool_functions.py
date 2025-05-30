import pandas as pd
import numpy as np
import datetime as dt
import requests
import api_calls as ac

def clean_stock_data(symbol):
    lower_symbol = symbol.lower()
    raw_csv_name = f"cache/raw_{lower_symbol}_data.csv"
    df = pd.read_csv(raw_csv_name)
    #rename columns for readability
    df.columns = [
        "date", "open", "high", "low", "close",
        "adjusted_close", "volume", "dividend_amount"]
    #convert "date" column to datetime
    df["date"] = pd.to_datetime(df["date"], errors='coerce')
    #convert the other data types
    df["open"] = pd.to_numeric(df["open"], errors='coerce')
    df["high"] = pd.to_numeric(df["high"], errors='coerce')
    df["low"] = pd.to_numeric(df["low"], errors='coerce')
    df["close"] = pd.to_numeric(df["close"], errors='coerce')
    df["adjusted_close"] = pd.to_numeric(df["adjusted_close"], errors='coerce')
    df["volume"] = pd.to_numeric(df["volume"], errors='coerce', downcast='integer')
    df.drop(columns=["dividend_amount"], inplace=True)
    #drop any pre-covid rows
    df_filtered = df[df["date"] >= pd.to_datetime('2020-02-28')]
    #saves the cleaned data to a new csv file
    df_filtered.to_csv(f'cache/cleaned_{lower_symbol}_data.csv', index=False)
    print(f"Data saved to cache/cleaned_{lower_symbol}_data.csv")


def call_stock_data_api(symbol):
    lower_symbol = symbol.lower()
    stock_data = ac.get_symbol_stock_data(symbol)
    #print out the first 5 rows of the data
    print(stock_data.head())
    # Save to CSV
    csv_name = f"cache/raw_{lower_symbol}_data.csv"
    stock_data.to_csv(csv_name, index=True)
    print(f"Data saved to {csv_name}")

if __name__ == "__main__":
    pass