import math

getal = float(input())

wortel = int(math.ceil(math.sqrt(getal)))
delers = range(2,wortel+1)
priemdeler =[]

for i in delers:
    if getal % i == 0:
        priemdeler.append(i)


print(priemdeler)

for i in priemdeler:
    if i != 0:
        for n in range(0, len(priemdeler)):
            if priemdeler[n]%i == 0  and priemdeler[n] != i:
                priemdeler[n] = 0
                
priemdeler=list(set(priemdeler))

print(max(priemdeler))