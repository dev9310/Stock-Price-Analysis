import yfinance as yf
import preprocessor

def get_stocks_list():
    tickers = [
    "NHPC.NS", "RELIANCE.NS", "HDFCBANK.NS", "INFY.NS", "TCS.NS", "ICICIBANK.NS",
    "SBIN.NS", "HINDUNILVR.NS", "ITC.NS", "KOTAKBANK.NS", "LT.NS", "AXISBANK.NS",
    "BAJFINANCE.NS", "BHARTIARTL.NS", "MARUTI.NS", "ASIANPAINT.NS", "M&M.NS",
    "SUNPHARMA.NS", "WIPRO.NS", "HCLTECH.NS", "ULTRACEMCO.NS", "TATAMOTORS.NS",
    "TATASTEEL.NS", "TECHM.NS", "ADANIPORTS.NS", "GRASIM.NS", "POWERGRID.NS",
     "BPCL.NS", "IOC.NS","AFIL.NS" , "DTL.NS"
     ]
    return tickers

def get_intervals():
    intervals = {  
        '1 year':365,
        '1 week':7,
        '1 month':30,
        '3 month':90,      
        '6 months':180,
        '3 years':1095,
        'all':1
                 }
    return intervals
    
def get_stock_df(ticker):

    data = yf.download(ticker)
    data = preprocessor.create_datetime(data)

    return data

def get_current_data(df):
    df = df.iloc[-1]
    return df
