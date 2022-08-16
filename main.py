# Author: Dallin Reeves
# Created: 15 August 2022

from csv_importer import get_hash_map

class Main:
    print("\n----------WGUPS Routing Program----------\n")

    user_input = input("UPDATE THIS LATER\n"
                       "Type 'quit' if you would like to quit\n"
                       "Type '1' if you would like to see hash\n")

    while user_input.lower() != 'quit':
        if user_input == '1':
            hashmap = get_hash_map()
            print(hashmap.print())
            quit()


