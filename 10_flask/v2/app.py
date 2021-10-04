# Clyde 'Thluffy' Sinclair
# SoftDev
# Oct 2021

from flask import Flask
app = Flask(__name__) #create instance of class Flask

@app.route("/")       #assign fxn to route
def hello_world():
    print("about to print __name__...")
    print(__name__)   #where will this go?
    return "No hablo queso!"

app.run()

#has an extra line and will print "about to print __name__" and then __name__ in terminal
#this prediction was correct; for __name__ it printed __main__, since this is the main method being run
