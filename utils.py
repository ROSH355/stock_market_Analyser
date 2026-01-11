"""
Utility functions for the Stock Market Risk & Return Analyzer.
Handles data fetching, preprocessing, and helper operations.
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def fetch_stock_data(tickers, start_date, end_date):
    """
    Fetch historical stock price data from Yahoo Finance.
    
    Parameters:
    -----------
    tickers : list
        List of stock ticker symbols (e.g., ['AAPL', 'MSFT', 'JPM'])
    start_date : str
        Start date in format 'YYYY-MM-DD'
    end_date : str
        End date in format 'YYYY-MM-DD'
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with adjusted closing prices for all tickers
    """
    try:
        logger.info(f"Fetching data for {', '.join(tickers)} from {start_date} to {end_date}")
        
        # Download data for each ticker individually to handle compatibility
        dataframes = []
        for ticker in tickers:
            data = yf.download(ticker, start=start_date, end=end_date, progress=False)
            # Extract Adj Close column
            if 'Adj Close' in data.columns:
                adj_close = data[['Adj Close']].rename(columns={'Adj Close': ticker})
            else:
                # Fallback: use the 4th column (usually Adj Close)
                adj_close = data.iloc[:, [3]].rename(columns={data.columns[3]: ticker})
            dataframes.append(adj_close)
        
        # Combine all tickers into one DataFrame
        combined_data = pd.concat(dataframes, axis=1)
        
        # Handle missing data
        combined_data = combined_data.dropna()
        
        logger.info(f"Successfully fetched data. Shape: {combined_data.shape}")
        return combined_data
    
    except Exception as e:
        logger.error(f"Error fetching data: {str(e)}")
        raise


def get_default_date_range(years=1):
    """
    Get default date range for analysis.
    
    Parameters:
    -----------
    years : int
        Number of years to go back from today
    
    Returns:
    --------
    tuple
        (start_date, end_date) in format 'YYYY-MM-DD'
    """
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365*years)
    
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')


def validate_tickers(tickers):
    """
    Validate that ticker symbols are valid.
    
    Parameters:
    -----------
    tickers : list
        List of ticker symbols
    
    Returns:
    --------
    bool
        True if all tickers are valid, False otherwise
    """
    if not isinstance(tickers, list) or len(tickers) == 0:
        return False
    
    # Quick validation - could be extended with more sophisticated checks
    for ticker in tickers:
        if not isinstance(ticker, str) or len(ticker) == 0:
            return False
    
    return True


def handle_missing_data(df, method='forward_fill'):
    """
    Handle missing data in the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with potential missing values
    method : str
        Method to handle missing data ('forward_fill', 'interpolate', or 'drop')
    
    Returns:
    --------
    pd.DataFrame
        DataFrame with missing data handled
    """
    if method == 'forward_fill':
        df = df.fillna(method='ffill').fillna(method='bfill')
    elif method == 'interpolate':
        df = df.interpolate(method='linear')
    elif method == 'drop':
        df = df.dropna()
    
    return df


def get_summary_statistics(df):
    """
    Generate summary statistics for the data.
    
    Parameters:
    -----------
    df : pd.DataFrame
        DataFrame with stock price data
    
    Returns:
    --------
    pd.DataFrame
        Summary statistics (min, max, mean, std)
    """
    return df.describe().round(4)
