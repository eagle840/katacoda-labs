`pip3 install jupyter`{{execute}}

`jupyter notebook --allow-root --ip=0.0.0.0`{{execute}}


inside jupyter
'%load_ext zipline'


'''
from zipline.api import order, record, symbol

def initialize(context):
    pass

def handle_data(context, data):
    order(symbol('AAPL'), 10)
    record(AAPL=data.current(symbol('AAPL'), "price"))
'''

inside jupter
'%zipline --bundle quantopian-quandl --start 2000-1-1 --end 2012-1-1 -o backtest.pickle --benchmark-symbol AAPL'

'''
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

style.use("ggplot")

backtest_df = pd.read_pickle("backtest.pickle")
backtest_df.portfolio_value.plot()
plt.show|()
'''