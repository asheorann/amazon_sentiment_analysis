import pandas as pd
from nltk.corpus import stopwords
import string
import nltk

nltk.download('stopwords')

# Load the dataset
test_data = pd.read_csv('/Users/maissanafisa/Downloads/archive 2/test.csv', header=None)

# Assign appropriate column names
test_data.columns = ['label','title','review_text']

# Define stopwords
stop_words = set(stopwords.words('english'))

def clean_text_simple(text):
    text = text.lower()
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    return text

test_data['cleaned_text'] = test_data['review_text'].apply(clean_text_simple)

print(test_data[['review_text', 'cleaned_text']].head())

test_data.to_csv('/Users/maissanafisa/Downloads/archive 2/cleaned_test_data.csv', index=False)
