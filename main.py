from tracker.wallet_scanner import scan_wallet
from rich import print

if __name__ == "__main__":
    print("[bold cyan]🕵️ PhantomTrace Wallet Tracer[/bold cyan]")
    wallet = input("Enter wallet address: ").strip()
    chain = input("Chain (eth/btc): ").strip().lower()

    result = scan_wallet(wallet, chain)
    print("\n[bold green]Scan Result:[/bold green]")
    print(result)
