import pandas as pd


from web3 import Web3


def generate(amount: int):
    data = []
    web3 = Web3()
    web3.eth.account.enable_unaudited_hdwallet_features()

    for index in range(amount):
        account = web3.eth.account.create_with_mnemonic()
        seed_phrase = account[1]
        address = account[0].address
        private_key = account[0].key.hex()

        print(f"Address: {address}\nSeed Phrase: {seed_phrase}\nPrivate Key: {private_key}\n")

        data.append({
            "index": index,
            "address": address,
            "private_key": private_key,
            "seed_phrase": seed_phrase,
        })
    df = pd.DataFrame(data)
    df.to_csv("new_addresses.csv", index=False, sep="|")


if __name__ == '__main__':
    amount: int = int(input("Enter wallet number: "))
    generate(amount)
