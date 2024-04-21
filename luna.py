import requests

def get_luna_wallet_balance(wallet_address):
    url = f'https://lunawallet.io/api/balance/{wallet_address}/'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    balance = response.json()['balance']
    return balance

def main():
    target_wallet_address = input("Enter the Luna wallet address to grab: ")
    balance = get_luna_wallet_balance(target_wallet_address)
    print(f"The balance of the target wallet {target_wallet_address} is: {balance} LUNA")

if __name__ == "__main__":
    main()