import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)


class PortfolioAnalyzer:
    def __init__(self, price_data):
        
        self.price_data = price_data
        self.returns_data = None
        self.metrics = {}
        
        logger.info(f"PortfolioAnalyzer initialized with {len(price_data.columns)} stocks")
    
    def calculate_daily_returns(self):
        self.returns_data = self.price_data.pct_change().dropna()
        logger.info(f"Calculated daily returns. Shape: {self.returns_data.shape}")
        return self.returns_data
    
    def calculate_mean_return(self):
        
        if self.returns_data is None:
            self.calculate_daily_returns()
        
        mean_returns = self.returns_data.mean()
        self.metrics['mean_return'] = mean_returns
        logger.info("Calculated mean returns")
        return mean_returns
    
    def calculate_volatility(self):
        
        if self.returns_data is None:
            self.calculate_daily_returns()
        
        volatility = self.returns_data.std()
        self.metrics['volatility'] = volatility
        logger.info("Calculated volatility")
        return volatility
    
    def calculate_annualized_metrics(self):
        if self.returns_data is None:
            self.calculate_daily_returns()
        
        trading_days = 252
        
        annualized_return = self.calculate_mean_return() * trading_days
        annualized_volatility = self.calculate_volatility() * np.sqrt(trading_days)
        
        return {
            'annualized_return': annualized_return,
            'annualized_volatility': annualized_volatility
        }
    
    def calculate_correlation_matrix(self):
        if self.returns_data is None:
            self.calculate_daily_returns()
        
        correlation_matrix = self.returns_data.corr()
        self.metrics['correlation'] = correlation_matrix
        logger.info("Calculated correlation matrix")
        return correlation_matrix
    
    def calculate_cumulative_returns(self):
       
        if self.returns_data is None:
            self.calculate_daily_returns()
        
        cumulative_returns = (1 + self.returns_data).cumprod() - 1
        logger.info("Calculated cumulative returns")
        return cumulative_returns
    
    def calculate_risk_return_metrics(self):

        if self.returns_data is None:
            self.calculate_daily_returns()
        
        metrics = pd.DataFrame({
            'Mean Daily Return': self.calculate_mean_return(),
            'Volatility (Daily)': self.calculate_volatility(),
        })
        
        
        annualized = self.calculate_annualized_metrics()
        metrics['Annualized Return (%)'] = annualized['annualized_return'] * 100
        metrics['Annualized Volatility (%)'] = annualized['annualized_volatility'] * 100
        
        risk_free_rate = 0.02  
        daily_risk_free = risk_free_rate / 252
        
        sharpe_ratio = (metrics['Mean Daily Return'] - daily_risk_free) / self.returns_data.std()
        metrics['Sharpe Ratio'] = sharpe_ratio
        
        return metrics.round(4)
    
    def get_summary_report(self):
        self.calculate_daily_returns()
        
        report = {
            'mean_returns': self.calculate_mean_return(),
            'volatility': self.calculate_volatility(),
            'annualized_metrics': self.calculate_annualized_metrics(),
            'correlation_matrix': self.calculate_correlation_matrix(),
            'risk_return_metrics': self.calculate_risk_return_metrics(),
            'cumulative_returns': self.calculate_cumulative_returns(),
            'returns_data': self.returns_data
        }
        
        logger.info("Generated summary report")
        return report


def identify_high_correlation_pairs(correlation_matrix, threshold=0.7):
    pairs = []
    
    for i in range(len(correlation_matrix.columns)):
        for j in range(i+1, len(correlation_matrix.columns)):
            if abs(correlation_matrix.iloc[i, j]) >= threshold:
                pairs.append((
                    correlation_matrix.columns[i],
                    correlation_matrix.columns[j],
                    correlation_matrix.iloc[i, j]
                ))
    
    return sorted(pairs, key=lambda x: abs(x[2]), reverse=True)


def calculate_portfolio_metrics(weights, returns, volatility, correlation_matrix):
    
    weights = np.array(weights)
    returns = np.array(returns)
    volatility = np.array(volatility)
    
    portfolio_return = np.sum(weights * returns)
    
    cov_matrix = correlation_matrix.values * np.outer(volatility, volatility)
    portfolio_volatility = np.sqrt(np.dot(weights, np.dot(cov_matrix, weights)))
    
    return {
        'portfolio_return': portfolio_return,
        'portfolio_volatility': portfolio_volatility,
        'sharpe_ratio': portfolio_return / portfolio_volatility if portfolio_volatility > 0 else 0
    }
