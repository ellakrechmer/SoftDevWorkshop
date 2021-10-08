#AWEsome: Ella Krechmer, Aaron Contreras, William Chen
#SoftDev
#K13 -- Template for Success
#10-08-21

# Import Flask so app will work
from flask import Flask
app = Flask(__name__)

# Import the things needed for occupation-chooser to work
import random
import csv

# Occupation-chooser code here
# Dictionary is now for all to see!
dictionary ={}
with open('data/occupations.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Excludes the last row since it isn't an occupation"
        if (row['Job Class']!= 'Total' and row['Job Class']!= 'Job Class'):
            dictionary[row['Job Class']] = float(row['Percentage'])

#Uses random.choices to pick the random job
def selectJob():
    job = random.choices(list(dictionary.keys()),list(dictionary.values()), k = 1)
    return "Here's the random one: " + job[0]

def makeList():
    #<br> for viewablity without making it too complicated
    #NOTE: \n does not work, since it will be put onto webpage
    written = "<br> <br> Here's the whole list:<br>"
    listJobs = list(dictionary.keys())
    #Turns the jobs into a string since I can add it to the future return and lists don't seem to work.
    for jobs in listJobs:
        written += jobs + '<br>'
    return written

#What shall be shown
@app.route("/occupyflaskst")
def HEY_WORLD():
    return selectJob() + makeList()

#RUN
app.run()
