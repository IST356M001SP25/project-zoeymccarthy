import pandas as pd
import api_calls as ac
import tool_functions as tf
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

#step 1: load bond yield data
bonds = pd.read_csv("cache/bond_rates.csv")

#keep only relevant columns
bonds = bonds[['record_date', 'avg_interest_rate_amt']].rename(columns={
    'record_date': 'date', 
    'avg_interest_rate_amt': 'bond_yield'})

#calculate month-over-month yield change
bonds['bond_yield_change'] = bonds['bond_yield'].diff()

#step 2: load and process stock data (e.g. for AAPL)
def load_stock_data(file_path, symbol):
    df = pd.read_csv(file_path)
    df['return'] = df['adjusted_close'].pct_change()
    df['ticker'] = symbol
    return df[['date', 'adjusted_close', 'return', 'ticker']]

#load all stock data
aapl = load_stock_data("cache/cleaned_aapl_data.csv", "AAPL")
xlre = load_stock_data("cache/cleaned_xlre_data.csv", "XLRE")
spy  = load_stock_data("cache/cleaned_spy_data.csv", "SPY")
jpm  = load_stock_data("cache/cleaned_jpm_data.csv", "JPM")

#combine stock data into one DataFrame
stocks = pd.concat([aapl, xlre, spy, jpm], ignore_index=True)

#step 3: merge stock and bond data
merged = pd.merge(stocks, bonds, on='date', how='inner')

#step 4: apply condition
condition = (merged['return'] < 0) & (merged['bond_yield_change'] <= 0.005)
condition_met = merged[condition]

#displaying where 
st.title("Stock Drop + Bond Yield Rise Condition Checker")
st.write(f"Showing dates where stock return < 0 and bond yield change <= 0")

#add filter by ticker
selected_ticker = st.selectbox("Select a stock ticker", merged['ticker'].unique())
filtered = condition_met[condition_met['ticker'] == selected_ticker]

# Show table
st.dataframe(filtered[['date', 'ticker', 'return', 'bond_yield_change']])

# Optional: Plot with seaborn
fig, ax = plt.subplots()
sns.scatterplot(data=filtered, x='date', y='return', hue='bond_yield_change', palette='coolwarm', ax=ax)
ax.axhline(0, color='gray', linestyle='--')
ax.set_title(f"Negative {selected_ticker} Returns with Non-negative Bond Yield Change")
st.pyplot(fig)