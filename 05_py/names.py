#Ella Krechmer
#SoftDev
#NamePrint/Classwork/Print a random name from two lists of students
#2021-09-24

#Summary
#Discoveries
#Questions
#Comments

from random import *

def printNames(pd1, pd2):
    names=pd1+pd2
    randname=names[randint(0,len(names)-1)]
    print(randname)
