#Gold Medalists: Ella Krechmer, Ivan Lam, Justin Morrill, Naomi Naranjo
#SoftDev
#K10 -- Putting Little Pieces Together
#SUMMARY: We used our previous occupation selector code to display a random occupation on a webpage
#10-05-2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

import csv
from random import *;

with open('occupations.csv', newline='') as csvfile:
    #read in data
    spamreader=csv.reader(csvfile, delimiter=',')
    #remove first and last row
    spamreader=list(spamreader)
    spamreader.pop(0)
    spamreader.pop(-1)
    #add to dictionary
    #make the percentages floats, then multiply by 10 so they're easier to work with later
    data={}
    for row in spamreader:
        data[row[0]]=float(row[1])*10


@app.route("/")       #assign fxn to route

def occupation_printer():
    #makes a string that you will eventually display
    ans=""

    #adds TNPG and roster
    ans+="Gold Medalists: Ella Krechmer, Ivan Lam, Justin Morrill, Naomi Naranjo"
    ans+="<br>"*2

    #prints out all occupations
    for row in data:
        ans+=str(row)+"<br>"

    #randomly print out job based on percentages
    n=randrange(1000)
    start=0
    end=0
    for job in data:
        #this sets the range we're looking at for how likely it is to happen
        start=end
        end+=data[job]
        if (start<=n<end):
            #add random selection to answer
            ans+="<br>"+"Random Occupation: "
            ans+=job
    return ans

app.debug = True
app.run()
