from brownie import *

def main():
    print('heya')
    # Get the account to deploy the contract
    acc = accounts.add('c7a1b72ccfb382bcf6c43a9527799fa60e519873f3324517cc23979bd4b3137f')#accounts[0]

    # Deploy the contract
    ratings = Ratings.deploy({"from": acc})

    # Set up a dummy contract address for testing
    dummy_contract_address = "0x1234567890123456789012345678901234567890"

    # Call the store function
    ratings.store(dummy_contract_address, 5, {"from": acc})

    # Print the stored rating
    print("printing")
    print(ratings.get(dummy_contract_address, {"from": acc}))
