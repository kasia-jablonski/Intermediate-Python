import csv

with open('museum.csv', newline='') as csvfile:
    artreader = csv.DictReader(csvfile, delimiter='|')
    rows = list(artreader)
    for row in rows[1:3]:
        print(row['group1'])