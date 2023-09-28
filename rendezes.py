with open("ki.txt", "r") as f:
    adatok = f.read()
    adatok = adatok.split(";")

def szam(list):
    try:
        int(list)
        return True
    except ValueError:
        return False
    
def ujadat(a, adatok):
    uj_adat=None
    x=False
    while x==False:
        if tipus == "szamok":
            uj_adat = input("Adjon meg egy új számot: ")
            if not uj_adat.isdecimal():
                print("Csak szám lehet!")
                continue
            else:
                x=True
        else:
            uj_adat = input("Adjon meg egy új szöveget: ")
            if not uj_adat.isalpha():
                print("Csak szöveg lehet!")
                continue
            else:
                x=True
        
    if szam(adatok[0]):
        adatok = [int(item) for item in adatok]
        uj_adat = int(uj_adat)
    
    index = 0
    while index < len(adatok) and ((uj_adat > adatok[index]) if not a else (uj_adat < adatok[index])):
        index += 1
    adatok.insert(index, uj_adat)
    
    with open("ki.txt", "w") as file:
        file.write(";".join(map(str, adatok)))
    
a = input("Növekvő vagy csökkenő? (n/cs): ").lower() == "cs"
tipus = "szamok" if szam(adatok[0]) else "szoveg"

if tipus == "szamok":
    adatok = [int(item) for item in adatok]
else:
    adatok = [str(item) for item in adatok]

n=len(adatok)
for i in range(n):
    for j in range(0, n-i-1):
        if (adatok[j] > adatok[j+1]) if not a else (adatok[j] < adatok[j+1]):
            adatok[j], adatok[j+1] = adatok[j+1], adatok[j]

if tipus == "szamok":
        adatok = [str(item) for item in adatok]
else:
    adatok = [item for item in adatok]
    
with open("ki.txt", "w") as file:
    file.write(";".join(adatok))

ujadat(a, adatok)

