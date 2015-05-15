N = int(input())
zetten = []
for i in range(0,N):
    zetten.append(input())
dobbel = {'boven' : '6', 'omhoog' : '3', 'omlaag': '4', 'rechts' : '5', 'links' : '2', 'benden' : '1'}
lijst_dobbel = [6,3,4,5,2,1]
lijst_begin = [6,3,4,5,2,1]

# boven, omhoog, omlaag, rechts, links, beneden
for i in range(0,N):
    if zetten[i] == "omhoog":
        lijst_dobbel[0] = lijst_begin[2]
        lijst_dobbel[1] = lijst_begin[0]
        lijst_dobbel[2] = lijst_begin[5]
        lijst_dobbel[5] = lijst_begin[1]
        lijst_begin=lijst_dobbel[:]
    if zetten[i] == "rechts":
        lijst_dobbel[3] = lijst_begin[0]
        lijst_dobbel[5] = lijst_begin[3]
        lijst_dobbel[4] = lijst_begin[5]
        lijst_dobbel[0] = lijst_begin[4]
        lijst_begin=lijst_dobbel[:]
    if zetten[i] == "links":
        lijst_dobbel[0] = lijst_begin[3]
        lijst_dobbel[3] = lijst_begin[5]
        lijst_dobbel[5] = lijst_begin[4]
        lijst_dobbel[4] = lijst_begin[0]
        lijst_begin=lijst_dobbel[:]
    if zetten[i] == "omlaag":
        lijst_dobbel[2] = lijst_begin[0]
        lijst_dobbel[0] = lijst_begin[1]
        lijst_dobbel[5] = lijst_begin[2]
        lijst_dobbel[1] = lijst_begin[5]
        lijst_begin=lijst_dobbel[:]
        

print(lijst_dobbel[0])