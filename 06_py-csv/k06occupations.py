import csv
with open('occupations.csv', newline='') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        print(row)
