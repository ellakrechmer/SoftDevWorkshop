#Ella Krechmer
#SoftDev
#NamePrint/Classwork/Print a random name from two lists of students
#2021-09-24, 2021-09-27

#SUMMARY: I worked with Christopher Liu and Ivan Lam. I modified some older code from the first
#classwork, combining the lists and picking from them, and putting them into a function. We also
#used Christopher's code for reading the names from two files.

#DISCOVERIES: I learned/remembered how to read from files in Python ("r" means read). I also learned
#how to take parameters from the terminal, by importing sys and using argv. I also learned a Python
#convention in using main (at the bottom of this file), which just makes sure that if there is a main
#function, it is run when the program is run.

#QUESTIONS: n/a

#COMMENTS: We didn't originally use the dictionary, we feel that it is an unnecessary
#way to structure the data.

from random import *
import sys


def readNames(filename):
    #open and read the file
    filecontents=""
    with open(filename, "r") as f:
        filecontents=f.read()
    names=filecontents.split("\n")

    #remove empty lines
    names=[name for name in names if name]

    return names

def main():
    #checks to make sure you are putting in the text files in the argument in terminal
    if len(sys.argv) != 3:
        print("Incorrect arguments. Usage: python names.py pd1_filename pd2_filename")
        return

    #dictionary of names read in from text files in the argument
    periods={
        'pd1':readNames(sys.argv[1]),
        'pd2':readNames(sys.argv[2])
    }

    #iterate through the dictionary to make a list of names
    names=[]
    for period in periods.keys():
        names+=periods[period]

    randname=names[randrange(len(names))]
    print(randname)

#python convention to have main run (from Christopher)
if __name__ == "__main__":
    main()
