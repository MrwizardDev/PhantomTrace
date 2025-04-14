from tracker.eth_tools import trace_eth_wallet
from tracker.btc_tools import trace_btc_wallet

def scan_wallet(address: str, chain: str) -> dict:
    if chain == "eth":
        return trace_eth_wallet(address)
    elif chain == "btc":
        return trace_btc_wallet(address)
    else:
        return {"error": "Unsupported chain"}
