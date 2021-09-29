#Gold Medalists: Ella Krechmer, Ivan Lam, Justin Morrill
#SoftDev
#K06 -- StI/O: Divine your Destiny!/Reading in csv files and using the data

#SUMMARY: We read in the data from a csv file (used example code from documentation) to a dictionary.
#Then we removed the first and last row since those are not values that we will be using. We also
#made the percentages (value of the keys) floats, and then multiplied them by 10 so they can be used
#as integers when generating random numbers. We picked a random number out of 1000 (since we multiplied
#by 10) and then went through the dictionary to see if the random number corresponded to a specific key.

#09-28-2021

import csv
from random import *;
with open('occupations.csv', newline='') as csvfile:
    #read in data
    spamreader=csv.reader(csvfile, delimiter=',')
    #add to dictionary
    data={}
    for row in spamreader:
        data[row[0]]=row[1]
    #remove first and last row
    keyslist=list(data)
    data.pop(keyslist[0])
    data.pop(keyslist[len(keyslist)-1])
    #make the percentages floats, then multiply by 10 so they're easier to work with later
    for job in data:
        data[job]=float(data[job])*10

    #randomly print out job based on percentages
    n=randrange(1000)
    start=0
    end=0
    for job in data:
        #this sets the range we're looking at for how likely it is to happen
        start=end
        end+=data[job]
        if (start<=n<end):
            print(job)
