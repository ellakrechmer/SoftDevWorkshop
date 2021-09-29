import csv
with open('occupations.csv', newline='') as csvfile:
    spamreader=csv.reader(csvfile, delimiter=',')
    data={}
    counter=0;
    for row in spamreader:
        data[row[0]]=row[1]
    keyslist=list(data)
    data.pop(keyslist[0])
    data.pop(keyslist[len(keyslist)-1])
print(data)
