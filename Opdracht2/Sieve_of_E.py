import sys
import timeit
<<<<<<< HEAD
=======
import math
>>>>>>> extension

N = int(sys.argv[1])
output = str(sys.argv[2])

T1=timeit.default_timer()
def sieve(a):
<<<<<<< HEAD
    lijst = list(range(2,a))
    for mini in lijst:
        for getal in lijst:
            if getal%mini==0 and getal != mini:
                lijst.remove(getal)
    return(lijst)
=======
    wortel=int(math.ceil((math.sqrt(a))))
    lijst1 = list(range(3,a,2))
    lijst1.append(2)
    minilijst=list(range(3,wortel))
    for mini in minilijst:
        for getal in lijst1:
            if getal%mini==0 and getal != mini:
                lijst1.remove(getal)
    return(lijst1)
>>>>>>> extension

prime = open(output,'w')
data = sieve(N)
for i in data:
    prime.write(str(i) + "\n")
    
T2=timeit.default_timer()
scherm='Found ' + str(len(data)) + ' Prime numbers smaller than ' + str(N) +  ' in ' +  str(T2-T1) + ' sec'
print(scherm)