import math
class Vector():
    
    def __init__(self,n,i=0):
        if type(i)==list:
            self.vector = i
            self.n = n
        else:
            self.vector = [i]*n
            self.n = n
            
    def __str__(self):
        self.scherm = ""
        for i in range(0,self.n):
            self.scherm += str(self.vector[i]) + "\n"
        
        return self.scherm
    
    
    def scalar(self, alpha):
        return(Vector(self.n, list(map(lambda x: x *alpha, self.vector))))
        
    def inner(self,other):
        return sum(list(map(lambda x,y: x *y, self.vector, other.vector)))
   
    def norm(self):
        return math.sqrt(self.inner(self))
    
    def lincomb(self,other,alpha, beta):
        return Vector(self.n, list(map(lambda x,y: x+y, self.scalar(alpha).vector, other.scalar(beta).vector)))

        