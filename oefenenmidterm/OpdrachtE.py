regel1 = list(input())
regel2 = list(input())
regel3 = list(input())

lijst = range(0,3)
speler1= False
speler2= False


for i in lijst:
    if regel1[i]==regel2[i] and regel1[i]==regel3[i]:
        if regel1[i]=="1":
            speler1 = True
        elif regel2[i]== "2":
            speler2 = True

if regel1[0]== regel1[1] and regel1[0]== regel1[2]:
    if regel1[0]=="1":
            speler1 = True
    elif regel1[0]== "2":
            speler2 = True

if regel2[0]== regel2[1] and regel2[0]== regel2[2]:
    if regel2[0]=="1":
            speler1 = True
    elif regel2[0]== "2":
            speler2 = True

if regel3[0]== regel3[1] and regel3[0]== regel3[2]:
    if regel3[0]=="1":
            speler1 = True
    elif regel3[0]== "2":
            speler2 = True
if regel1[0]== regel2[1] and regel1[0]== regel3[2]:
    if regel2[1]=="1":
            speler1 = True
    elif regel2[1]== "2":
            speler2 = True
if regel3[0]== regel2[1] and regel3[0]== regel1[2]:
    if regel2[1]=="1":
            speler1 = True
    elif regel2[1]== "2":
            speler2 = True

if speler1:
    print("Player 1 wins")
elif speler2:
    print("Player 2 wins")
else:
    print("No winner")


