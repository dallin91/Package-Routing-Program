# Author: Dallin Reeves
# Created: 15 August 2022

from csv_importer import get_hash_map

class Main:
    print("----------WGUPS Routing Program----------")

    user_input = input("UPDATE THIS LATER"
                       "Type 'quit' if you would like to quit"
                       "Type '1' if you would like to see hash")

    while user_input.lower() != 'quit':
        if user_input == '1':
            print(get_hash_map())


