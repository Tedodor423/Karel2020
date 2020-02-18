from time import sleep
from tkinter import messagebox

import pygame
pygame.init()

# obrazky
ivanSObr = pygame.image.load("obrazky\Ivan-S.png")
ivanJObr = pygame.image.load("obrazky\Ivan-J.png")
ivanVObr = pygame.image.load("obrazky\Ivan-V.png")
ivanZObr = pygame.image.load("obrazky\Ivan-Z.png")
karloveObr = [ivanSObr, ivanVObr, ivanJObr, ivanZObr]

zedObr = pygame.image.load("obrazky\zed.png")

znackyObr = []
for i in range(10):
        znackyObr.append(pygame.image.load("obrazky\znacka" + str(i) + ".png"))

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

dvelikost = VELIKOST_MESTA * 65

# mesto
mesto = []
for i in range(VELIKOST_MESTA):
        mesto.append([])
        for j in range(VELIKOST_MESTA):
                mesto[i].append(0)


def vykresliMesto():
        for i in mesto:
                print(mesto.index(i))
                for j in i:
                        if i[j] < 10:
                                win.blit(znackyObr[i[j]], (mesto.index(i)*64 + mesto.index(i), j*64 + j))
                        else:
                                win.blit(zedObr, (mesto.index(i) * 64 + mesto.index(i), j * 64 + j))
                pygame.display.flip()
        win.blit(karloveObr[ivan.smer], (ivan.x*64+ivan.x, ivan.y*64+ivan.y))

# ivan
class Ivan:
        def __init__(self):
                self.smer = 2
                """
                sever  - 1
                jih    - 3
                vychod - 2
                zapad  - 4
                """
                self.x = 1
                self.y = 1

        def vlevo_vbok(self):
                if self.smer == 1:
                        self.smer = 4
                else:
                        self.smer = self.smer - 1

        def krok(self):
                if jeZed():
                        messagebox.showerror("Ivan má problém", "Narazil jsem, AU!")
                elif self.smer == 1:
                        self.x = self.x + 1
                elif self.smer == 2:
                        self.x = self.y + 1
                elif self.smer == 3:
                        self.y = self.x - 1
                else:
                        self.y = self.y - 1

        def poloz(self):
                if mesto[self.x][self.y] >= 9:
                        messagebox.showerror("Ivan má problém", "Není kam položit!")
                    return
                mesto[self.x][self.y] = mesto[self.x][self.y] + 1
        def zvedni(self):
                if jeZnacka(0):
                        messagebox.showerror("Ivan má problém", "Není co zvednout!")
                    return
                mesto[self.x][self.y] = mesto[self.x][self.y] - 1

ivan = Ivan

# funkce
def opakuj(n, prikazy):
        for i in range(n):
                for subprikaz in prikazy:
                        vykonej(subprikaz)

def kdyz(podminka, prikazy):
        if type(podminka) == list and podminka[0](podminka[1]) or podminka():
                for subprikaz in prikazy:
                        vykonej(subprikaz)

def dokud(podminka, n, prikazy):
        for i in range(n):
                if not podminka():
                        return
                for subprikaz in prikazy:
                        vykonej(subprikaz)

def vypisSlovnik():
        for slovo in slovnik:
                print(slovo)


# podminky
def Zed(je):
        zed = False
        if ivan.smer == 1:
                if mesto[ivan.x+1][ivan.y] == 255:
                        zed = True
        elif ivan.smer == 2:
                if mesto[ivan.x][ivan.y+1] == 255:
                        zed = True
        elif ivan.smer == 3:
                if mesto[ivan.x-1][ivan.y] == 255:
                        zed = True
        elif ivan.smer == 4:
                if mesto[ivan.x][ivan.y-1] == 255:
                        zed = True
        if je:
                return zed
        else:
                return not zed



def jeZnacka(pocet):
        if mesto[ivan.x][ivan.y] == pocet:
                return True
        else:
                return False


slovnik = {"slovnik":vypisSlovnik, "krok":ivan.krok, "vlevo_vbok":ivan.vlevo_vbok, "poloz":ivan.poloz, "zvedni":ivan.zvedni, "opakuj:":opakuj}


def vykonej(prikaz):
        if type(prikaz) == list:
                if prikaz[0] == opakuj or kdyz:
                        prikaz[0](prikaz[1], prikaz[2])
                elif prikaz[0] == dokud:
                        dokud(prikaz[1], prikaz[2], prikaz[3])
                else:
                        for subprikaz in slovnik[prikaz]:
                                vykonej(subprikaz)
        else:
                slovnik[prikaz]()


# okno
win = pygame.display.set_mode((dvelikost, dvelikost))
win.fill((0, 128, 255))
pygame.display.set_caption("Robot Ivan  - 2019")
vykresliMesto()
sleep(5)


# main

pokracuj = True
while pokracuj:
        pozadavek = "Zadej prikaz: "

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        pokracuj = False

        vstup = input(pozadavek)
        if vstup in slovnik:
                vykonej(vstup)

