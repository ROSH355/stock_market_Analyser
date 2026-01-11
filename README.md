# 📈 Stock Market Risk & Return Analyzer

A professional-grade Python application for analyzing stock portfolio risk and return metrics, perfect for demonstrating financial data analysis skills in interviews.

## 🎯 Project Overview

This project fetches real-time stock market data, calculates comprehensive financial metrics, analyzes correlations, and visualizes insights through an interactive Streamlit dashboard. It demonstrates proficiency in financial analysis, data manipulation, and building production-ready applications.

### Key Features

✅ **Real-Time Data Fetching** - Integrates Yahoo Finance API via `yfinance`  
✅ **Comprehensive Metrics** - Calculates returns, volatility, Sharpe ratios, and correlations  
✅ **Interactive Dashboard** - Streamlit-based UI for real-time analysis  
✅ **Rich Visualizations** - Price trends, returns distribution, correlation heatmaps, risk-return profiles  
✅ **Portfolio Optimization** - Adjust weights to analyze portfolio performance  
✅ **Data Export** - Download analysis results as CSV files  
✅ **Production-Ready Code** - Clean architecture, proper logging, error handling

---

## 🧠 Financial Concepts

### Daily Returns
The percentage change in stock price from one day to the next:
```
Daily Return = (Price_today - Price_yesterday) / Price_yesterday × 100%
```

### Volatility (Risk)
Standard deviation of daily returns, measuring price fluctuations:
- **Higher volatility** = Higher risk and higher potential returns
- **Lower volatility** = More stable, predictable stock

### Annualization
Converting daily metrics to yearly equivalents (assuming 252 trading days):
- **Annualized Return** = Daily Return × 252
- **Annualized Volatility** = Daily Volatility × √252

### Correlation
Measures how two stocks move together:
- **Correlation = 1**: Perfect positive correlation (move together)
- **Correlation = 0**: No relationship
- **Correlation = -1**: Perfect negative correlation (move opposite)

**Portfolio Insight**: Low-correlated assets reduce portfolio risk through diversification.

### Sharpe Ratio
Risk-adjusted return metric:
```
Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Portfolio Volatility
```
- **Higher Sharpe Ratio** = Better risk-adjusted returns
- Typical risk-free rate: 2-3% (10-year Treasury yield)

---

## 🛠️ Tech Stack

| Technology | Purpose |
|-----------|---------|
| **Python 3.8+** | Core language |
| **pandas** | Data manipulation and analysis |
| **numpy** | Numerical computations |
| **yfinance** | Yahoo Finance data API |
| **matplotlib** | Static visualizations |
| **seaborn** | Statistical visualization |
| **streamlit** | Interactive web dashboard |
| **requests** | HTTP library |

---

## 📊 Project Structure

```
stock-risk-return-analyzer/
│
├── app.py                  # Streamlit interactive dashboard
├── analysis.py             # Core financial analysis logic
├── utils.py                # Utility functions for data fetching
├── requirements.txt        # Project dependencies
├── README.md               # This file
└── data/                   # Directory for storing downloaded data (optional)
```

### File Descriptions

**app.py** - Main Streamlit application
- User interface for stock selection and date range configuration
- Renders all visualizations and metrics
- Portfolio weight adjustment interface
- Data export functionality

**analysis.py** - Financial analysis module
- `PortfolioAnalyzer` class: Main analysis engine
- Calculates returns, volatility, correlation, and Sharpe ratios
- Helper functions for high-correlation detection
- Portfolio metrics calculation

**utils.py** - Utility functions
- `fetch_stock_data()`: Downloads price data from Yahoo Finance
- `validate_tickers()`: Validates ticker symbols
- `handle_missing_data()`: Data cleaning and preprocessing
- `get_default_date_range()`: Convenient date range generation

---

## 🚀 Installation & Setup

### 1. Clone/Download the Repository

```bash
cd /workspaces/stock_market_Analyser
```

### 2. Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

---

## 📖 How to Use

### 1. **Configure Stocks & Date Range**

In the left sidebar:
- Enter stock tickers (comma-separated): `AAPL,MSFT,JPM,SPY`
- Select a date range: 1 Year, 6 Months, 3 Months, or custom dates
- Default stocks: JPM, AAPL, MSFT, SPY

### 2. **View Key Metrics**

The main dashboard displays:
- **Average Return**: Mean daily return across all stocks
- **Average Volatility**: Mean daily volatility
- **Annualized Return**: Expected yearly return
- **Annualized Volatility**: Yearly risk measure

### 3. **Detailed Metrics Table**

See comprehensive metrics for each stock:
- Mean Daily Return
- Daily Volatility
- Annualized Return & Volatility
- Sharpe Ratio

### 4. **Analyze Visualizations**

- **Price Chart**: Historical adjusted closing prices
- **Returns Distribution**: Histogram of daily returns
- **Correlation Heatmap**: Identify relationships between stocks
- **Risk vs Return**: Scatter plot showing risk-return profile
- **Cumulative Returns**: Total return over the period

### 5. **Build a Portfolio**

Use sliders to adjust portfolio weights and see:
- Portfolio Return
- Portfolio Volatility
- Sharpe Ratio

### 6. **Export Results**

Download CSV files with:
- Historical price data
- Risk & return metrics

---

## 💡 Key Insights & Analysis Tips

### Understanding Correlations

1. **Low Correlation Pairs** (< 0.5):
   - Excellent for diversification
   - Reduces overall portfolio risk
   - Example: Stock prices may move independently due to different sectors

2. **High Correlation Pairs** (> 0.7):
   - Both move in similar directions
   - Less diversification benefit
   - Common in same-sector stocks

3. **Negative Correlation** (< 0):
   - Assets move opposite to each other
   - Strongest diversification benefit
   - Example: Bonds often negatively correlate with stocks

### Risk-Return Analysis

1. **Efficient Frontier**:
   - Stocks in upper-left = High return, low risk (ideal)
   - Stocks in lower-right = Low return, high risk (avoid)

2. **Volatility Interpretation**:
   - SPY (S&P 500) = Low volatility, stable
   - Tech stocks (AAPL, MSFT) = Higher volatility, higher growth potential
   - JPMorgan = Financial sector, moderate volatility

3. **Sharpe Ratio Ranking**:
   - Compare risk-adjusted returns
   - Higher Sharpe ratio = Better performance per unit of risk

### Portfolio Optimization Example

Starting with equal weights (25% each for JPM, AAPL, MSFT, SPY):

| Scenario | Return | Volatility | Insight |
|----------|--------|-----------|---------|
| 25-25-25-25 (Equal) | ~X% | ~Y% | Baseline |
| 50% MSFT, 50% SPY | ~X'% | ~Y'% | Growth-focused |
| 40% JPM, 60% SPY | ~X''% | ~Y''% | Conservative |

---

## 📊 Example Analysis Results

### Typical Stock Metrics (1-Year Period)

| Stock | Daily Return | Volatility | Annualized Return | Annualized Volatility | Sharpe Ratio |
|-------|--------------|-----------|-------------------|----------------------|-------------|
| JPM | 0.05% | 1.2% | 12.5% | 19.0% | 0.55 |
| AAPL | 0.12% | 1.8% | 30.2% | 28.6% | 0.98 |
| MSFT | 0.10% | 1.5% | 25.2% | 23.8% | 0.97 |
| SPY | 0.08% | 1.1% | 20.1% | 17.5% | 0.99 |

*Note: Actual values depend on the time period selected and market conditions.*

### Correlation Matrix Example

|     | JPM  | AAPL | MSFT | SPY  |
|-----|------|------|------|------|
| JPM | 1.00 | 0.45 | 0.42 | 0.68 |
| AAPL| 0.45 | 1.00 | 0.78 | 0.62 |
| MSFT| 0.42 | 0.78 | 1.00 | 0.71 |
| SPY | 0.68 | 0.62 | 0.71 | 1.00 |

**Insights**:
- AAPL & MSFT highly correlated (0.78) → Less diversification
- JPM & AAPL low correlation (0.45) → Good diversification pair

---

## 🎓 Interview Talking Points

### Explain the Project

*"I built a financial data analysis application that fetches real-time stock data, computes key risk and return metrics, and visualizes them through an interactive dashboard. This demonstrates my ability to work with APIs, perform statistical analysis, and build user-friendly applications."*

### Technical Highlights

1. **API Integration**: Seamless Yahoo Finance data fetching with error handling
2. **Statistical Analysis**: Implemented financial metrics from scratch
3. **Object-Oriented Design**: `PortfolioAnalyzer` class for clean, reusable code
4. **Data Pipeline**: Fetch → Process → Analyze → Visualize
5. **User Interface**: Streamlit for creating professional web apps
6. **Best Practices**: Logging, validation, exception handling

### Why This Project?

- **Relevant**: Financial analysis is core to JPMorgan's business
- **Practical**: Demonstrates real-world data science workflow
- **Scalable**: Can extend with backtesting, ML predictions, risk models
- **Production-Ready**: Clean code structure, proper error handling

### Possible Extensions

During interviews, be ready to discuss:

1. **Machine Learning**:
   - Predict stock prices with LSTM neural networks
   - Classify stocks as buy/sell/hold using classification models

2. **Advanced Portfolio Theory**:
   - Implement Markowitz efficient frontier
   - Optimize portfolio weights for maximum Sharpe ratio
   - Add Value-at-Risk (VaR) calculations

3. **Real-Time Trading**:
   - Integrate with broker APIs (Alpaca, Interactive Brokers)
   - Implement automated trading strategies
   - Backtesting with historical data

4. **Risk Analytics**:
   - Monte Carlo simulations for portfolio returns
   - Stress testing with extreme market scenarios
   - Value-at-Risk and Expected Shortfall calculations

5. **Database Integration**:
   - Store data in PostgreSQL/MongoDB
   - Create data warehouse for historical analysis
   - Enable multi-user portfolio tracking

---

## 🐛 Troubleshooting

### Issue: "No data retrieved"

**Cause**: Invalid ticker symbols or date range

**Solution**:
- Verify ticker symbols are correct (e.g., AAPL, not APPLE)
- Check that start date is before end date
- Ensure stocks were trading during the selected period

### Issue: "API connection error"

**Cause**: Network issue or Yahoo Finance API unavailable

**Solution**:
```bash
# Check internet connection
ping google.com

# Verify yfinance is working
python -c "import yfinance; print(yfinance.__version__)"
```

### Issue: Slow data loading

**Cause**: Too many stocks or long date range

**Solution**:
- Reduce number of stocks (start with 3-4)
- Reduce date range (try 6 months instead of 1 year)
- Run during off-peak hours

### Issue: Missing dependencies

**Solution**:
```bash
# Reinstall all dependencies
pip install -r requirements.txt --force-reinstall
```

---

## 📚 Resources & References

### Financial Concepts
- [Investopedia - Stock Returns](https://www.investopedia.com/terms/r/return.asp)
- [Investopedia - Volatility](https://www.investopedia.com/terms/v/volatility.asp)
- [Investopedia - Sharpe Ratio](https://www.investopedia.com/terms/s/sharperatio.asp)
- [Wikipedia - Correlation](https://en.wikipedia.org/wiki/Correlation)

### Libraries
- [pandas Documentation](https://pandas.pydata.org/docs/)
- [yfinance GitHub](https://github.com/ranaroussi/yfinance)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [matplotlib/seaborn Tutorials](https://matplotlib.org/stable/tutorials/index.html)

### Data Sources
- [Yahoo Finance](https://finance.yahoo.com/)
- [FRED - Federal Reserve Economic Data](https://fred.stlouisfed.org/)
- [Alpha Vantage (Free Stock Data API)](https://www.alphavantage.co/)

---

## 🎯 Future Improvements

1. ✨ **Backtesting Engine**: Test trading strategies with historical data
2. 🤖 **ML Predictions**: Stock price forecasting with deep learning
3. 📱 **Mobile App**: React Native mobile version
4. 🌍 **Global Markets**: Support for international exchanges
5. 💾 **Database**: Store analysis results for comparison over time
6. 🔔 **Alerts**: Email/SMS alerts for price movements
7. 📈 **Advanced Metrics**: VaR, CVaR, Sortino Ratio, Calmar Ratio
8. 🎯 **Portfolio Rebalancing**: Automated rebalancing strategies

---

## 📝 License

This project is open-source and available for educational and personal use.

---

## ✍️ Author

Created as a comprehensive financial data analysis project for demonstrating Python proficiency and financial analysis skills.

**Last Updated**: January 2026

---

## 🙏 Acknowledgments

- Yahoo Finance for providing free stock market data
- Streamlit for excellent data app framework
- Pandas and NumPy communities for powerful data tools
- JPMorgan Chase for inspiration and real-world context

---

## 📞 Support

For questions or issues:
1. Check the troubleshooting section above
2. Review the code comments in each module
3. Consult library documentation (links provided)

**Happy Analyzing! 📊💡**