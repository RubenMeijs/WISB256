bericht = input()
codewoord = input()

lijstbericht= list(bericht)
lijstcode=((list(codewoord))*len(lijstbericht))[0:len(lijstbericht)]




vertaling=[]
for i in range(0,len(lijstbericht)):
    codegetal = ord(lijstcode[i]) - 97
    antwoordgetal = ((ord(lijstbericht[i]) - 97 - codegetal) % 26) + 97
    antwoord =  chr(antwoordgetal)
    vertaling.append(antwoord)

print(''.join(vertaling))
