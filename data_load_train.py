import pandas as pd
from nltk.corpus import stopwords
import string
import nltk

nltk.download('stopwords')

# Load the dataset
train_data = pd.read_csv('/Users/maissanafisa/Downloads/archive 2/train.csv', header=None)

# Assign appropriate column names
train_data.columns = ['label','title','review_text']

# Define stopwords
stop_words = set(stopwords.words('english'))

def clean_text_simple(text):
    text = text.lower()
    
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    text = ' '.join([word for word in text.split() if word not in stop_words])
    
    return text

train_data['cleaned_text'] = train_data['review_text'].apply(clean_text_simple)

print(train_data[['review_text', 'cleaned_text']].head())

train_data.to_csv('/Users/maissanafisa/Downloads/archive 2/cleaned_train_data.csv', index=False)