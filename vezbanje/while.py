import random


sekunde = 10

# while sekunde > 0:
#     print(sekunde)
#     sekunde -= 1






baterija = 90

while baterija > 0 :
    print("Mozes koristiti telefon:" , baterija , "%")
    baterija -= random.randint(5,20)


print("Baterija je prazna")


# prekini petlju kada naidjes na broj 5
# stampaj sve brojeve osim broj 2


for broj in range(11):
  if broj == 2:
     continue
  print(broj)
  







