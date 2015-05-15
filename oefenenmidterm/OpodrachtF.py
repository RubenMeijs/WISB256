smax =  int(input())
slijst = list(input())
slijst = list(map(int,slijst))
swaarde = range(0, smax+1)


aantal_bezoek = 0
aantal_vrienden = 0
aantal_tot = 0

for i in swaarde:
    if aantal_tot >= swaarde[i]:
        aantal_bezoek += slijst[i]
        aantal_tot += slijst[i]
    else:
        aantal_vrienden += (swaarde[i] -aantal_tot)
        aantal_tot += slijst[i] + swaarde[i] - aantal_tot

print(aantal_vrienden)