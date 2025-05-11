import os
import code.tool_functions as tf

# Test 1: Check if the function returns data for a valid stock symbol
def test_call_stock_data_api_valid_symbol():
    result = tf.call_stock_data_api("AAPL")  # Replace "AAPL" with a valid stock symbol
    expected_file_path = "cache/raw_aapl_data.csv"
    
    # Check if the CSV file is created
    assert os.path.exists(expected_file_path), "The CSV file should exist at the specified path."
    
    #verify the contents of the CSV file
    with open(expected_file_path, 'r') as file:
        content = file.read()
        assert len(content) > 0, "The CSV file should not be empty."


# Test 2: A test that should always pass
def test_always_pass():
    assert True, "This test should always pass."

#run the tests
if __name__ == "__main__":
    test_call_stock_data_api_valid_symbol()
    test_always_pass()
    print("All tests passed!")