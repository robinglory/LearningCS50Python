import sys
import requests

def get_bitcoin_price():
    """Fetch the current Bitcoin price in USD from the CoinDesk API."""
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response.raise_for_status()  
        data = response.json()
        return data["bpi"]["USD"]["rate_float"]  
    except requests.RequestException:
        sys.exit("Error: Unable to fetch Bitcoin price.")

def main():
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    try:
        bitcoins = float(sys.argv[1])  
    except ValueError:
        sys.exit("Command-line argument is not a number")

    bitcoin_price = get_bitcoin_price()
    total_cost = bitcoins * bitcoin_price

    print(f"${total_cost:,.4f}")

if __name__ == "__main__":
    main()
