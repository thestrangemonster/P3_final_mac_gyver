#!/usr/bin/python
# coding: utf-8

# importation du fichier gui.py, puis on cible la class Gui()
from gui import Gui
# importation du fichier game.py, puis on cible la class Game()
from game import Game
import pygame
from pygame.locals import *


def main():
    # initialisation de pygame
    pygame.init()
    # instance de class
    game = Game()
    gui = Gui()
    # variable pour la boucle while
    run_game = True
    # tant que run_game == True la boucle s'effectue
    while run_game:
        # dans mon fichier gui.py j'appel à l'aide de mon instance gui la méthode run_gui_menu 
        # qui s'execute en lançant le menu
        gui.run_gui_menu()
        # dans mon menu SI je choisi entrer:
        if gui.choice_gui_menu == "enter":
            # dans mon fichier game.py j'appel à l'aide de mon instance game la méthode run
            # qui lance le jeu
            game.run()

            if game.result == "you won!":
                gui.run_gui_message("win")
                if gui.choice_gui_message == "exit" or gui.exit == False:  
                    return
            if game.result == "you lose!":
                gui.run_gui_message("lose")
                if gui.choice_gui_message == "exit" or gui.exit == False:  
                    return
            gui.re_init()
            game.re_init()
            if game.exit == False:
                run_game = False
        else:
            run_game = False

if __name__ == "__main__":
    main()

"""
if __name__ == '__main__' est un idiome

"""
