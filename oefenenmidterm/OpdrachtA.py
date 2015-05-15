zinnen=int(input())
aantal=range(1,zinnen+1)

for i in aantal:
    bericht=input()
    woorden=bericht.split()
    if len(woorden)>4:
        print("Crackers!")
    else:
        print(bericht + " krAh!") 