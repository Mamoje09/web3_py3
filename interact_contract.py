import os
from web3 import Web3
from dotenv import load_dotenv

load_dotenv()

provider = os.getenv("WEB3_PROVIDER")
wallet = os.getenv("WALLET_ADDRESS")

if not provider or not wallet:
    raise SystemExit("Set WEB3_PROVIDER and WALLET_ADDRESS in .env")

w3 = Web3(Web3.HTTPProvider(provider))

# USDC Mainnet
contract_address = Web3.to_checksum_address("0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48")
abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function",
    }
]

if not w3.is_connected():
    raise SystemExit("❌ Connection failed. Check WEB3_PROVIDER.")

contract = w3.eth.contract(address=contract_address, abi=abi)
balance = contract.functions.balanceOf(wallet).call()

print(f"USDC Balance for {wallet}: {balance / 1e6} USDC")
