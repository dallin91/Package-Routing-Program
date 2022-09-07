from csv_importer import loadAddressData

addresses = loadAddressData("Addresses.csv")


# Method to extract address from csv
def getAddress(address):
    for r in addresses:
        if address in r[2]:
            return int(r[0])


