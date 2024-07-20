import pandas as pd 

def create_datetime(df):
    df.insert(0,'Time', df.index)
    df['Time'] = pd.to_datetime(df['Time'])
    
    df['Year'] = df['Time'].dt.year
    df['Month'] = df['Time'].dt.month
    df['Day'] = df['Time'].dt.day
    df['Month_name'] = df['Time'].dt.month_name()
    df['10 Days Moving Average'] = df['Close'].rolling(window=10).mean()
    df['30 Days Moving Average'] = df['Close'].rolling(window=30).mean()
    df['100 Days Moving Average'] = df['Close'].rolling(window=100).mean()
    
    


    
    clmn_list = ['Open' , 'Close' , 'Adj Close' , 'Volume' , 'High' , 'Low' ]
    for clmn in clmn_list:
        df[clmn] = df[clmn].round(2)
    

    return df