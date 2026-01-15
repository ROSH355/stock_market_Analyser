import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def fetch_stock_data(tickers, start_date, end_date):
    try:
        logger.info(f"Fetching data for {', '.join(tickers)} from {start_date} to {end_date}")
        dataframes = []
        for ticker in tickers:
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)
            if 'Adj Close' in data.columns:
                adj_close = data[['Adj Close']].rename(columns={'Adj Close': ticker})
            else:
                adj_close = data.iloc[:, [3]].rename(columns={data.columns[3]: ticker})
            dataframes.append(adj_close)
        combined_data = pd.concat(dataframes, axis=1)
        combined_data = combined_data.dropna()
        
        logger.info(f"Successfully fetched data. Shape: {combined_data.shape}")
        return combined_data
    
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        raise


def get_default_date_range(years=1):
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*years)
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')

def validate_tickers(tickers):
    if not isinstance(tickers, list) or len(tickers) == 0:
        return False
    for ticker in tickers:
        if not isinstance(ticker, str) or len(ticker) == 0:
            return False
    return True


def handle_missing_data(df, method='forward_fill'):
    if method == 'forward_fill':
        df = df.fillna(method='ffill').fillna(method='bfill')
    elif method == 'interpolate':
        df = df.interpolate(method='linear')
    elif method == 'drop':
        df = df.dropna()
    return df


def get_summary_statistics(df):
    return df.describe().round(4)
