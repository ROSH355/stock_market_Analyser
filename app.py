import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import logging

from utils import fetch_stock_data, get_default_date_range, validate_tickers
from analysis import PortfolioAnalyzer, identify_high_correlation_pairs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

st.set_page_config(
    page_title="Stock Market Risk & Return Analyzer",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    .metric-card {
        padding: 20px;
        border-radius: 10px;
        background-color: #f0f2f6;
        margin: 10px 0;
    }
    </style>
""", unsafe_allow_html=True)


def main():
    st.title("📈 Stock Market Risk & Return Analyzer")
    st.markdown("""
    Analyze stock portfolio risk, returns, and correlations using real-time Yahoo Finance data.
    Perfect for understanding investment dynamics and portfolio optimization.
    """)

    with st.sidebar:
        st.header("⚙️ Configuration")
        
        default_stocks = ['JPM', 'AAPL', 'MSFT', 'SPY']
        
        stocks_input = st.text_input(
            "Enter stock tickers (comma-separated)",
            value=",".join(default_stocks),
            help="e.g., AAPL,MSFT,JPM,SPY"
        )
        
        tickers = [s.strip().upper() for s in stocks_input.split(",") if s.strip()]

        st.subheader("Date Range")
        
        preset_periods = {
            "1 Year": 1,
            "6 Months": 0.5,
            "3 Months": 0.25,
            "1 Month": 1/12,
            "Custom": None
        }
        
        period_choice = st.radio("Select Period:", list(preset_periods.keys()))
        
        if period_choice == "Custom":
            col1, col2 = st.columns(2)
            with col1:
                start_date = st.date_input(
                    "Start Date",
                    value=datetime.now() - timedelta(days=365)
                )
            with col2:
                end_date = st.date_input("End Date", value=datetime.now())
        else:
            years = preset_periods[period_choice]
            end_date = datetime.now()
            start_date = end_date - timedelta(days=365*years)

        st.subheader("Analysis Options")
        show_price_chart = st.checkbox("Show Price Chart", value=True)
        show_returns_dist = st.checkbox("Show Returns Distribution", value=True)
        show_correlation_heatmap = st.checkbox("Show Correlation Heatmap", value=True)
        show_risk_return_scatter = st.checkbox("Show Risk vs Return", value=True)
        show_cumulative_returns = st.checkbox("Show Cumulative Returns", value=True)

        correlation_threshold = st.slider(
            "Correlation Threshold",
            min_value=0.0,
            max_value=1.0,
            value=0.7,
            step=0.05,
            help="Identify stock pairs above this correlation"
        )

    try:
        if not validate_tickers(tickers):
            st.error("❌ Please enter valid stock tickers.")
            return

        with st.spinner(f"📥 Fetching data for {', '.join(tickers)}..."):
            price_data = fetch_stock_data(
                tickers,
                start_date.strftime('%Y-%m-%d'),
                end_date.strftime('%Y-%m-%d')
            )
        
        if price_data.empty:
            st.error("❌ No data retrieved. Please check ticker symbols and date range.")
            return

        analyzer = PortfolioAnalyzer(price_data)

        report = analyzer.get_summary_report()
        col1, col2, col3, col4 = st.columns(4)
        
        mean_returns = report['mean_returns']
        volatility = report['volatility']
        annualized = report['annualized_metrics']
        
        with col1:
            st.metric(
                "Average Return",
                f"{mean_returns.mean()*100:.3f}%",
                help="Mean daily return across all stocks"
            )
        
        with col2:
            st.metric(
                "Average Volatility",
                f"{volatility.mean()*100:.3f}%",
                help="Mean daily volatility across all stocks"
            )
        
        with col3:
            st.metric(
                "Annualized Return",
                f"{annualized['annualized_return'].mean()*100:.2f}%",
                help="Average annualized return (252 trading days)"
            )
        
        with col4:
            st.metric(
                "Annualized Volatility",
                f"{annualized['annualized_volatility'].mean()*100:.2f}%",
                help="Average annualized volatility"
            )

        st.subheader("📊 Risk & Return Metrics")
        st.dataframe(report['risk_return_metrics'], width='stretch')
        
        st.subheader("📈 Visualizations")

        actual_tickers = price_data.columns.tolist()

        if show_price_chart:
            st.markdown("### Stock Prices Over Time")
            fig, ax = plt.subplots(figsize=(12, 6))
            
            for ticker in actual_tickers:
                ax.plot(price_data.index, price_data[ticker], label=str(ticker), linewidth=2)
            
            ax.set_xlabel("Date", fontsize=12)
            ax.set_ylabel("Adjusted Close Price ($)", fontsize=12)
            ax.set_title("Historical Stock Prices", fontsize=14, fontweight='bold')
            ax.legend(loc='best')
            ax.grid(True, alpha=0.3)
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)

        if show_returns_dist:
            st.markdown("### Daily Returns Distribution")
            
            returns_data = report['returns_data'] if 'returns_data' in report else analyzer.returns_data
            
            fig, axes = plt.subplots(2, 2, figsize=(14, 8))
            axes = axes.flatten()
            dist_tickers = returns_data.columns.tolist()[:4]
            for idx, ticker in enumerate(dist_tickers):
                axes[idx].hist(returns_data[ticker] * 100, bins=50, alpha=0.7, color='steelblue', edgecolor='black')
                axes[idx].set_xlabel("Daily Return (%)", fontsize=10)
                axes[idx].set_ylabel("Frequency", fontsize=10)
                axes[idx].set_title(f"{ticker} Daily Returns", fontsize=11, fontweight='bold')
                axes[idx].grid(True, alpha=0.3)
            
            plt.tight_layout()
            st.pyplot(fig)

        if show_correlation_heatmap:
            st.markdown("### Correlation Matrix Heatmap")
            correlation_matrix = report['correlation_matrix']
            
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(
                correlation_matrix,
                annot=True,
                fmt='.2f',
                cmap='coolwarm',
                center=0,
                square=True,
                ax=ax,
                cbar_kws={'label': 'Correlation'}
            )
            ax.set_title("Stock Returns Correlation Matrix", fontsize=14, fontweight='bold')
            plt.tight_layout()
            st.pyplot(fig)
            high_corr_pairs = identify_high_correlation_pairs(correlation_matrix, correlation_threshold)
            if high_corr_pairs:
                st.markdown(f"#### Stock Pairs with Correlation ≥ {correlation_threshold}")
                for stock1, stock2, corr in high_corr_pairs:
                    st.write(f"• **{stock1} - {stock2}**: {corr:.3f}")

        if show_risk_return_scatter:
            st.markdown("### Risk vs Return Analysis")
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            annualized_returns = report['annualized_metrics']['annualized_return'] * 100
            annualized_volatility = report['annualized_metrics']['annualized_volatility'] * 100
            
            scatter = ax.scatter(
                annualized_volatility,
                annualized_returns,
                s=200,
                alpha=0.6,
                c=range(len(tickers)),
                cmap='viridis',
                edgecolors='black',
                linewidth=1.5
            )

            for i, ticker in enumerate(tickers):
                ax.annotate(
                    ticker,
                    (annualized_volatility.iloc[i], annualized_returns.iloc[i]),
                    xytext=(5, 5),
                    textcoords='offset points',
                    fontsize=10,
                    fontweight='bold'
                )
            
            ax.set_xlabel("Annualized Volatility (Risk) %", fontsize=12)
            ax.set_ylabel("Annualized Return %", fontsize=12)
            ax.set_title("Risk vs Return Profile", fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig)

        if show_cumulative_returns:
            st.markdown("### Cumulative Returns")
            
            cumulative_returns = report['cumulative_returns']
            
            fig, ax = plt.subplots(figsize=(12, 6))
            
            for ticker in actual_tickers:
                ax.plot(cumulative_returns.index, cumulative_returns[ticker] * 100, label=str(ticker), linewidth=2)
            
            ax.set_xlabel("Date", fontsize=12)
            ax.set_ylabel("Cumulative Return (%)", fontsize=12)
            ax.set_title("Cumulative Returns Over Time", fontsize=14, fontweight='bold')
            ax.legend(loc='best')
            ax.grid(True, alpha=0.3)
            plt.xticks(rotation=45)
            plt.tight_layout()
            st.pyplot(fig)

        st.subheader("💼 Portfolio Analysis")
        
        st.write("Adjust portfolio weights to see the impact on returns and volatility.")
        
        col1, col2 = st.columns([2, 1])
        
        with col1:
            weights = []
            cols = st.columns(len(actual_tickers))
            
            for idx, ticker in enumerate(actual_tickers):
                with cols[idx]:
                    weight = st.slider(
                        f"{ticker} Weight",
                        min_value=0,
                        max_value=100,
                        value=int(100/len(tickers)),
                        step=1,
                        key=f"weight_{ticker}"
                    )
                    weights.append(weight / 100)
            total_weight = sum(weights)
            if total_weight > 0:
                weights = [w / total_weight for w in weights]
            else:
                weights = [1/len(tickers)] * len(tickers)
        from analysis import calculate_portfolio_metrics
        portfolio_metrics = calculate_portfolio_metrics(
            weights,
            report['annualized_metrics']['annualized_return'].values,
            report['annualized_metrics']['annualized_volatility'].values,
            report['correlation_matrix']
        )
        
        with col2:
            st.metric("Portfolio Return", f"{portfolio_metrics['portfolio_return']*100:.2f}%")
            st.metric("Portfolio Volatility", f"{portfolio_metrics['portfolio_volatility']*100:.2f}%")
            st.metric("Sharpe Ratio", f"{portfolio_metrics['sharpe_ratio']:.3f}")
        st.subheader("💾 Export Data")
        col1, col2 = st.columns(2)
        
        with col1:
            csv_prices = price_data.to_csv()
            st.download_button(
                label="Download Price Data (CSV)",
                data=csv_prices,
                file_name=f"stock_prices_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
        
        with col2:
            csv_metrics = report['risk_return_metrics'].to_csv()
            st.download_button(
                label="Download Metrics (CSV)",
                data=csv_metrics,
                file_name=f"risk_return_metrics_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )
    
    except Exception as e:
        st.error(f"❌ An error occurred: {str(e)}")
        logger.exception("Application error")
        
if __name__ == "__main__":
    main()
