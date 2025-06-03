# Notebooks: Financial News and Stock Analysis

This directory contains Jupyter notebooks related to **financial news and stock price integration**. The goal is to analyze and extract insights from financial news headlines and correlate them with stock market movements using natural language processing (NLP) and statistical techniques.

---

## Contents

### 1. `news_headline_analysis.ipynb`

**Purpose**:  
Performs a full pipeline of **text preprocessing**, **topic modeling**, and **publisher-based analysis** for financial news headlines. It aims to extract key financial themes (e.g., earnings reports, analyst coverage) and assess how different publishers specialize in certain types of news.

### 2. `META_eda.ipynb`

**Purpose**:  
Clean and prepare the **META_historical_data.csv**, then save the cleaned, indexed, and sorted data to **META_cleaned.csv**.

### 3. `AAPL_eda.ipynb`

**Purpose**:  
Clean and prepare the **AAPL_historical_data.csv**, then save the cleaned, indexed, and sorted data to **AAPL_cleaned.csv**.

### 4. `meta_quant_analysis.ipynb`

**Purpose**:  
Performs technical and quantitative analysis on the Meta stock dataset. Utilizes TA-Lib for technical indicators and libraries like pynance and yfinance for financial data retrieval and processing.

### 4. `meta_correlation_analysis.ipynb`

**Purpose**:  
Aligns news and stock data by date and ticker, performs sentiment analysis using TextBlob and VADER, aggregates sentiment scores per stock and date, and calculates correlations between sentiment and both same-day and next-day stock returns. Includes visualizations to assess the impact of news sentiment on stock performance

**Key Tasks Covered**:

- ✅ **Text Cleaning**  
  Custom financial stopwords, lemmatization, and retention of relevant symbols like `$` and `%`.

- ✅ **TF-IDF Keyword Extraction**  
  Identifies the top 2–3 word phrases across all headlines using term frequency-inverse document frequency (TF-IDF).

- ✅ **Topic Modeling (LDA)**  
  Implements Latent Dirichlet Allocation to uncover hidden topics within financial headlines.

- ✅ **Topic Labeling**  
  Manually interprets and labels topics with meaningful descriptions (e.g., “Analyst Coverage & Price Targets”).

- ✅ **Publisher Specialization Analysis**  
  Quantifies how much each publisher contributes to each topic, revealing specialization patterns.

- ✅ **Technical & Quantitative Analysis**
  Loads stock price data using yfinance and performs technical analysis with TA-Lib, including momentum and volatility indicators.

- ✅ **News Sentiment Correlation**
  Aligns stock and news data by date and ticker, performs sentiment analysis (TextBlob & VADER), aggregates sentiment, and computes correlation with same-day and next-day returns. Visualizes results through correlation matrices and distribution plots.

---

## 📦 Requirements

- Python 3.7+
- pandas
- nltk
- scikit-learn
- TA-Lib
- scipy
- matplotlib / seaborn (optional for visualization)

Install packages with:

```bash
pip install requirements.txt
```