def fibo(x):
    i=j=1
    getal=0
    while i<x:
        if i%2==0:
            getal=getal+i
        s=i
        i=s+j
        j=s
    print(getal)            
fibo(4000000)
