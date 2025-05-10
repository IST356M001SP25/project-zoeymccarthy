import requests
import pandas as pd
import json
import numpy as np

#FED Data API
#Gets data on average Interest Rates on U.S. Treasury Securities
def get_fed_data(row_amt):
    base_url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'
    endpoint = '/v2/accounting/od/avg_interest_rates'
    #filter = '&filter=record_date:eq:2025-05-06'
    sort = '?sort=-record_date'
    format = '&format=json'
    pagination = '&page[number]=1&page[size]='+str(row_amt)
    #API = f'{baseUrl}{endpoint}{fields}{filter}{sort}{format}{pagination}'
    API = f'{base_url}{endpoint}{sort}{format}{pagination}'
    # Call API and load into a pandas dataframe
    response = requests.get(API)
    #raise for status if fails
    response.raise_for_status()
    data = response.json()
    #raise for status if fails
    response.raise_for_status() 
    return pd.DataFrame(data['data'])

def get_symbol_stock_data(symbol):
    base_url = "https://www.alphavantage.co/query?"
    func = "function=TIME_SERIES_WEEKLY_ADJUSTED"
    sort = "&sort=asc"
    symbol = "&symbol=" + symbol
    apikey = "&apikey=KNRVCWZ5R9ZZEXXE"
    API = f"{base_url}{func}{symbol}{apikey}"
    # Call API and load into a pandas dataframe
    response = requests.get(API)
    #raise for status if fails
    response.raise_for_status()
    data = response.json()
    #Extract / convert the "Weekly Adjusted Time Series" part
    weekly_data = data["Weekly Adjusted Time Series"]
    #convert to DataFrame
    df = pd.DataFrame.from_dict(weekly_data, orient='index')
    #rename columns for readability
    df.columns = [
        "open", "high", "low", "close",
        "adjusted_close", "volume", "dividend_amount" ]
    #convert data types
    df = df.astype({
        "open": float,
        "high": float,
        "low": float,
        "close": float,
        "adjusted_close": float,
        "volume": int,
        "dividend_amount": float
    })
    #convert index to datetime
    df.index = pd.to_datetime(df.index)
    return df

# Call the function and print the result
if __name__ == "__main__":
    '''
    fed_data = get_fed_data(2)
    print(fed_data.head())
    # Save to CSV
    fed_data.to_csv('fed_data.csv', index=False)
    print("Data saved to fed_data.csv")'''
    stock_data = get_symbol_stock_data("IBM")
    print(stock_data.head())
    # Save to CSV
    stock_data.to_csv('stock_data.csv', index=False)
    print("Data saved to stock_data.csv")