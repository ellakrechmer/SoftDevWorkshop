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

app.debug = True
app.run()

#the difference between this in the previous is app.debug, so debug mode will turn on, but I don't know what that means
#in terminal, says "Debugger is active!" and shows the Debugger PIN (945-902-457), but I still don't know how this will work or what it does
