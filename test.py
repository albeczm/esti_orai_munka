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



print(lista)
print("Átlaguk: ",(sum(lista)/len(lista)))
print("Legkisebb: ",min(lista))
print("Legnagyobb: ",max(lista))
print("Van benne kilences?", kilencesvane)

print("Harmadik feladat")
neved=str(input("Kérek egy felhasználó nevet!: "))
password=str(input("Kérek egy jelszavat, amivel befogsz jelentkezni! Ne felejtsd el!: "))
valaszneved=""
valaszpassword=""
while valaszneved != neved and valaszpassword != password:
    valaszneved = str(input("Add meg a neved!: "))
    valaszpassword = str(input("Add meg a jelszód!: "))
print("Bejelentkezve")
