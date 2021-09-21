from random import *
pd1=["Ella", "Ivan", "Justin"]
pd2=["John", "Amanda", "Peter"]

r=randint(0,len(pd1)+len(pd2)-1);
if r>=len(pd1):
    print(pd2[r-len(pd1)])
else:
    print(pd1[r])
