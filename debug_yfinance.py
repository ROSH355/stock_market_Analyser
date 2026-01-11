import yfinance as yf
import pandas as pd

tickers = ['AAPL', 'MSFT']
data = yf.download(tickers, start='2025-01-11', end='2026-01-11', progress=False)

print("Data shape:", data.shape)
print("\nColumn types:")
print(type(data.columns))
print("\nColumns:")
print(data.columns.tolist())
print("\nFirst few rows:")
print(data.head())
print("\nData dtypes:")
print(data.dtypes)
