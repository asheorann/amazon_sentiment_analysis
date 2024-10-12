import pandas as pd

# Load the dataset without headers
test_data = pd.read_csv('/Users/maissanafisa/Downloads/archive 2/test.csv', header=None)

# Assign appropriate column names
test_data.columns = ['label', 'title', 'review_text']

# Check the new column names and first few rows
print(test_data.head())
