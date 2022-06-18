###---AlluKoodaa---###

KIRJAIMET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def tulostus(k: int):
    mjono = KIRJAIMET[:k][::-1]
    pituus = len(mjono) * 2 - 1
    rivit = []
    for i in range(k):
        c = 0 # laskuri
        rivi = ""
        while c <= i:
            if i == 0:
                rivi = mjono[i] * pituus
                rivit.append(rivi)
                break
            if c == 0:
                rivi = mjono[0]
                c += 1
                continue
            if c == k-1:
                rivi += mjono[-1]
                rivit.append(rivi)
                break
            if c == i:
                rivi += mjono[c] * (pituus - c * 2 - 1)
                rivit.append(rivi)
                break
            rivi += mjono[c]
            c += 1
    for r in rivit:
        if len(r) < pituus:
            loppu = r[:pituus-len(r)][::-1]
            r += loppu
        print(r)
    for r in rivit[-2::-1]:
        if len(r) < pituus:
            loppu = r[:pituus-len(r)][::-1]
            r += loppu
        print(r)

kerrokset = int(input("Kerrokset: "))
tulostus(kerrokset)

###---eof---###
