import requests

def trace_btc_wallet(adress):
    try:
        url = f"https://api.blockcypher.com/v1/btc/main/addrs/{adress}/balance"
        res = requests.get(url).json()
        return {
            "address": adress,
            "balance_btc": res.get("balance") / 1e8,
            "txs": res.get("n_tx")
        }
    except Exception as e:
        return {"error": str(e)}
