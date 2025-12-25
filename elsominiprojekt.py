import json,pickle
bemenet = input("Nyomjon entert a kezdéshez")
lista = []


while True:
    bemenet = input("Bemeneti adat : | Kilépés : q | Eddig bevitt adatok megjelenítése : s |")

    if bemenet == "q":  #ha kilép,mentse,jsonbe és picklebe
        with open("bemenet.json","w") as f:
            json.dump(lista,f)

        with open("bemenet.pickle", "wb") as f:
            pickle.dump(lista,f)
        break

    elif bemenet == "s":
        try:
            with open("bemenet.json","r") as f:
                mentett_lista = json.load(f)
                print(f"Fájlban tárolt adatok: {mentett_lista}")
        except FileNotFoundError:
            print("Hiba: nincsen még fájl")
        continue
        # with open("bemenet.json","r") as f:
        #     lines = f.readlines()
        #     print(lista)
        #     continue

    lista.append(bemenet)
    print("Hozzáadva a memóriához")

 



