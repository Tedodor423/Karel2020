from time import sleep
from tkinter import messagebox, Tk
from random import randint
import re
import keyboard
import sys

from tkinter.filedialog import askopenfilename

#Tk().withdraw()  # neobjeví se okno tkinteru

sys.setrecursionlimit(2000)  # S TÍMHLE OPATRNĚ!!!!!!!

def vykresliMesto():
        for y in range(VELIKOST_MESTA-1, -1, -1):
            print("")
            for x in range(VELIKOST_MESTA):
                    if karel.x == y and karel.y == x:
                        print(iZnaky[karel.smer-1], end='')
                    elif mesto[x][y] < 10:
                        print(mesto[x][y], end='')
                    else:
                        print("▓", end='')
                    print(" ", end='')

        print()


# karel
class Karel:
        smer = 4
        x = 0
        y = 0

        def __init__(self):

                # zacni vlevo dole otoceny na vychod
                self.smer = 4
                """
                sever  - 1
                jih    - 3
                vychod - 4
                zapad  - 2
                """
                self.x = 1
                self.y = 1

        def vlevo_vbok(self):
                if self.smer == 4:
                        self.smer = 1
                else:
                        self.smer = self.smer + 1
                return True

        def krok(self):
                if podminka.zed([True]):
                        messagebox.showerror("Karel má problém", "Narazil jsem, AU!")
                        return False
                elif self.smer == 1:
                        self.x += 1
                elif self.smer == 2:
                        self.y -= 1
                elif self.smer == 3:
                        self.x -= 1
                else:
                        self.y += 1
                return True

        def poloz(self):
                if podminka.pocetZnacek([9, True]):
                        messagebox.showerror("Karel má problém", "Není kam položit!")
                        return False
                else:
                        mesto[self.y][self.x] = mesto[self.y][self.x] + 1
                return True

        def zvedni(self):
                if podminka.znacka([False]):
                        messagebox.showerror("Karel má problém", "Není co zvednout!")
                        return False
                else:
                        mesto[self.y][self.x] = mesto[self.y][self.x] - 1
                return True

karel = Karel

iZnaky = ("┴", "┤", "┬", "├")


# funkce
class Funkce():
        def opakuj(self, n, prikazy):
                if n == -1:  # nekonecnekrat
                        while True:
                                for subprikaz in prikazy:
                                        if not prikaz.vykonej(subprikaz):
                                                return False
                for i in range(n):
                        for subprikaz in prikazy:
                                if not vykonej(subprikaz):
                                        return False
                return True


        def kdyz(self, podminka, prikazy, altPrikazy):
                if podminka[0](podminka[1]):  # podminka[1] jsou parametry
                        for subprikaz in prikazy:
                                if not prikaz.vykonej(subprikaz):
                                        return 0  # neco je spatne
                        return 1  # podminka splnena
                else:
                        for subprikaz in altPrikazy:
                                if not prikaz.vykonej(subprikaz):
                                        return 0  # neco je spatne
                return 2  # podminka nesplnena


        def dokud(self, podminka, prikazy):
                pokud = funkce.kdyz(podminka, prikazy, [])
                if pokud == 1:
                        funkce.dokud(podminka, prikazy)
                elif pokud == 0:
                        return False
                return True


        def vypisSlovnik(self, foo):
            for slovo in slovnik:
                print(slovo)
            return True

        def doslovaVypisSlovnik(self, foo):
            print(slovnik)


        def chyba(self, foo):
                global slovnik
                if len(slovnik) > indexPPP+1:
                        print("ZRUŠENO " + list(slovnik.keys())[-1].upper())
                        slovnik.popitem()
                else:
                        messagebox.showerror("Karel má problém", "Není co odebrat!")
                return True

funkce = Funkce()


class Podminky():
                def __init__(self):
                        # "jmeno podminky": [podminka, [parametry podminky]]
                        slovnikPodminek = {"nahoda": [self.nahoda, []], "znacka": [self.znacka, []], "sever": [self.smer, [1]], "zapad": [self.smer, [2]],
                           "jih": [self.smer, [3]], "vychod": [self.smer, [4]], "zed": [self.zed, []]}

                        for i in range(10):
                                slovnikPodminek[str(i)] = [self.pocetZnacek, [i]]
                
                # podminky
                def zed(self, je):
                        zed = False

                        # podle smeru
                        if karel.smer == 1:
                                if karel.x == VELIKOST_MESTA-1 or mesto[karel.x+1][karel.y] == 255:
                                        return je[0]
                        elif karel.smer == 4:
                                if karel.y == VELIKOST_MESTA-1 or mesto[karel.x][karel.y+1] == 255:
                                        return je[0]
                        elif karel.smer == 3:
                                        if karel.x == 0 or mesto[karel.x-1][karel.y] == 255:
                                                return je[0]
                        elif karel.smer == 2:
                                if karel.y == 0 or mesto[karel.x][karel.y-1] == 255:
                                        return je[0]
                        return je[0] == False  # NOT gate


                def znacka(self, je):
                        if mesto[karel.y][karel.x] != 0:
                                return je[0]
                        else:
                                return je[0] == False  # NOT gate



                def pocetZnacek(self, pocet):
                        if mesto[karel.y][karel.x] == pocet[0]:
                                return pocet[1]  # pocet[1] je True/False
                        else:
                                return pocet[1] == False  # NOT gate


                def smer(self, smer):
                        if smer[0] == karel.smer:
                                return smer[1]  # smer[1] je True/False
                        else:
                                return smer[1] == False  # NOT gate


                def nahoda(self, je):
                        return je[0] == randint(1)

podminka = Podminky()  

slovnik = {"slovnik": funkce.vypisSlovnik, "chyba": funkce.chyba, "vyskoc": "vyskoc", "krok": karel.krok,
           "vlevo_vbok": karel.vlevo_vbok, "poloz": karel.poloz, "zvedni": karel.zvedni,
           "ke_zdi": [[funkce.dokud, [podminka.zed, [False]], [karel.krok]]]}
indexPPP = len(slovnik)-1  # index Posledniho Permanentniho Prikazu


class Prikaz():
        def __init__(self):
                self.odsazeni = 0
                self.posledniPrikaz = {}
                
        def vykonej(self, prikaz):
                if type(prikaz) == str:
                        prikaz = slovnik[prikaz]

                if type(prikaz) == list:
                        if prikaz[0] in (funkce.opakuj, funkce.dokud):
                                if not prikaz[0](prikaz[1], prikaz[2]):  # prikaz[1] je podminka/pocet iteraci, prikaz[2] jsou prikazy pro vykonani
                                        return False
                        elif prikaz[0] == funkce.kdyz:
                                if not prikaz[0](prikaz[1], prikaz[2], prikaz[3]):  # prikaz[3] jsou alternativni prikazy pro pripad nesplneni podminky
                                        return False
                        else:
                                for subprikaz in prikaz:
                                        if subprikaz == "vyskoc":
                                                return True
                                        elif not prikaz.vykonej(subprikaz):
                                                return False
                else:  # jeden ze zakladnich prikazu
                    if not prikaz(karel):
                            return False
                    vykresliMesto()

                    # počkej, při stisknutí esc ukonči příkaz, manipulace rychlosti
                    global rychlost
                    for i in range(rychlost):
                            if keyboard.is_pressed('esc'):
                                return False
                            elif keyboard.is_pressed('shift') and rychlost > 5:
                                rychlost -= 1
                            elif keyboard.is_pressed('alt'):
                                rychlost += 1
                            elif keyboard.is_pressed('tab'):
                                if rychlost != 1:
                                        rychlost = 1
                            elif not keyboard.is_pressed('tab') and rychlost == 1:
                                rychlost = defRychlost
                            sleep(rychlost/defRychlost/100)
                return True


        # prida novou radku se spravnym odsazenim do listu s vypsanym prikazem
        def vypisPrikaz(self, radek):

                if radek != "":
                        self.posledniPrikaz[radek] = self.odsazeni
                else:  # pokud je vstupni parametr prazdny vymaz posledni radku

                        for i in self.posledniPrikaz.values()[:-1]:
                                i %= 100


                for prikaz in self.posledniPrikaz.keys():
                        print(prikaz + (self.posledniPrikaz[prikaz] % 100) * "  ")
                print()


        def novyPrikaz(self):
                prikaz = []
                
                while True:
                        vstup = input("Zadej známý příkaz: ")

                # matchování zkratek k slovníku
                if vstup.endswith("."):
                        nenasel = True
                        for slovo in slovnik:
                                if slovo.startswith(vstup[:-1]):
                                        vstup = slovo
                                        nenasel = False
                                        break
                        if nenasel:
                                messagebox.showerror("Karel má problém", vstup + ". neznám!")

                if vstup == "konec" or vstup == "":  # "" znamena enter
                        self.odsazeni -= 1
                        vypisPrikaz("KONEC")
                        return prikaz

                elif vstup == "chyba":
                        if not len(prikaz):
                                return False  # zrus cely novyPrikaz()
                        else:
                            prikaz.pop()
                            vypisPrikaz("")

                elif vstup.startswith("opakuj"):  # tvar: [opakuj, pocet_iteraci, prikazy]
                        prikaz.append([])
                        prikaz[-1].append(opakuj)

                        # zkus najit prvni prirozene cislo napsane po "opakuj " (vse ostatni ignoruj)
                        if re.match("(opakuj [0-9]{1,3}).*", vstup):
                                n = int(re.search("[0-9]{1,4}", vstup).group())

                        else:  # nenasel
                                # zjisti pocet iteraci sam
                                while True:
                                        try:
                                                n = int(input("Kolikrát? "))
                                                break
                                        except ValueError:
                                                messagebox.showerror("Karel má problém", "Jen přirozená čísla!")
                        # pokud vetsi nez 999 tak nekonecnekrat
                        if n > 999:
                                n = -1

                        prikaz[-1].append(n)

                        if n == -1:
                                vypisPrikaz("OPAKUJ NEKONECNE KRAT:")
                        else:
                                vypisPrikaz("OPAKUJ " + str(n) + "KRAT:")
                        self.odsazeni += 1

                        # prikazy pro vykonani
                        subPrikaz = novyPrikaz()
                        if subPrikaz:
                                prikaz[-1].append(subPrikaz)
                        else:
                                prikaz.pop()
                                self.odsazeni -= 1
                                vypisPrikaz("")

                elif vstup.startswith("kdyz"):  # tvar: [kdyz, [podminka, [parametry_podminky]], prikazy, alternativni_prikazy]
                        prikaz.append([])
                        prikaz[-1].append(kdyz)

                        je = True
                        podminka = []
                        validniPodminka = False

                        if re.match("kdyz ((je)|(neni)) ([0-9]|[a-zA-Z]{1,10})", vstup):  # matchuje s tvarem
                                # je/neni
                                if vstup[5:].startswith("neni"):
                                        je = False

                                # podminka
                                vstup = vstup[(8 + int(je == False) * 2):]  # odriznuti podminky od zbytku

                                # matchovani se slovnikem (i zkratek)
                                for slovo in slovnikPodminek:
                                        if vstup == slovo:
                                                podminka = slovnikPodminek[slovo]
                                                validniPodminka = True
                                if not validniPodminka:
                                        messagebox.showerror("Ty máš problém", vstup + " není validní podmínka")

                        if not validniPodminka:  # nematchuje s tvarem nebo neexistujici podminka
                                # zjisti podminku sam
                                    # podminka
                                while True:
                                        vstup = input("Když co: ")
                                        validniPodminka = False

                                        # matchovani se slovnikem (i zkratek)
                                        for slovo in slovnikPodminek:
                                                if (vstup.endswith(".") and slovo.startswith(vstup[:-1])) or vstup == slovo:
                                                        podminka = slovnikPodminek[slovo]
                                                        validniPodminka = True

                                        if not validniPodminka:
                                                messagebox.showerror("Ty máš problém", vstup + " není validní podmínka")

                                        else:
                                                break
                                    # je/neni
                                while True:
                                        vstup = input("je/není: ")
                                        if vstup == "j." or vstup == "je" or vstup == "":
                                            je = True
                                            break
                                        elif (vstup.endswith(".") and "neni".startswith(vstup[:-1])) or "neni" == vstup:
                                            je = False
                                            break
                                        messagebox.showerror("Ty máš problém", "Piš jen \"je\" nebo \"není\"")

                        podminka[:-1].append(je)
                        prikaz[-1].append([podminka])

                        if je:
                                vypisPrikaz("KDYZ JE " + vstup.upper() + ":")
                        else:
                                vypisPrikaz("KDYZ NENI " + vstup.upper() + ":")

                        self.odsazeni += 1

                        # prikazy pro vykonani
                        subPrikaz = novyPrikaz()
                        if subPrikaz:
                                prikaz[-1].append(subPrikaz)
                                # jinak

                                vypisPrikaz("JINAK:")
                                self.odsazeni += 1

                                # prikazy pro jinak vykonani
                                subPrikaz = novyPrikaz()
                                if subPrikaz:
                                        prikaz[-1].append(subPrikaz)
                                else:
                                        prikaz.pop()
                                        self.odsazeni -= 1
                                        vypisPrikaz("")
                        else:
                                prikaz.pop()
                                self.odsazeni -= 1
                                vypisPrikaz("")

                elif vstup.startswith("dokud"):
                        prikaz.append([])
                        prikaz[-1].append(dokud)

                        je = True
                        podminka = []
                        validniVstup = False

                        # podminka
                        if re.match("dokud ((je)|(neni)) ([0-9]|[a-zA-Z]{1,10})", vstup):
                                if vstup[6:].startswith("je"):
                                        validniVstup = True
                                elif vstup[6:].startswith("neni"):
                                        je = False
                                        validniVstup = True
                                else:
                                        messagebox.showerror("Ty máš problém", vstup[6:] + " není validní podmínka")
                                if validniVstup:
                                        vstup = vstup[(9 + int(je == False) * 2):]  # odriznuti podminky od zbytku

                                        validniPodminka = False

                                        for slovo in slovnikPodminek.keys():
                                                if vstup == slovo:
                                                        podminka = slovnikPodminek[slovo]
                                                        validniPodminka = True
                                        if not validniPodminka:
                                                messagebox.showerror("Ty máš problém", vstup + " není validní podmínka")
                                                validniVstup = False

                        if not validniVstup:
                                while True:
                                        vstup = input("Dokud co: ").lower()

                                        validniPodminka = False

                                        for slovo in slovnikPodminek:
                                                if (vstup.endswith(".") and slovo.startswith(
                                                        vstup[:-1])) or vstup == slovo:
                                                        podminka = slovnikPodminek[slovo]
                                                        validniPodminka = True
                                        if not validniPodminka:
                                                messagebox.showerror("Ty máš problém", vstup + " není validní podmínka")
                                                validniVstup = False
                                        else:
                                                break
                                while True:
                                        vstup = input("je/není: ").lower()
                                        if vstup == "j." or vstup == "je" or vstup == "":
                                                break
                                        elif (vstup.endswith(".") and "neni".startswith(vstup)) or "neni" == vstup:
                                                je = False
                                                break
                                        messagebox.showerror("Jen \"je\" nebo \"není\"")

                        podminka[-1].append(je)
                        prikaz[-1].append(podminka)

                        if je:
                                vypisPrikaz("DOKUD JE " + vstup.upper() + ":")
                        else:
                                vypisPrikaz("DOKUD NENI " + vstup.upper() + ":")

                        self.odsazeni += 1

                        # prikazy pro vykonani
                        subPrikaz = novyPrikaz()
                        if subPrikaz:
                                prikaz[-1].append(subPrikaz)
                        else:
                                prikaz.pop()

                elif vstup in slovnik and vstup != "slovnik":
                        vypisPrikaz(vstup.upper())
                        prikaz.append(slovnik[vstup])
                else:
                        messagebox.showerror("Karel má problém", vstup + " neznám!")

prikaz = Prikaz()


# definovani velikosti mesta
dobraV = False
tempVelikost = int(input("Zadej velikost mesta: "))
while not dobraV:
        if tempVelikost > 25:
                tempVelikost = int(input("Město nemůže být větší než 25!\nZadej velikost mesta: "))
                dobraV = False
        else:
                dobraV = True
VELIKOST_MESTA = tempVelikost

# vytvor 2d pole (mesto)
mesto = []
for i in range(VELIKOST_MESTA):
        mesto.append([])
        for j in range(VELIKOST_MESTA):
                mesto[i].append(0)

print(karel.smer)

pokracuj = True
vykresliMesto()

defRychlost = 75
rychlost = defRychlost

prikazy = []

while pokracuj:
        vstup = input("Zadej příkaz: ")

        # matchování zkratek k slovníku
        if vstup.endswith("."):
                nenasel = True
                for slovo in slovnik:
                        if slovo.startswith(vstup[:-1]):  # pokud slovo ve slovníku začíná zkratkou
                                vstup = slovo
                                nenasel = False
                                break
                if nenasel:
                        messagebox.showerror("Karel má problém", vstup + " neznám!")

        if vstup == "end":
                if messagebox.askokcancel("Tak to je konec", "Chete opravu Karla ukončit?"):
                        pokracuj = False
        elif vstup in slovnik:
                prikaz.vykonej(vstup)
        elif vstup.startswith("opakuj") or vstup.startswith("kdyz") or vstup.startswith("dokud"):
                messagebox.showerror("Karel má problém", vstup + " teď nemohu!")
        elif vstup == "":
                pass
        else:
                # indexPVP = 0  # index posledního vypraného příkazu
                prikaz.vypisPrikaz("\nNOVÝ PŘÍKAZ " + vstup.upper() + ":")
                slovnik[vstup] = []

                prikaz.odsazeni += 1

                neueWeisung = prikaz.novyPrikaz()
                if neueWeisung:
                        slovnik[vstup] = neueWeisung
                else:
                        print("ZRUŠENO " + vstup.upper())
                        slovnik.pop(vstup)
                        prikaz.odsazeni -= 1

        # print(slovnik)


