from scipy.integrate import odeint
from numpy import *

class Lorenz():
    
    
    def __init__(self,begin,sigma =10, rho =28, beta =8/3):
        self.begin = begin
        self.const = [sigma, rho, beta]
        
    
    
    def stel(self, f, time):
        f0 = self.const[0] * (f[1] -f[0])
        f1 = f[0] * (self.const[1] - f[2] ) - f[1]
        f2 = f[0]* f[1] - self.const[2]*f[2]
        return [f0,f1,f2]
    
    def solve(self, T, dt):
        sol = odeint(self.stel, self.begin,arange(0,T,dt))
        return sol
    
    def df(self,u):
        jacobi = array( [ (-self.const[0], self.const[0], 0), 
            (self.const[1]-u[2],-1, - u[0]),
            (u[1],u[0],-self.const[2])])
        return jacobi
    
    def isStable(self, u):
        matrix= self.df(u)
        stabiel = True
        for i in linalg.eigvals(matrix):
            if i>= 0:
                stabiel = False
                
        return stabiel
            
            
    # def isStable(self, u):
    #     matrix = self.df(u)
    #     stable = True
    #     for i in linalg.eigvals(matrix):
    #         if i>=0:
    #             stable = False
    #             break

    #     return stable    
    