def findRoot(f,a,b,epsilon):
    
    m=(a+b)/2
    
    if abs(a-b)<=epsilon:
        return m
    
    if f(a)<f(b):
        if f(m)<= 0:
            return findRoot(f,m,b,epsilon)
        else:
            return findRoot(f,a,m,epsilon)
    
    if f(a)>f(b):
        if f(m)<= 0:
            return findRoot(f,a,m,epsilon)
        else:
            return findRoot(f,m,b,epsilon)    

def findAllRoots(f,a,b,epsilon):
    
    nulpunten=[]
    
    if epsilon>(1/1000):
        dx=epsilon
    else:
        dx=1/1000
    
    aantalstappen=int(abs(b-a)/dx)
    
    for i in range(1,aantalstappen):
        if (f(a)<=0 and f(a+dx)>=0) or (f(a)>=0 and f(a+dx)<=0):
            nulpunten.append(findRoot(f,a,a+dx,epsilon))
        a+= dx
    
    return nulpunten