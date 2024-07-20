import yfinance as yf
import pandas as pd
import mplfinance as mpf

# List of popular Indian stock tickers
tickers = [
    "NHPC.NS", "RELIANCE.NS", "HDFCBANK.NS", "INFY.NS", "TCS.NS", "ICICIBANK.NS",
    "SBIN.NS", "HINDUNILVR.NS", "ITC.NS", "KOTAKBANK.NS", "LT.NS", "AXISBANK.NS",
    "BAJFINANCE.NS", "BHARTIARTL.NS", "MARUTI.NS", "ASIANPAINT.NS", "M&M.NS",
    "SUNPHARMA.NS", "WIPRO.NS", "HCLTECH.NS", "ULTRACEMCO.NS", "TATAMOTORS.NS",
    "TATASTEEL.NS", "TECHM.NS", "ADANIPORTS.NS", "GRASIM.NS", "POWERGRID.NS",
    "HDFC.NS", "BPCL.NS", "IOC.NS"
]

# Download and store data
dataframes = {}
for ticker in tickers:
    data = yf.download(ticker)
    dataframes[ticker] = pd.DataFrame(data)
    break

# Function to plot candlestick chart using mplfinance
def plot_candlestick_mpf(ticker, df):
    df.index.name = 'Date'  # Ensure 'Date' is the index name
    df = df[['Open', 'High', 'Low', 'Close', 'Volume']]  # Reorder columns for mplfinance
    mpf.plot(df, type='candle', style='charles', title=f'{ticker} - Candlestick Chart',
             ylabel='Price', volume=True, figsize=(14, 7))

# Plot candlestick charts for each ticker
for ticker, df in dataframes.items():
    plot_candlestick_mpf(ticker, df)
