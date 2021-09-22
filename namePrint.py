from random import *
pd1=["Ella", "Ivan", "Justin"]
pd2=["John", "Amanda", "Peter"]

if (randint(0,1)==0):
    print(pd1[randint(0, len(pd1)-1)])
else:
    print(pd2[randint(0, len(pd2)-1)])
