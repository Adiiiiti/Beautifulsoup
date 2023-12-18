import requests
from bs4 import BeautifulSoup
import pandas as pd
#from datetime import datetime
 
#current_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
file_path = "data.csv"

d = {'TICKER': [], 'PRICE': [] , 'CHANGE VALUE': []}

url="https://stocks.zerodha.com/"

r=requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
tickers = soup.find_all(class_="jsx-4132829120 jsx-2772069103 pointer")
for ticker in tickers:
    print(ticker.text.strip())
    d["TICKER"].append(ticker.text.strip())


prices = soup.find_all(class_="jsx-4132829120 jsx-2772069103 cell text-left font-normal text-14")
for price in prices:
    print(price.text.strip())
    d["PRICE"].append(price.text.strip())

changes = soup.find_all(class_="jsx-4132829120 jsx-2772069103 cell text-left font-normal text-14 change-value")
for change in changes:
    print(change.text.strip())
    d["CHANGE VALUE"].append(change.text.strip())

df = pd.DataFrame(data=d)
df.to_csv(file_path, index=False)

#df.to_csv("data.csv",index=False)


