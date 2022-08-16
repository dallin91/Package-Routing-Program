import csv

import value as value

from hash_map import HashMap

with open("WGUPS Package File.csv") as csvfile:
    read_csv = csv.reader(csvfile)
    hash_map = HashMap()

    for row in read_csv:
        id = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        start = ''
        location = ''
        delivery_status = ''

        value = [id, address, city, state, zip, deadline, weight, note,
                 start, location, delivery_status]

    hash_map.insert(id, value)


def get_hash_map():
    return hash_map
