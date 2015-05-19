import math

N = int(input())

def priemdelers (getal):
    delers = range(2, getal+1)
    priemen = []
    for i in delers:
        if getal % i == 0:
            priemen.append(i)
    for i in priemen:
        if i != 0:
            for n in range(0, len(priemen)):
                if priemen[n]%i == 0  and priemen[n] != i:
                    priemen[n] = 0
    return priemen
                    
for i in range(2, N+1):
    lijst=[]
    priemen=priemdelers(i)
    lijst.append(priemen)

print(lijst)    

