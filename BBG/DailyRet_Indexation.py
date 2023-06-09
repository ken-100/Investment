import pdblp
from xbbg import blp
import workdays
import time
import datetime
import pandas as pd
pd.set_option('display.max_columns', 70)

con = pdblp.BCon(timeout=10000)
con.start()

T = ["JPY Curncy","EUR Curncy"]
tmp = ["px_last"]


d_from = "20050301"
d_to = workdays.workday(datetime.datetime.today(), days=-1).strftime("%Y%m%d")

FX = con.bdh(T, "px_last", d_from, d_to,
             elms = [("nonTradingDayFillOption","NON_TRADING_WEEKDAYS"),("nonTradingDayFillMethod","PREVIOUS_VALUE")]).reset_index()

Ret = FX.iloc[:,1:].pct_change()
Index = ( 1 + Ret ).cumprod()*100
Index.loc[0,:] = 100
Index


Diff = FX.iloc[:,1:].diff()
Diff