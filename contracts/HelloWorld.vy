# @version 0.3.7

# Declaring the data type of our stored data
storedData: public(String[32])

@external
def store(_data: String[32]) -> bool:
    """
    Function to store data into the blockchain
    """
    self.storedData = _data
    return True

@external
def get() -> String[32]:
    """
    Function to retrieve stored data from the blockchain
    """
    return self.storedData
