from csv_importer import loadDistanceData

distances = loadDistanceData('Distances.csv')


# Method to find distance between two addresses
# O(1)
def findDistance(x, y):
    distance = distances[x][y]
    if distance == '':
        distance = distances[y][x]

    return float(distance)
