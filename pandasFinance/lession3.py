''' build a pandas datafram'''
import pandas as pd

def test_run():
    start_date='2019-02-05'
    end_date='2020-04-04'
    dates=pd.date_range(start_date, end_date)
    print (dates)
    print (dates.summary)
    df1=pd.DataFrame(index=dates)
    print (df1)
    # read SPY data
    dfSPY = pd.read_csv("SPY.csv", index_col="Date",parse_dates=True, 
                       usecols=['Date','Adj Close'],na_values=['nan'])
    # re-name the 'adv close' column to SPY so we don't conflick adding other stocks
    dfSPY = dfSPY.rename(columns={'Adj Close':'SPY'})
    
    #Join the 2 dataframes using DataFrame.join(), left join by default
    df1=df1.join(dfSPY)
    df1 = df1.dropna()
    # both these commands can be used together as
    # df1=
    print df1
    
    symbols = ['GOOG','IBM','GLD']
    
    for symbol in symbols:
        df_temp=pd.read_csv("{}.csv".format(symbol), index_col='DATE',
                           parse_dates=True, usecols=['Date', 'Adj Close'], na_values=['nan'])
        #rename 'adj close' to avoid clash
        df_temp = df_temp.rename(columns={'Adj Close': symbol})
        df=df1.join(df_temp) # default is left join