import requests
import pandas as pd

#FED Data API
#Gets data on average Interest Rates on U.S. Treasury Securities
def get_fed_data(row_amt):
    baseUrl = 'https://api.fiscaldata.treasury.gov/services/api/fiscal_service'
    endpoint = '/v2/accounting/od/avg_interest_rates'
    #filter = '&filter=record_date:eq:2025-05-06'
    sort = '?sort=-record_date'
    format = '&format=json'
    pagination = '&page[number]=1&page[size]='+str(row_amt)
    #API = f'{baseUrl}{endpoint}{fields}{filter}{sort}{format}{pagination}'
    API = f'{baseUrl}{endpoint}{sort}{format}{pagination}'
    # Call API and load into a pandas dataframe
    response = requests.get(API)
    #raise for status if fails
    response.raise_for_status()
    data = response.json()
    #raise for status if fails
    response.raise_for_status() 
    return pd.DataFrame(data['data'])


# Call the function and print the result
if __name__ == "__main__":
    fed_data = get_fed_data(2)
    print(fed_data.head())
    # Save to CSV
    fed_data.to_csv('fed_data.csv', index=False)
    print("Data saved to fed_data.csv")