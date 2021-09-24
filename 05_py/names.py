#Ella Krechmer
#SoftDev
#NamePrint/Classwork/Print a random name from two lists of students
#2021-09-24

#Summary: I worked with Christopher Liu and Ivan Lam. I modified some older code from the first
#classwork, combining the lists and picking from them, and putting them into a function. We also
#used Christopher's code for reading the names from two files.

#Discoveries:
#Questions
#Comments

from random import *
import sys

def readNames(filename):
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

    pd1=readNames(sys.argv[1])
    pd2=readNames(sys.argv[2])
    names=pd1+pd2

    randname=names[randrange(len(names))]
    print(randname)

#python convention to have main run (from Christopher)
if __name__ == "__main__":
    main()
