# Notebooks: Financial News and Stock Analysis

This directory contains Jupyter notebooks related to **financial news and stock price integration**. The goal is to analyze and extract insights from financial news headlines and correlate them with stock market movements using natural language processing (NLP) and statistical techniques.

---

## Contents

### 1. `financial_data_analysis.ipynb`

**Purpose**:  
Performs a full pipeline of **text preprocessing**, **topic modeling**, and **publisher-based analysis** for financial news headlines. It aims to extract key financial themes (e.g., earnings reports, analyst coverage) and assess how different publishers specialize in certain types of news.

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

---

## 📦 Requirements

- Python 3.7+
- pandas
- nltk
- scikit-learn
- matplotlib / seaborn (optional for visualization)

Install packages with:

```bash
pip install requirements.txt
```