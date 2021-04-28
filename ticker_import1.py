import pygsheets
import pandas as pd
import time as t

gc = pygsheets.authorize() # Oauth2 verification from attached client_secret.json and service_account.json

sh = gc.open('pythonforfinance') # opens spreadsheet pythonforfinance
wks = sh.sheet1# sets wks to sheet1

# Hard code For tickers
df = pd.DataFrame({"A":["AAPL", "ABBV", "ABT", "ACN", "ADBE", "AIG", "AMGN", "AMT", "AMZN", "AVGO", "AXP", "BA", "BAC", "BIIB", "BK", "BKNG", "BLK", "BMY", "BRK.B", "C", "CAT", "CHTR", "CL", "CMCSA", "COF", "COP", "COST", "CRM", "CSCO", "CVS", "CVX", "DD", "DHR", "DIS", "DOW", "DUK", "EMR", "EXC", "F", "FB", "FDX", "GD", "GE", "GILD", "GM", "GOOG", "GOOGL", "GS", "HD", "HON", "IBM", "INTC", "JNJ", "JPM", "KHC", "KO", "LIN", "LLY", "LMT", "LOW", "MA", "MCD", "MDLZ", "MDT", "MET", "MMM", "MO", "MRK", "MS", "MSFT", "NEE", "NFLX", "NKE", "NVDA", "ORCL", "PEP", "PFE", "PG", "PM", "PYPL", "QCOM", "RTX", "SBUX", "SO", "SPG", "T", "TGT", "TMO", "TMUS", "TSLA", "TXN", "UNH", "UNP", "UPS", "USB", "V", "VZ", "WBA", "WFC", "WMT", "XOM"]})
spaces = [] # empty list 

intab = "" # intab and outtab to be used with maketrans
outtab = ""


i = 0
while i != 100:
    spaces.append(" ")# creates 100 empty cells to seperate tickers
    i = i+1 
    
df2 = pd.DataFrame({"A": [spaces]})# sets spaces as a DataFrame
TCK = pd.DataFrame() # creates an empty DataFrame

for i in range(0,100):
    dfx = pd.concat([df.iloc[i].T, df2.iloc[0].T])
    TCK = pd.concat([TCK, dfx])  # adds an empty cell between each ticker

j = 1
for i in range(0,len(TCK)):
    s = str(TCK.iloc[j])# sets s to Ticker
    line = s.translate(str.maketrans(intab,outtab,"0"))# deletes zero from input
    wks.update_value((1,j), line, True) # updates values using pygsheets
    j = j +1   
    t.sleep(1.1) # sleep function to prevent Google API override
    # this code is very inefficient but I do not know how to use pygsheets.set_dataframe to insert code horizontally
