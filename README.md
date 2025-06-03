# 📰 Financial News & Stock Movement Analysis

## 📌 Project Overview

This project analyzes **financial news headlines** and **stock return behavior** using natural language processing (NLP), topic modeling, time-series analysis, Sentiment Analysis and Correlation Analysis.
---

## 🛠 Tools & Technologies

- Python  
- Pandas, NumPy  
- NLTK (text preprocessing)  
- Scikit-learn (TF-IDF, LDA)  
- Matplotlib, Seaborn (visualization)  
- Jupyter Notebook  
- Git  

---

## ⚙️ Setup Instructions

1. **Clone the repository:**

```bash
git clone https://github.com/she-code/KAIM-WEEK-1.git
cd KAIM-WEEK-1
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt

```
## Dataset Description

### 1. **News Dataset**

- **headline**: Article release headline, the title of the news article, which often includes key financial actions like stocks hitting highs, price target changes, or company earnings.
- **url**: The direct link to the full news article.
- **publisher**: Author/creator of article.
- **date**: The publication date and time, including timezone information(UTC-4 timezone).
- **stock**: Stock ticker symbol (unique series of letters assigned to a publicly traded company). For example (AAPL: Apple)

### 2. **Stock Dataset**

- **Date** – Trading day (format: YYYY-MM-DD).
- **Open** – Opening stock price.
- **High** – Highest price of the day.
- **Low** – Lowest price of the day.
- **Close** – Closing stock price.
- **Adj Close** – Adjusted close price (after dividends/splits).
- **Volume** – Number of shares traded.
- **Dividends** – Dividend paid per share on that date.
- **Stock Splits** – Stock split ratio (if any) applied on that date.

