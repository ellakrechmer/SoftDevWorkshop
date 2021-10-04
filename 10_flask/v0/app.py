# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?
#This reminds me of creating a new element in Java that pertains to a certain class.

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
#When I see the '/' it reminds me of path directories in the terminal.
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    #2. I think it'll print in terminal once I run it. 3. It says it'll print __name__ so I assume it's the name corresponding to the Flask element or maybe the file name, since that isn't defined yet.
    return "No hablo queso!"  # Q3: Will this appear anywhere? How u know?
    #I don't think this will appear anywhere unless you want to print out the value of the function and I don't think run() will do that.
app.run()  # Q4: Where have you seen similar construcs in other languages?
#This reminds me of when we ran functions that were part of specific classes in Java for specific elements of those classes.

#post-running: it showed "No hablo queso!" in the browser and I believe it printed __name__ in the terminal
