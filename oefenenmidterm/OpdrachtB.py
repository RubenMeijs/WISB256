som= input()
lijst=som.split()

getal1=int(lijst[0])
getal2=int(lijst[1])
operatie=lijst[2]

# antwoord=getal1 operatie getal2

if operatie== "+":
    antwoord= getal1 + getal2
    print("{0:.3f}".format(antwoord))

if operatie == "*":
    antwoord= getal1 * getal2
    print("{0:.3f}".format(antwoord))

if operatie == "-":
    antwoord= getal1 - getal2
    print("{0:.3f}".format(antwoord))

if operatie == "/":
    antwoord= getal1 / getal2
    print("{0:.3f}".format(antwoord))


