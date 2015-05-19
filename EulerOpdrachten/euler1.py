def som(x):
    i=getal=0
    while i<x:
        if i%3==0:
            getal=i+getal
            i=i+1
        elif i%5==0:
            getal=i+getal
            i=i+1
        else:
            i=i+1
    print(getal)


som(1000)

    