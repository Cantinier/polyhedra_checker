import requests
from web3 import Web3

with open("wallets.txt", "r") as file:
    wallets = [row.strip() for row in file]


def check(address: str) -> float:
    addr = Web3.to_checksum_address(address)
    addr_prefix = addr.lower()[2:5]

    result_count = 0
    # для Ethereum
    url_eth = f"https://pub-88646eee386a4ddb840cfb05e7a8d8a5.r2.dev/eth_data/{addr_prefix}.json"
    resp_eth = requests.get(url_eth)

    try:
        json = resp_eth.json()
        if json is None:
            result_count += 0
        else:
            if addr in json:
                result_count += int(json[addr]['amount'], 16) / 10 ** 18
            else:
                result_count += 0
    except:
        return "Ошибка от сервера"

    # для BSC
    url_bsc = f"https://pub-88646eee386a4ddb840cfb05e7a8d8a5.r2.dev/bsc_data/{addr_prefix}.json"
    resp_bsc = requests.get(url_bsc)

    try:
        json = resp_bsc.json()
        if json is None:
            result_count += 0
        else:
            if addr in json:
                result_count += int(json[addr]['amount'], 16) / 10 ** 18
            else:
                result_count += 0
    except:
        return "Ошибка от сервера"

    return result_count


total = 0

for wallet in wallets:
    tokens = check(wallet)
    print(f"{wallet}: {tokens}")
    total += tokens

print(f"Total: {total}")
