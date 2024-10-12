import pandas as pd

# Load the dataset without headers
train_data = pd.read_csv('/Users/maissanafisa/Downloads/archive 2/train.csv', header=None)

# Assign appropriate column names
train_data.columns = ['label', 'title', 'review_text']

# Check the new column names and first few rows
print(train_data.head())

