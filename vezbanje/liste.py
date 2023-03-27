osoba = ["Sofija" , 25 , "plava", False]

for indeks in range(len(osoba)):
    print(osoba[indeks])


for osobina in osoba:
    print(osobina)




voce_i_povrce = ["jabuka", "beli luk" , "crni luk", "banana", "mandarina", "lubenica", "krastavac"]

for stavka in voce_i_povrce:
    print(stavka)

for i in range(len(voce_i_povrce)):
    print("Na indeksu:" , i , "nalazi se", voce_i_povrce[i])


for indeks , vrednost in enumerate(voce_i_povrce):
    print("indeks:", indeks, "stavka:", vrednost)

automobili = ["Citroen", "BMW", "Opel" , "Kia", "Yugo", "Opel" , "Opel"]

for pozcija , auto in enumerate(automobili):
    if len(auto) == 3:
        print(auto)
    # print("Pozicija", pozcija, "Auto", auto)

# dodaj novi proizvod = append
automobili.append("Mercedes")
automobili[2] = "Opel Corsa"
print(automobili)
automobili[3] = "Kia Sportage"


del automobili[3]
print(automobili)
automobili.remove("BMW")
print(automobili)
automobili.pop(0)
print(automobili)








broj_opela = 0
for indeks in range(len(automobili)):
    if automobili[indeks] == "Opel":
        print("Evo ga opel")
        broj_opela += 1

print("imam", broj_opela , "na placu ")




automobili = ["Citroen", "BMW", "Opel" , "Kia", "Yugo", "Peugeot" , "Audi"]
      
automobili_akcija = []

for i in range(len(automobili)):
    if i == 1 or i == 2 or i == 3:
        automobili_akcija.append(automobili[i])

print(automobili_akcija)


automobili_akcija = automobili[1:4]
print(automobili_akcija)



brojevi = [ 1, 10 , 12 , 7 ,3 ,4 , 2, 5]
parni = []
neparni = []

for broj in brojevi:
    parni.append(broj) if broj % 2 == 0 else neparni.append(broj)
     # if broj % 2 == 0:
    #     parni.append(broj)
    # else:
    #     neparni.append(broj)
print(parni , neparni)

















