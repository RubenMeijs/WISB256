import sys
import math

naam=  str(sys.argv[1])
priemgetallen=[]
twinpriem=0
file = open(naam, 'r')

for line in file:
    getal=int(line.strip())
    priemgetallen.append(getal)

aantal=len(priemgetallen)
grootste=priemgetallen[aantal-1]
nlogn=grootste / (math.log(grootste))
ratio1= aantal * math.log(grootste) / grootste
c2=0.6601618
index=range(0,aantal-1)

for i in index:
    if priemgetallen[i+1]-priemgetallen[i]==2:
        twinpriem+=1
nlogn2=2*c2*grootste/ (math.log(grootste))**2
ratio2= twinpriem / nlogn2

print('Largest Prime =  ' + str(grootste))
print('-------------------------------- ')
print('pi(N) = ' + str(aantal))
print('N/log(N) = ' + str(nlogn))
print('ratio = ' + str(ratio1))
print('--------------------------------')
print('pi_2(N) = ' +str(twinpriem))
print('2CN/log(N)^2 = ' +str(nlogn2))
print('ratio = ' + str(ratio2))

