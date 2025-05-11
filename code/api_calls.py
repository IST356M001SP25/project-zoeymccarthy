import requests
import pandas as pd
import json
import numpy as np
import datetime as dt
import tool_functions as tf

#FED Data API
#Gets data on average Interest Rates on U.S. Treasury Securities
def get_fed_data(row_amt):
    base_url = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'
    endpoint = '/v2/accounting/od/avg_interest_rates'
    #filter = '&filter=record_date:eq:2025-05-06'
    sort = '?sort=-record_date'
    format = '&format=json'
    pagination = '&page[number]=1&page[size]='+str(row_amt)
    API = f'{base_url}{endpoint}{sort}{format}{pagination}'
    # Call API and load into a pandas dataframe
    response = requests.get(API)
    #raise for status if fails
    response.raise_for_status()
    data = response.json()
    #raise for status if fails
    response.raise_for_status() 
    return pd.DataFrame(data['data'])

#Symbol Stock Data API
#Gets data on weekly adjusted time series for a given stock symbol using Alpha Vantage API
#Note: I  included my API key in the code; the API only allows 25 calls per API key per day
def get_symbol_stock_data(symbol):
    base_url = "https://www.alphavantage.co/query?"
    func = "function=TIME_SERIES_MONTHLY_ADJUSTED"
    sort = "&sort=asc"
    link_symbol = "&symbol=" + symbol
    apikey = "&apikey=KNRVCWZ5R9ZZEXXE"
    #data_type = "&datatype=csv"
    API = f"{base_url}{func}{link_symbol}{apikey}"
    # Call API and load into a pandas dataframe
    response = requests.get(API)
    #raise for status if fails
    response.raise_for_status()
    data = response.json()
    #Extract / convert the "Monthly Adjusted Time Series" part
    monthly_data = data["Monthly Adjusted Time Series"]
    #convert to DataFrame
    df = pd.DataFrame.from_dict(monthly_data, orient='index')
    return df


if __name__ == "__main__":
    # Call the function and print the result
    fed_data = get_fed_data(1052)
    print(fed_data.head())
    # Save to CSV
    fed_data.to_csv('cache/fed_data.csv', index=False)
    print("Data saved to fed_data.csv")

    #gets data on the S&p 500 index
    #tf.call_stock_data_api("AAPL")