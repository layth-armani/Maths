import random

liste = [0,1]

caca= random.choices(liste, k=8)

e=0

for i in range (len(caca)):
    
    if caca[i]==1:
        e+=1


if e%2==0:
    print("1",caca)
else:
    print("0",caca)

  


