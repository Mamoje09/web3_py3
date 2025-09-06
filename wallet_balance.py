
### `wallet_balance.py`

import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

provider = os.getenv("WEB3_PROVIDER")
wallet = os.getenv("WALLET_ADDRESS")

if not provider or not wallet:
    raise SystemExit("Set WEB3_PROVIDER and WALLET_ADDRESS in .env")

w3 = Web3(Web3.HTTPProvider(provider))

if w3.is_connected():
    balance = w3.eth.get_balance(wallet)
    print(f"Wallet: {wallet}")
    print(f"Balance: {w3.from_wei(balance, 'ether')} ETH")
else:
    print("❌ Connection failed. Check WEB3_PROVIDER.")
