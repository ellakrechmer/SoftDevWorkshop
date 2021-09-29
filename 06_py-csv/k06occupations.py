import csv
from random import *;
with open('occupations.csv', newline='') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=',')
    data={}
    for row in spamreader:
        data[row[0]]=row[1]
    keyslist=list(data)
    data.pop(keyslist[0])
    data.pop(keyslist[len(keyslist)-1])
    for job in data:
        data[job]=float(data[job])*10
print(data)
