from csv_importer import loadDistanceData

distances = loadDistanceData('Distances.csv')


def findDistance(x, y):
    distance = distances[x][y]
    if distance == '':
        distance = distances[y][x]

    return float(distance)


print(findDistance(0, 3))
