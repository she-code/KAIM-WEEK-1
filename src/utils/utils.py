
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

def setup_financial_stopwords():
    """Create customized stopwords list for financial text analysis"""
    base_stopwords = set(stopwords.words('english'))
    keep_words = {'up', 'down', 'gain', 'loss', 'high', 'low', 'inc', 'ltd','fda','approval','price','target'}
    financial_stopwords = base_stopwords - keep_words

    extra_stopwords = {
        'said', 'new', 'year', 'firm', 'corp', 'week', 'day', 'time',
        'company', 'companies', 'like', 'would'
    }
    financial_stopwords.update(extra_stopwords)
    return financial_stopwords

def clean_financial_text(text, stopwords_set, lemmatizer=None):
    """Clean and preprocess financial text"""
    if lemmatizer is None:
        lemmatizer = WordNetLemmatizer()
    
    # Retain alphanumerics, $, %, spaces
    text = re.sub(r'[^a-zA-Z0-9\s$%]', '', text)
    tokens = word_tokenize(text.lower())
    
    cleaned_tokens = [
        lemmatizer.lemmatize(token)
        for token in tokens
        if token not in stopwords_set and len(token) > 1
    ]
    return ' '.join(cleaned_tokens)
