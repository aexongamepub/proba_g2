import random




x = -10

if x > 0:
    print("broj x je pozitivan")

print("izvrasava se u svakom slucaju")

vozilo_u_pokretu = True
brzina = 60

if vozilo_u_pokretu :
    print("vozilo se krece...")
    print("Proverite i brzinu...")
    if brzina > 50 :
        print("Prekoracena brzina")
    print("ovo izvrasvam kolika god da je brzina")
    if brzina <= 50:
        print("Brzina je OK.")

if vozilo_u_pokretu == False:
    print("Vozilo se ne krece...")


# 1 - prikaz , 2 - kupovina , 3 - izlaz 
proizvod = "duks"
cena = 3000

# komanda = int(input("Unesite komandu: "))



# if komanda == 1:
#     print("Prikazi proizvode")
#     print("Proizvod:", proizvod , "Cena:",cena )
# if komanda == 2:
#     print("Kupovina...")
#     stanje = int(input("Unesite stanje na racunu: "))
#     if stanje >= cena:
#         print("Uspesna kupovina!")
#     if stanje < cena:
#         print("Neuspesna kupovina...")
# if komanda == 3:
#     print("Izlaz")



broj = 5

if broj > 0:
    print("broj je veci od 0.")
else:
    print("broj je 0 ili manji od 0.")

marija = False
ksenija = True
katarina = False

devojka_na_dejtu = ""

if marija:
    devojka_na_dejtu = "marija"
elif katarina:
    devojka_na_dejtu = "katarina"
elif ksenija:
    devojka_na_dejtu = "ksenija"
else:
    devojka_na_dejtu = "sofija"

print("Izlazi sa mnom:", devojka_na_dejtu)



automobil_polovan = False
godiste = 2021
boja = "crna"


if (automobil_polovan == True or godiste > 2017) and boja == "crna" :
    print("Kupujem")


# not False - > True

if not automobil_polovan :
    print("Automobil je nov.")


prisutan = False  # nije na casu
smer = "python"

if prisutan == True and smer == "python" :
    print("Polaznik je bio na casu")

if prisutan:
    print("Na casu je")

if not prisutan :      # ako nas interesuje da li je False
    print("Nije na casu")


# trenutni_rezultat = random.randint(1, 100)
# novi_rezulltat = int(input("Unesite novi broj (od 1 do 100): "))

# if novi_rezulltat > 100 or novi_rezulltat < 1 :
#     print("Proverite broj , dozvoljeno od 1 do 100")
# elif trenutni_rezultat < novi_rezulltat:
#     print("Pobedili ste")
# elif trenutni_rezultat == novi_rezulltat:
#         print("Identicne vrednosti !!!")
# else:
#         print("Izgubili ste")

# pol = input("Unesite pol :")
# poruka = ""


# if pol == "m":
#     poruka = "Hey mister !"
# else:
#     poruka = "Hey miss!"


# poruka = "Hey mister!" if pol == "m" else "Hey miss"

# print(poruka)

# boja_tastera = zelena if obrok_kompletiran else crvena


popularan_proizvod = ""
jesen = False


popularan_proizvod = "ajvar" if jesen  else "sladoled"


 




# ajvar ako je jesen , tada je ajvar , a ako nije onda sladoled




