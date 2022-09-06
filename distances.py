import csv
from csv_importer import loadDistanceData

distances = loadDistanceData('Distances.csv')
distances = list(distances)


def findDistance(x,y):
    distance = distances[x][y]
    if distance == '':
        distance = distances[y][x]
    return float(distance)
