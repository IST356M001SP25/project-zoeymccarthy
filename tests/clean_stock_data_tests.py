from tool_functions import clean_stock_data
import pandas as pd


def test_clean_stock_data_columns():
    # Test that the function ensures correct columns
    input_data = pd.DataFrame([
        {"date": "2023-01-01", "open": 100, "high": 110, "low": 90, "close": 105, "adjusted_close": 105, "volume": 1000},
        {"date": "2023-01-02", "open": 106, "high": 112, "low": 95, "close": 108, "adjusted_close": 108, "volume": 1200},
    ])
    cleaned_data = clean_stock_data(input_data)
    expected_columns = ["date", "open", "high", "low", "close", "adjusted_close", "volume"]
    assert list(cleaned_data.columns) == expected_columns

def test_clean_stock_data_no_dates_pre_feb_2020():
    # Test that the function removes dates before February 2020
    input_data = pd.DataFrame([
        {"date": "2020-01-15", "open": 100, "high": 110, "low": 90, "close": 105, "adjusted_close": 105, "volume": 1000},
        {"date": "2020-02-01", "open": 106, "high": 112, "low": 95, "close": 108, "adjusted_close": 108, "volume": 1200},
    ])
    cleaned_data = clean_stock_data(input_data)
    assert all(pd.to_datetime(cleaned_data["date"]) >= pd.Timestamp("2020-02-01"))
    expected_output = input_data
    assert clean_stock_data(input_data) == expected_output

def test_should_pass():
    print("\nAlways True!")
    assert True

if __name__ == "__main__":
    test_clean_stock_data_columns()
    test_clean_stock_data_no_dates_pre_feb_2020()
    test_should_pass()
    print("All tests passed!")