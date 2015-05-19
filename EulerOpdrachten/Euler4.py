getallen = list(range(1,1000))

def palindroom(n,m):
    vermenig =  str(n * m)
    if vermenig == vermenig[::-1]:
        hit = True
        return hit

antwoorden = []
        
for i in getallen:
    for n in getallen:
        hit = palindroom(i,n)
        if hit == True:
            antwoorden.append(i*n)

print(max(antwoorden))
            


