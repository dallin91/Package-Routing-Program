import csv

from hash_map import HashMap


class Package:
    def __init__(self, id, address, city, state, zip, deadline, weight, note,
                 start, location, status):
        self.id = id
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.note = note
        self.start = start
        self.location = location
        self.status = status
        self.delivered = None
        self.departure = None

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s" % (self.id, self.address, self.city, self.state,
                                                   self.zip, self.deadline, self.weight, self.note,
                                                               self.start, self.location, self.status)


def loadPackageData(filename):
    with open(filename) as packageFile:
        packageData = csv.reader(packageFile)
        next(packageData)
        for package in packageData:
            pId = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pWeight = package[6]
            pNote = package[7]
            pStart = ''
            pLocation = ''
            pStatus = ''

            package = Package(pId, pAddress, pCity, pState, pZip, pDeadline, pWeight,
                              pNote, pStart, pLocation, pStatus)

            packageHash.insert(pId, package)


packageHash = HashMap()


def loadDistanceData(filename):
    with open(filename) as distanceFile:
        return list(csv.reader(distanceFile))


def loadAddressData(filename):
    with open(filename) as addressFile:
        return list(csv.reader(addressFile))


def getPackageIDs():
    all = []
    for bucket in packageHash.table:
        for pair in bucket:
            all.append(pair[0])
    return sorted(all)


def getPackages():
    # for i in range (len(packageHash.table)+1):
    #     print("Key: {} and Package: {}".format(i+1, packageHash.search(i+1)))
    return packageHash
