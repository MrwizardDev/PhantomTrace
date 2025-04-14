import requests

def trace_eth_wallet(address):
    try:
        url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address}/balance"
        res = requests.get(url).json()
        return {
            "address": address,
            "balance_eth": res.get("balance") / 1e18,
            "txs": res.get("n_tx")
        }
    except Exception as e:
        return {"error": str(e)}
