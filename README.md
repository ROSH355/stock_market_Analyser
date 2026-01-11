# Stock Market Risk & Return Analyzer

Python application for analyzing stock portfolio risk and return metrics using real-time Yahoo Finance data.

## Overview

Fetches stock market data, calculates financial metrics (returns, volatility, correlations, Sharpe ratios), and visualizes insights through an interactive Streamlit dashboard.

## Features

- Real-time data fetching via Yahoo Finance API
- Comprehensive financial metrics calculation
- Interactive Streamlit dashboard
- Price trends and returns distribution visualizations
- Correlation analysis and risk-return profiles
- Portfolio weight optimization
- CSV data export

## Financial Metrics

### Daily Returns
Percentage change in stock price day-to-day: (Price_today - Price_yesterday) / Price_yesterday

### Volatility
Standard deviation of daily returns. Higher volatility indicates higher risk and potential returns.

### Annualization
Convert daily metrics to yearly values using 252 trading days:
- Annualized Return = Daily Return × 252
- Annualized Volatility = Daily Volatility × √252

### Correlation
Measures how stocks move together. Ranges from -1 (opposite movement) to 1 (identical movement). Low-correlated assets provide better portfolio diversification.

### Sharpe Ratio
Risk-adjusted return: (Portfolio Return - Risk-Free Rate) / Portfolio Volatility. Higher values indicate better returns per unit of risk.

## Tech Stack

- Python 3.8+
- pandas - data manipulation
- numpy - numerical computations
- yfinance - Yahoo Finance API
- matplotlib, seaborn - visualizations
- streamlit - web dashboard
- requests - HTTP client

## Project Structure

```
stock-risk-return-analyzer/
├── app.py            # Streamlit dashboard
├── analysis.py       # Financial analysis logic
├── utils.py          # Utility functions
├── requirements.txt  # Dependencies
└── README.md
```

**app.py** - Main Streamlit interface with visualizations and portfolio controls.

**analysis.py** - PortfolioAnalyzer class for calculating returns, volatility, correlation, and Sharpe ratios.

**utils.py** - fetch_stock_data(), validate_tickers(), handle_missing_data(), and helper functions.

## Installation

Clone the repository:
```bash
cd stock-risk-return-analyzer
```

Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the application:
```bash
streamlit run app.py
```

Access at http://localhost:8501

## Usage

Enter stock tickers (e.g., AAPL,MSFT,JPM,SPY) in the sidebar and select a date range. The dashboard displays:

- Average return and volatility across all stocks
- Annualized returns and volatility
- Detailed metrics table for each stock
- Price trends, returns distribution, and correlation heatmap
- Risk-return scatter plot
- Cumulative returns chart
- Portfolio weight sliders to analyze different allocations
- CSV export of results

## Troubleshooting

**No data retrieved**: Verify ticker symbols are correct (AAPL, not APPLE) and the date range is valid.

**API connection error**: Check internet connection and yfinance availability.

**Slow loading**: Reduce number of stocks or shorten the date range.

**Missing dependencies**: Run `pip install -r requirements.txt --force-reinstall`