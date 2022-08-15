import csv

from hash_map import HashMap

with open("WGUPS Package File.csv", "wt") as fp:
    writer = csv.writer(fp, delimiter=",")