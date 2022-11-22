from math import*
from itertools import product,permutations


#Calcul du nombre de polynomes qui admettent -1 comme racine avec P=ax^2 + bx + c   et le triplet (a;b;c) appartenant a C

# a - b + c   = 0    car x= -1


C= [0,1,2,3,4,5,6,7,8,9]
e=0

for (a,b,c) in permutations(C,3):
    k = [a,b,c]
    if a - b + c == 0:
        print(k)
        e +=1

print("Le nombre de polynomes qui admettent -1 comme racine sont: ", e   )
