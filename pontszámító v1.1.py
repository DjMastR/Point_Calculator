
def evvege_ellenorzo(a):
    while int(a) < 1 or int(a) > 5:
        print("Helytelen adat")
        a = input("Kérlek írd be mégegyszer: ")
    return a


def erettsegi_ellenorzo(a):
    while int(a) < 0 or int(a) > 100:
        print("Helytelen adat")
        a = input("Kérlek írd be mégegyszer: ")
    return a


def szoveg_ellenorzo(a, b):
    o = False
    a = input(b)
    while not o:
        try:
            int(a) + 1
        except:
            if len(a) >= 4:
                o = True
            else:
                print("Túl rövid adat")
                a = input("Add meg újra: ")
        else:
            print("Helytelen adat")
            a = input("Add meg újra: ")
    return a


class Erettsegi:
    szazalek = None

    def __init__(self, tan):
        self.tantargy = tan
        self.ellenorzo(self.szazalek, self.tantargy)

    def ellenorzo(self, a, b):
        k = False
        while not k:
            a = input(str(b) + " érettségi százaléka: ")
            try:
                a = erettsegi_ellenorzo(a)
                k = True
            except ValueError as e:
                print("Hibás adat")
        self.szazalek = a


class Evvegijegy:
    jegy = None

    def __init__(self, a, b):
        self.tantargy = a
        self.ev = b
        self.ellenorzo(self.jegy, self.tantargy, self.ev)

    def ellenorzo(self, a, b, c):
        # a: jegy, b: név, c: év
        k = False
        while not k:
            a = input(str(b) + c + "jegye: ")
            try:
                a = evvege_ellenorzo(a)
                k = True
            except ValueError as e:
                print("Hibás adat")
                k = False
        self.jegy = a


ue = " utolsó előtti év "
u = " utolsó év "

inyelv = ""
inyelv = szoveg_ellenorzo(inyelv, "Milyen idegen nyelvet tanultál? ")
term = ""
term = szoveg_ellenorzo(term, "Milyen természettudományos tárgyat választottál? ")

j1 = Evvegijegy("Irodalom", ue)
j2 = Evvegijegy("Nyelvtan", ue)
j3 = Evvegijegy("Történelem", ue)
j4 = Evvegijegy("Matematika", ue)
j5 = Evvegijegy(inyelv, ue)
j6 = Evvegijegy(term, ue)

print("")

j7 = Evvegijegy("Irodalom", u)
j8 = Evvegijegy("Nyelvtan", u)
j9 = Evvegijegy("Történelem", u)
j10 = Evvegijegy("Matematika", u)
j11 = Evvegijegy(inyelv, u)
j12 = Evvegijegy(term, u)

print("")

val_e = ""
val_e = szoveg_ellenorzo(val_e, "Mi volt a választott érettségi tantárgyad? ")

e1 = Erettsegi("Magyar")
e2 = Erettsegi("Történelem")
e3 = Erettsegi("Matematika")
e4 = Erettsegi(inyelv)
e5 = Erettsegi(val_e)


nyelvv = input("Nyelvvizsga: Közép/2 Közép/Felső/Nincs: ")
g = False
while not g:
    if nyelvv == "Közép":
        nyelvv = 28
        g = True
    elif nyelvv == "2 Közép":
        nyelvv = 40
        g = True
    elif nyelvv == "Felső":
        nyelvv = 40
        g = True
    elif nyelvv == "Nincs":
        nyelvv == 0
        g = True
    else:
        print("Helytelen adat")
        nyelvv = input("Próbáld újra: ")

e = False
while not e:
    emelt = input("Emeltek száma: ")
    try:
        while int(emelt) < 0 or int(emelt) > 5:
            print("Helytelen adat")
            emelt = input("Kérlek írd be mégegyszer: ")
        e = True
    except ValueError as hiba:
        print("Hibás adat")

evvege11 = (((int(j1.jegy) + int(j2.jegy)) / 2 + int(j3.jegy) + int(j4.jegy) + int(j5.jegy) + int(j6.jegy)) * 2)
evvege12 = (((int(j7.jegy) + int(j8.jegy)) / 2 + int(j9.jegy) + int(j10.jegy) + int(j11.jegy) + int(j12.jegy)) * 2)

hozott = evvege11 + evvege12

atlag = (int(e1.szazalek) + int(e2.szazalek) + int(e3.szazalek) + int(e4.szazalek) + int(e5.szazalek)) / 5

d = False
while not d:
    vitt1 = input("Mi az első kiemelt tárgyad? (" + e1.tantargy + "/" + e2.tantargy + "/" + e3.tantargy + "/" + e4.tantargy + "/" + e5.tantargy + ")")
    h = False
    while not h:
        if vitt1 == e1.tantargy:
            vitte1 = e1.szazalek
            h = True
        elif vitt1 == e2.tantargy:
            vitte1 = e2.szazalek
            h = True
        elif vitt1 == e3.tantargy:
            vitte1 = e3.szazalek
            h = True
        elif vitt1 == e4.tantargy:
            vitte1 = e4.szazalek
            h = True
        elif vitt1 == e5.tantargy:
            vitte1 = e5.szazalek
            h = True
        else:
            print("Helytelen adat")
            vitt1 = input("Kérlek add meg újra: ")

    vitt2 = input("Mi az második kiemelt tárgyad? (" + e1.tantargy + "/" + e2.tantargy + "/" + e3.tantargy + "/" + e4.tantargy + "/" + e5.tantargy + ")")
    t = False
    while not t:
        if vitt2 == e1.tantargy:
            vitte2 = e1.szazalek
            t = True
        elif vitt2 == e2.tantargy:
            vitte2 = e2.szazalek
            t = True
        elif vitt2 == e3.tantargy:
            vitte2 = e3.szazalek
            t = True
        elif vitt2 == e4.tantargy:
            vitte2 = e4.szazalek
            t = True
        elif vitt2 == e5.tantargy:
            vitte2 = e5.szazalek
            t = True
        else:
            print("Helytelen adat")
            vitt2 = input("Kérlek add meg újra: ")
    if vitt1 == vitt2:
        print("Nem lehet ugyan az a két tárgyad!")
    else:
        d = True

f = False
while not f:
    plusz = input("Egyéb pluszpontjaid(pontszámot adj meg kérlek): ")
    try:
        while int(plusz) < 0:
            print("Helytelen adat")
            plusz = input("Kérlek add meg mégegyszer: ")
        f = True
    except ValueError as hiba1:
        print("Hibás adat")

egyeb = int(plusz) + int(nyelvv) + int(emelt) * 50
if egyeb > 100:
    egyeb = 100

eredmeny1: int = int(hozott) + int(atlag) + int(vitte1) + int(vitte2) + int(egyeb)
eredmeny2: int = 2 * int(vitte1) + 2 * int(vitte2) + int(egyeb)

print(" ")
print("Hozott pontok: " + str(hozott))
print("Érettségik átlaga: " + str(atlag))
print("Első kiemelt érettségi pontja: " + str(vitte1))
print("Második kiemelt érettségi pontja:" + str(vitte2))
print("Egyéb pontok: " + str(egyeb))
# print(eredmeny1)
# print(eredmeny2)
print("")

print(max(eredmeny1, eredmeny2))

input("Nyomj meg egy gombot hogy kilépj")
