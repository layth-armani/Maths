import random

liste = [0,1]

ca= random.choices(liste, k=8)

e=0

for i in range (len(ca)):
    
    if ca[i]==1:
        e+=1


if e%2==0:
    print("1",ca)
else:
    print("0",ca)

  


