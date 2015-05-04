import sys
import timeit
import math

N = int(sys.argv[1])
output = str(sys.argv[2])

T1=timeit.default_timer()
def sieve(a):
    
    wortel=int(math.ceil((math.sqrt(a))))
    lijst1 = list(range(3,a,2))
    minilijst=list(range(3,wortel,2))
    
    for mini in minilijst:
        for getal in lijst1:
            if getal%mini==0 and getal != mini:
                lijst1[(getal-1)/2-1]=0
    lijst1=list(set(lijst1))
    lijst1.remove(0)
    lijst1.append(2)
    lijst1.sort()
    return(lijst1)


prime = open(output,'w')
data = sieve(N)
for i in data:
    prime.write(str(i) + "\n")
    
T2=timeit.default_timer()
scherm='Found ' + str(len(data)) + ' Prime numbers smaller than ' + str(N) +  ' in ' +  str(T2-T1) + ' sec'
print(scherm)