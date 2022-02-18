If not already connect with the jupiyter notebote

https://[[HOST_SUBDOMAIN]]-8888-[[KATACODA_HOST]].environments.katacoda.com

In this lab we'll be using:

https://pandas.pydata.org/docs/getting_started/index.html


And lets open our first notebook.  


import sqlite3
import pandas as pd
import sqlalchemy

engine = sqlalchemy.create_engine('localhost:///OurDataBase.db')


pd.read_sql('table_name', engine)