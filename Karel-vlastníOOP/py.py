from time import sleep
from tkinter import messagebox
from random import randint

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

# mesto
mesto = []
for i in range(VELIKOST_MESTA):
        mesto.append([])
        for j in range(VELIKOST_MESTA):
                mesto[i].append(0)


def vykresliMesto():
        for y in range(VELIKOST_MESTA-1, -1, -1):
            print("")
            for x in range(VELIKOST_MESTA):
                    if ivan.x == y and ivan.y == x:
                        print(iZnaky[ivan.smer-1], end='')
                    elif mesto[x][y] < 10:
                        print(mesto[x][y], end='')
                    else:
                        print("▓", end='')
                    print(" ", end='')
        sleep(0.5)
        print()


# ivan
class Ivan:
        smer = 4
        x = 0
        y = 0
        def __init__(self):
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

        def krok(self):
                if Zed(True):
                        messagebox.showerror("Ivan má problém", "Narazil jsem, AU!")
                elif self.smer == 1:
                        self.x += 1
                elif self.smer == 2:
                        self.y -= 1
                elif self.smer == 3:
                        self.x -= 1
                else:
                        self.y += 1

        def poloz(self):
                if jeZnacka(9):
                        messagebox.showerror("Ivan má problém", "Není kam položit!")
                else:
                        mesto[self.y][self.x] = mesto[self.y][self.x] + 1
        def zvedni(self):
                if jeZnacka(0):
                        messagebox.showerror("Ivan má problém", "Není co zvednout!")
                else:
                        mesto[self.y][self.x] = mesto[self.y][self.x] - 1

ivan = Ivan

iZnaky = ("┴", "┤", "┬", "├")

# funkce
def opakuj(n, prikazy):
        for i in range(n):
                for subprikaz in prikazy:
                        vykonej(subprikaz)

def kdyz(podminka, prikazy):
        if type(podminka) == list:
                if podminka[0](podminka[1]):
                        for subprikaz in prikazy:
                                vykonej(subprikaz)
        else:
                if podminka():
                        for subprikaz in prikazy:
                                vykonej(subprikaz)

def dokud(podminka, n, prikazy):
        opakuj(n, kdyz(podminka, prikazy))

def vypisSlovnik(nepotrebne):
        for slovo in slovnik:
                print(slovo)
def end(nepotrebne):
        if messagebox.askokcancel("Tak to je konec", "Chete opravu Ivana ukončit?"):
                pokracuj = False


# podminky
def Zed(je):
        zed = False
        if ivan.smer == 1:
                if ivan.x == VELIKOST_MESTA-1 or mesto[ivan.x+1][ivan.y] == 255:
                        zed = True
        elif ivan.smer == 4:
                if ivan.y == VELIKOST_MESTA-1 or mesto[ivan.x][ivan.y+1] == 255:
                        zed = True
        elif ivan.smer == 3:
                if ivan.x == 0 or mesto[ivan.x-1][ivan.y] == 255:
                        zed = True
        elif ivan.smer == 2:
                if ivan.y == 0 or mesto[ivan.x][ivan.y-1] == 255:
                        zed = True
        if je:
                return zed
        else:
                return not zed



def jeZnacka(pocet):
        if mesto[ivan.y][ivan.x] == pocet:
                return True
        else:
                return False

def nahoda():
        return randint(1)


slovnik = {"end": end, "slovnik": vypisSlovnik, "krok": ivan.krok, "vlevo_vbok": ivan.vlevo_vbok, "poloz": ivan.poloz, "zvedni": ivan.zvedni, "opakuj:": opakuj,
           "4krok": [opakuj, 4, [ivan.krok]], "vp": [opakuj, 3, [ivan.vlevo_vbok]], "?krok": [kdyz, [jeZnacka,  3], [ivan.krok]]}


def vykonej(prikaz):
        if type(prikaz) == list:
                if prikaz[0] == opakuj or kdyz:
                        prikaz[0](prikaz[1], prikaz[2])
                elif prikaz[0] == dokud:
                        dokud(prikaz[1], prikaz[2], prikaz[3])
                else:
                        for subprikaz in prikaz:
                                vykonej(subprikaz)
        else:
                prikaz(ivan)
                vykresliMesto()


# main

print(ivan.smer)

pokracuj = True
vykresliMesto()
while pokracuj:
        pozadavek = "Zadej prikaz: "

        vstup = input(pozadavek)
        if vstup in slovnik:
                vykonej(slovnik[vstup])


