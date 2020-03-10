#!/usr/bin/python
# coding: utf-8

#Importation des bibliothèques nécessaires
import pygame
from pygame.locals import *
from random import randint
from constants import *


class Maze:  # class labyrinthe

    def __init__(self, files):  # initialiser
        pygame.init()
        # variable qui servira à stocker mon fichier *maze*
        self.files = files
        # variable data qui me permettra de stocker mon labyrinthe généré conteneur 
        self.data = None
        # dictionnaire contenant mes images 
        self.images = {}
        self.images["W"] = pygame.image.load(PICTURE_WALL).convert()
        self.images["M"] = pygame.image.load(PICTURE_EMPTY).convert()
        self.images["G"] = pygame.image.load(
            PICTURE_GUARDIAN).convert_alpha()
        self.images["S"] = pygame.image.load(PICTURE_SYRINGE).convert_alpha()
        self.images["N"] = pygame.image.load(PICTURE_NEEDLE).convert_alpha()
        self.images["T"] = pygame.image.load(PICTURE_TUBE).convert_alpha()
        self.images["E"] = pygame.image.load(PICTURE_EMPTY).convert_alpha()
        self.images["I"] = pygame.image.load(PICTURE_EMPTY).convert_alpha()
        self.images["O"] = pygame.image.load(PICTURE_EMPTY).convert_alpha()
        self.images["B"] = pygame.image.load(PICTURE_BAG).convert_alpha()
        self.images["A"] = pygame.image.load(PICTURE_BAG2).convert_alpha()
        
    def generate(self):  # générer
        # j'ouvre mon fichier *maze*
        with open(self.files) as f:
            print(f)
            # je le lis et je lui demande de stocker le tout dans ma variable data 'string'
            self.data = f.read()
            # je remplace les espace ainsi que les saut de ligne en les supprimant afin de les préparer pour en faire une liste
            self.data = self.data.replace(" ", "").replace("\n", "")
            # je créé ma liste à l'aide d'une méthode de structure de donnée list
            self.data = list(self.data)

    def draw(self, window):  # afficher
        
        x = 0  # ligne des abscisses
        y = 0  # ligne des ordonnées
        # permet d'iterer envoi un tuple et la virgule permet de decompacter le tuple  k 
        # commence à 0 jusqu'a n-1
        for k, tile in enumerate(self.data):
            window.blit(self.images[tile], (x, y))
            # lorsque je passe un sprite j'ajoute la longueur d'un sprite pour passer au 
            # suivant
            x += HEIGHT_OF_SPRITE
            # si lors de mon itération k+1 modulo de la taille d'une ligne complète de 
            # sprite == 0
            if (k+1) % NB_OF_SPRITE == 0:
                # lorsque j'arrive à la fin d'une longueur total de sprite sur une ligne je 
                # remet les compteur de l'abscisse à 0 et j'ajoute la longueur d'un sprite à 
                # l'ordonnée afin de passer à la ligne suivante dans la modélisation graphique 
                # du labyrinthe
                y += HEIGHT_OF_SPRITE
                x = 0



    # méthode qui permet de me renvoyer la position de mac gyver 
    def get_mc_pos(self):
        return self.data.index("M")

    # méthode qui permet de placer aléatoirement les items avec la méthode randint 
    def random_items(self):
        
        for item in ("S", "N", "T"):
            while True:
                pos = randint(0, 224)
                if self.data[pos] == "E":
                    self.data[pos] = item
                    break

    def get_item_pos(self):
        return self.data.index("O")
    
    

