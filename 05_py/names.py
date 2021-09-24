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

pd1=["Ella", "Christopher", "Ivan"]
pd2=["Justin", "Naomi", "Jeffrey"]

def readNames(filename: str):
    filecontents=""
    with open(filename, "r") as f:
        filecontents=f.read()
    names=filecontents.split("\n")

    #remove empty lines
    names=[name for name in names if name]

    return names

def printNames(pd1, pd2):
    names=pd1+pd2
    randname=names[randrange(len(names))]
    print(randname)

printNames(pd1, pd2)
