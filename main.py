# Author: Dallin Reeves   ID: 001176010

from csv_importer import getPackageIDs, getPackages, packageHash
from csv_importer import loadPackageData, loadDistanceData, loadAddressData
from hash_map import HashMap
from distances import findDistance
from addresses import getAddress
import trucks
import datetime

# Load the csv files
loadPackageData('Packages.csv')

packageIDs = getPackageIDs()
packagesHash = getPackages()

# Create truck objects
# I'm only using two trucks because there are only 2 drivers. The 3rd truck is useless without a driver
truck1 = trucks.Truck(16, 18, datetime.timedelta(hours=10, minutes=20),
                      [2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 17, 21, 22, 23, 24, 25, 26, 27, 28, 32],
                      0.0, "4001 South 700 East", None)
truck2 = trucks.Truck(16, 18, datetime.timedelta(hours=8),
                      [1, 3, 13, 14, 15, 16, 18, 19, 20, 29, 30, 31, 33, 34, 35, 36, 37, 38, 39, 40],
                      0.0, "4001 South 700 East", None)


# O(n^2)
def truckDeliverPackages(truck):
    # Creates list of Package IDs currently still on specified truck
    not_delivered = []
    for pId in truck.packages:
        package = packagesHash.search(pId)
        not_delivered.append(package)

    # Sets up nearest neighbor algorithm for delivering packages
    while len(not_delivered) > 0:
        nextAddress = 2000
        nextPackage = None
        for p in not_delivered:
            if findDistance(getAddress(truck.address), getAddress(p.address)) <= nextAddress:
                nextAddress = findDistance(getAddress(truck.address), getAddress(p.address))
                nextPackage = p
        truck.packages.append(nextPackage.id)
        not_delivered.remove(nextPackage)
        truck.miles += nextAddress
        truck.address = nextPackage.address
        truck.time += datetime.timedelta(hours=nextAddress / 18)
        nextPackage.delivered = truck.time
        nextPackage.departure = truck.depart_time


# Sending trucks on their delivery route
truckDeliverPackages(truck2)
truckDeliverPackages(truck1)

print("\n----------WGUPS Routing Program----------\n")

user_input = input("OPTIONS:\n"
                   "Type 'all' if you would like to see status of all packages\n"
                   "Type 'search' to look up a specific package\n"
                   "Type 'miles' if you would like to see total mileage of all trucks\n"
                   "Type 'quit' if you would like to quit the program\n").lower()

# O(n^2)
while user_input != 'quit':

    if user_input == 'all':
        input_time = input("What time would you like to see status of packages? Format: HH:MM:SS ")
        (h, m, s) = input_time.split(":")
        converted_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        for i in packageIDs:
            package = packagesHash.search(i)
            package.updateStatus(converted_time)
            print("\nPackage #{} \nStatus: {}\n".format(i, package.status))
    elif user_input == 'search':
        search_input = int(input("Enter the package ID: "))
        try:
            package = packagesHash.search(search_input)
            input_time = input("What time would you like to see status of package #{}? "
                               "Format: HH:MM:SS ".format(search_input))
            (h, m, s) = input_time.split(":")
            converted_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
            package.updateStatus(converted_time)
            print("\nPackage #{} \nStatus: {}\n".format(search_input, package.status))
        except ValueError:
            print("Invalid input")
            exit()
    elif user_input == 'miles':
        print("\nTotal miles driven:", truck1.miles + truck2.miles, "\n")
    user_input = input("OPTIONS:\n"
                       "Type 'all' if you would like to see status of all packages\n"
                       "Type 'search' to look up a specific package\n"
                       "Type 'miles' if you would like to see total mileage of all trucks\n"
                       "Type 'quit' if you would like to quit the program\n").lower()
