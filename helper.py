import yfinance as yf
import preprocessor
import pandas as pd
import numpy as np

def get_markdown():
    return """

This tool provides a **comprehensive analysis** of various stocks. Here are some of the features you can explore:



- **📊 Stock Price Analysis**: View **historical stock prices** with interactive line charts.

- **📅 Current Stock Data**: Get the latest stock data including **Open, Close, High, Low**, and **Volume**.

- **📈 Volume Analysis**: Visualize the trading volume with colorful bar charts.

- **🔄 Moving Averages**: Analyze the stock's performance with **10, 30, and 100-day moving averages**.

- **⏳ Customizable Intervals**: Choose different time intervals to tailor the analysis to your needs.

- 🌿 Also check my [GitHub](https://github.com/bannu82)

Select a stock from the sidebar to get started! 🚀
"""

def get_stocks_list():
    tickers = [
    "ICICIBANK.NS","NHPC.NS", "RELIANCE.NS", "HDFCBANK.NS", "INFY.NS", "TCS.NS", 
    "SBIN.NS", "HINDUNILVR.NS", "ITC.NS", "KOTAKBANK.NS", "LT.NS", "AXISBANK.NS",
    "BAJFINANCE.NS", "BHARTIARTL.NS", "MARUTI.NS", "ASIANPAINT.NS", "M&M.NS",
    "SUNPHARMA.NS", "WIPRO.NS", "HCLTECH.NS", "ULTRACEMCO.NS", "TATAMOTORS.NS",
    "TATASTEEL.NS", "TECHM.NS", "ADANIPORTS.NS", "GRASIM.NS", "POWERGRID.NS",
     "BPCL.NS", "IOC.NS","AFIL.NS" , "DTL.NS"
     ]
    return tickers

def get_intervals():
    intervals = {  
        'all':1,
        '1 week':7,
        '1 month':30,
        '3 month':90,      
        '6 months':180,
        '1 year':365,
        '3 years':1095   
                 }
    return intervals
    
def get_stock_df(ticker):

    data = yf.download(ticker)
    data = data[['Open', 'Close' ,'High' , 'Low','Volume']]
    data = preprocessor.create_datetime(data)


    return data

def get_current_data(df):
    df = df.iloc[-1]
    return df

def get_no_of_points(df , points):
    indx = []
    for i in range(points):
        indx.append(int((i/points)*len(df)))
    return np.array(indx)


def get_data_for_ploting(data):

    
    df = pd.DataFrame({
        "Time": np.array(data.Time),
        "Close": np.array(data.Close)
    })
    if len(data) > 100:
        df = df.iloc[get_no_of_points(df,100)]

    return df

