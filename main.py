# Author: Dallin Reeves   ID: 001176010
# Created: 15 August 2022

from csv_importer import getPackageIDs, getPackages
from csv_importer import loadPackageData
from hash_map import HashMap

loadPackageData('WGUPS Package File.csv')
packageIDs = getPackageIDs()
packages = getPackages()

print("\n----------WGUPS Routing Program----------\n")

user_input = input("UPDATE THIS LATER\n"
                   "Type 'quit' if you would like to quit\n"
                   "Type 'search' to look up a package\n"
                   "Type 'hash' if you would like to see hash\n").lower()

while user_input != 'quit':

    if user_input == 'hash':
        print(packageIDs)
    elif user_input == 'search':
        search_input = int(input("Enter the package ID:"))
        try:
            package = packages.search(search_input)
            print(package)
        except ValueError:
            print("Invalid input")
            exit()
    user_input = input("UPDATE THIS LATER\n"
                   "Type 'quit' if you would like to quit\n"
                   "Type 'search' to look up a package\n"
                   "Type 'hash' if you would like to see hash\n").lower()



