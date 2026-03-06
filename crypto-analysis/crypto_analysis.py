import requests
import pandas as pd

url = "https://api.coindesk.com/v1/bpi/historical/close.json"
data = requests.get(url).json()  # Ask internet for Bitcoin data

prices = data["bpi"]

df = pd.DataFrame(list(prices.items()), columns=["date","price"])  # Make a table
print("Average Price:", df["price"].mean())