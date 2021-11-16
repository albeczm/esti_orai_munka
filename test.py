import random

print("Git próba")
print("Ez már a nem tudom hanyadik commit.")


print("Első feladat")
szam1 = int(input("Kérek egy számot: "))
szam2 = int(input("Kérek egy másik számot: "))
print(szam1+szam2)
kilencesvane="Nincs"
print("Második feladat")
lista = [0,0,0,0,0,0,0,0,0,0]
for x in range(10):
    lista[x]=int(random.randrange(1,10))
    if(lista[x] == 9):
        kilencesvane="Van"




print("Átlaguk: ",(sum(lista)/len(lista)))
print("Legkisebb: ",min(lista))
print("Legnagyobb: ",max(lista))
print("Van benne kilences?", kilencesvane)
