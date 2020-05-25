If not already connect with the jupiyter notebote

https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com


https://pandas.pydata.org/docs/getting_started/index.html

And lets open our first notebook.  
SHOW JPG OF IMAGE TO CLICK ON
(see how it populates file in terminal)

Lets first install the python package pandas

In the notebook enter

NO! WRITE A NOTE BOOK WITH THSES INSTRUCTIONS



You'll notice we've already included a couple of stocks, Apple and IBM

'''
def test_run():
    df = pd.read_csv("AAPL.csv")
    # print (df)
'''
`test_run()`





locate and download data

finance yahoo aapl
historical history > default is ok > download to your local dir

download APPL and IBM

on rhs click upload and upload the file you just downloaded

`!ls` to connfirm it's there

Now create a new python notebook (next to download)

WIP ERROR on creation

[E 14:37:03.762 NotebookApp] 500 GET /notebooks/Untitled.ipynb (172.17.0.4) 7.79ms referer=https://2886795359-8888-elsy06.environments.katacoda.com/tree?


```python
import pandas as pd

def test_run():
    df = pd.read_csv("AAPL.csv")
    print (df)

if __name__ == "__main__":
    test_run()
```

notice the index at the beginning of each line

add [10:20] in print line   to display just indexes 10 to 20 (19)


```python
import pandas as pd

def get_max_close(symbol):
    df = pd.read_csv("{}.csv".format(symbol))
    return df['Close'].max()

def test_run():
    for symbol in ["AAPL","IBM"]:
        print ("Max Close")
        print (symbol, get_max_close(symbol))

if __name__ == "__main__":
    test_run()
```


ADD QUIZ
how would you calulate the mean for each?


lets ass some plots

```python
import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("AAPL.csv")
    print (df['Adj Close'].plot())
    plt.show()

if __name__ == "__main__":
    test_run()
```


QUIZ 
now show IBM high prices

import pandas as pd
import matplotlib.pyplot as plt

def test_run():
    df = pd.read_csv("IBM.csv")
    print (df['High'].plot())
    plt.show()

if __name__ == "__main__":
    test_run()


Plot two lines:

df[['Close','Adj Close']].plot()