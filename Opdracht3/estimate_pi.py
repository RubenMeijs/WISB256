import random
import math
import sys

# we gaan uit van verticale lijnen

def drop_needle(L):
    #defineren van random variables
    x0=random.random()
    y0=random.random()
    a=random.vonmisesvariate(0,0)
    punt1=(x0,y0)
    punt2=(x0+ L*math.cos(a),y0+L*math.sin(a))
    #omdat we van verticale lijnen uit gaan hebben we een hit als x1-x0 groter is dan de afstand tot de lijn
    
    #bepalen of het een hit is of niet
    if punt2[0]>1 or punt2[0]<0:
        hit=True
    else:
        hit=False
    return(hit)

if len(sys.argv)<3:
    print('Use: estimate_pi.py N L')
elif float(sys.argv[2])>1:
    print('AssertionError: L should be smaller than 1')  
else:
    N = int(sys.argv[1])
    L = float(sys.argv[2])
    aantal_hits=0
    lijst= range(1,N)
    
    for i in lijst:
        hit=drop_needle(L)
        if hit== True:
            aantal_hits+=1
    
    pi=2*L*N / aantal_hits
    
    scherm1 = str(aantal_hits) + ' hits in ' +  str(N) +  ' tries \n Pi = ' + str(pi)
    
    
    print(scherm1)