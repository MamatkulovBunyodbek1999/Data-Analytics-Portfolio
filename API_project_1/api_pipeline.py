import requests
import pandas as pd


url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
response = requests.get(url)
data = response.json()

# converting JSON to dataframe
df = pd.json_normalize(data)

# kerakli ustunlarni tanlab olaman
df = df[['id', 'symbol', 'name', 'current_price', 'market_cap', 'total_volume']]

# csv faylga o'tqazaman
df.to_csv("crypto_data.csv", index=False)
top10 = df.sort_values(by='market_cap', ascending=False).head(10)
top10.to_csv("top10_crypto.csv", index=False)

# resultatni print qilaman
print("\nTop 10 Cryptocurrencies:\n")
print(top10[['name', 'market_cap']])