from Pomocne_funkce import*

hledane_slovo = "pes"


Oddelovac()
Vypis_slova(hledane_slovo)



pocet_pokusu = len(hledane_slovo) * 2

for pokus in range(pocet_pokusu):
    zbyvajici_pocet_pokusu = pocet_pokusu-pokus
    tip = input(f"Mysli si písmeno (ještě máš {zbyvajici_pocet_pokusu} pokusů): ")
    Oddelovac()
    index = []
    for i in range(len(hledane_slovo)):
        if hledane_slovo[i] == tip:
            index.append(i)
    if index == []:
        print("slovo neobsahuje písmeno",tip)
    else:
        for i in range(len(index)):
            vypis[index[i]] = tip
    if hledane_slovo == "".join(vypis):
        print("Vyhrál jsi, hledané slovo je:",hledane_slovo)
        break
    else:
        Oddelovac()
        print(" ".join(vypis))

if hledane_slovo != "".join(vypis):
    print("Už nemáš žádný pokus, hledané slovo bylo:",hledane_slovo)
