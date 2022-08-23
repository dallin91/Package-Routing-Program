# Author: Dallin Reeves
# Created: 15 August 2022

from csv_importer import getPackages
from csv_importer import loadPackageData
from hash_map import HashMap


class Main:
    print("\n----------WGUPS Routing Program----------\n")

    user_input = input("UPDATE THIS LATER\n"
                       "Type 'quit' if you would like to quit\n"
                       "Type '1' if you would like to see hash\n")

    while user_input.lower() != 'quit':
        if user_input == '1':
            loadPackageData('WGUPS Package File.csv')
            packages = getPackages()
            print(type(packages))
            print(len(packages.table))
            break



