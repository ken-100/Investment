from xbbg import blp

LS = ["ES","NQ","RTY","VG","GX","Z ","PT","XP","TP","HI","XU","IH"]

T=[]
T1=[]
for i in range(0,len(LS)):
    T += [LS[i]+"A Index"]
    T1 += [LS[i]+"1 Index"]
    
BDP = blp.bdp(tickers=T, flds=["name","currency","undl_spot_ticker"])
BDP = BDP.loc[T,:]

BDP1 = blp.bdp(tickers=T1, flds=["volume_avg_5d","volatility_90d"])
BDP1 = BDP1.loc[T1,:]

undl = BDP.loc[T,["undl_spot_ticker"]].loc[T,:] + " Index"

tmp=[]
for i in range(0,len(undl)):
    tmp += [undl.iloc[i,0]]
tmp = blp.bdp(tickers=tmp, flds="country_iso").loc[tmp,"country_iso"]
BDP.loc[:,"country"] = BDP.loc[:,"name"]
for i in range(0,len(T)):
    BDP.loc[:,"country"][i] = tmp[i]
    
    undl = BDP.loc[T,["undl_spot_ticker"]].loc[T,:] + " Index"
tmp=[]
for i in range(0,len(undl)):
    tmp += [undl.iloc[i,0]]
tmp = blp.bdp(tickers=tmp, flds="country_iso").loc[tmp,"country_iso"]

for i in range(0,len(T)):
    BDP.loc[:,"country"][i] = tmp[i]
BDP.loc[:,"volume"] = BDP1.loc[:,"volume_avg_5d"].values
BDP.loc[:,"vola"] = BDP1.loc[:,"volatility_90d"].values

print(BDP.shape)
BDP
