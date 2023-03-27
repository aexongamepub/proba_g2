#          0        1    2       3    clanovi u sekvnci primer ispod
osoba = ["Sofija", 20, "plava", True]
print(osoba)


print(osoba[0])
print("Godine:", osoba[1])


#               0           1           2 
automobili = ["Opel" , "Mercedes" , "Citroen"]
print(automobili[2])

for x in range(5,10,2):
    print(x)


       #012345
kurs = "python"
print(kurs[0])
print(kurs[1])
print(kurs[2])
print(kurs[3])



# len(sekvenca)
# duzina = len(kurs)

for x in range(len(kurs)):
    print("Na poziciji:", x ,kurs[x])

ustanova ="IT Academy"

for indeks in range (len(ustanova)):
    print(ustanova[indeks])


'''
0 , 1 , 2 , 3 , 4 , 5 
python 
["Sofija", 25 , True]
   for x in sekvenca :

'''



primer = "zadatak1"
for y in range(len(primer)):
    print(primer[y], end= "")


broj_karaktera = len(primer)
print(broj_karaktera)
indeks = 0 

while indeks < len(primer):
    print(primer[indeks])
    indeks += 1


# korisnicko_ime = "admin"
# uneto_kor_ime = input("Unesi korisnicko ime:")

# if korisnicko_ime == uneto_kor_ime.lower():          #lower menja mala slova u velika
#     print("Dobro dosli")
# else:
#     print("Pogresni podaci")

















