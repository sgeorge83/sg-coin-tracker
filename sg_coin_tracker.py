import requests

# CoinGecko IDs for your coins
coins = {
    "BTC"   : "bitcoin",
    "ETH"   : "ethereum",
    "SOL"   : "solana",
    "XRP"   : "ripple",
    "HBAR"  : "hedera-hashgraph",
    "PI"    : "pi-network-iou",
    "KASPA" : "kaspa",
    "LINK"  : "chainlink",
    "TICS"  : "qubetics",
    "QUBIC" : "qubic-network",
 "ASTERDEX" : "aster-2",
 "CARDANO"  : "cardano",
    "NIGHT" : "midnight-3",
   "RENDER" : "render-token"
}

# Prepare API call
ids = ','.join(coins.values())
url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"

try:
    response = requests.get(url)
    prices = response.json()

    print("🪙 Live Crypto Prices (USD):\n")

    for symbol, cid in coins.items():
        price = prices.get(cid, {}).get("usd")
        if price:
            print(f"{symbol}: ${price}")
        else:
            print(f"{symbol}: ❌ Not Found")

except Exception as e:
    print("Error fetching prices:", e)
