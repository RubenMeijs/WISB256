import sys
import timeit

N = int(sys.argv[1])
output = str(sys.argv[2])

T1=timeit.default_timer()
def sieve(a):
    lijst = list(range(2,a))
    for mini in lijst:
        for getal in lijst:
            if getal%mini==0 and getal != mini:
                lijst.remove(getal)
    return(lijst)

prime = open(output,'w')
data = sieve(N)
for i in data:
    prime.write(str(i) + "\n")
    
T2=timeit.default_timer()
scherm='Found ' + str(len(data)) + ' Prime numbers smaller than ' + str(N) +  ' in ' +  str(T2-T1) + ' sec'
print(scherm)