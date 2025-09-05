import requests

def get_eth_price_usd():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "ethereum", "vs_currencies": "usd"}
    r = requests.get(url, params=params, timeout=15)
    r.raise_for_status()
    data = r.json()
    return data["ethereum"]["usd"]

if __name__ == "__main__":
    price = get_eth_price_usd()
    print(f"💰 Current ETH Price: ${price}")
