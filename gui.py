import pygame
from pygame.locals import *
from constants import *
from game import Game


class Gui:
    
    def __init__(self):
        pygame.init()
        self.game = Game()
        self.window = self.game.window
        self.fps_clock = pygame.time.Clock()
        self.loop_gui_menu = True
        self.loop_gui_message = True
        self.exit = True
        self.choice_gui_menu = 0
        self.choice_gui_message = 0

                ##PICTURES OF GUI MENU##
        self.mac = pygame.image.load(mac).convert_alpha()
        self.gyver = pygame.image.load(gyver).convert_alpha()
        self.logo = pygame.image.load(logo).convert_alpha()
        self.macgyver = pygame.image.load(macgyver_menu).convert_alpha()
        self.select_get_into_the_game = pygame.image.load(
            get_into_the_game).convert_alpha()
        self.chevron_select_left = pygame.image.load(
            chevron_left).convert_alpha()
        self.chevron_select_right = pygame.image.load(
            chevron_right).convert_alpha()
        self.enter = pygame.image.load(enter).convert_alpha()
        self.enter_small = pygame.image.load(enter_small).convert_alpha()
        self.exit = pygame.image.load(exit).convert_alpha()
        self.exit_small = pygame.image.load(exit_small).convert_alpha()
        self.info_menu = pygame.image.load(info_menu).convert_alpha()

                ##PICTURES OF GUI MESSAGE##
        self.you_won_img = pygame.image.load(you_won).convert_alpha()
        self.you_lost_img = pygame.image.load(you_lost).convert_alpha()
        self.continue_big = pygame.image.load(continue_big).convert_alpha()
        self.continue_small = pygame.image.load(continue_small).convert_alpha()
        

                ##SIZE OF GUI MENU##
        self.size_banner_mac = [600, 20]
        self.size_banner_gyver = [-174, 20]
        self.size_banner_macgyver = [147.5, 120]
        self.size_banner_logo = [50, 125]
        self.size_get_into_the_game = [120, -20]
        self.size_chevron_select_left = [-30, 320]
        self.size_chevron_select_right = [600, 320]
        self.size_enter = [175, 450]
        self.size_enter_small = [232.5, 465]
        self.size_exit = [200, 550]
        self.size_exit_small = [250, 565]
        self.size_info_menu = [125, 375]

                ##SIZE OF GUI MESSAGE##
        self.size = [120, 100]
        self.size_continue_big = [100, 450]
        self.size_continue_small = [200, 465]
       

     
    def run_gui_menu(self):
        pygame.mixer.music.load(soundtrack)
        pygame.mixer.music.play()
        while self.loop_gui_menu:
            if self.size_banner_mac[0] != 160:
                self.size_banner_mac[0] -= 2
            if self.size_banner_gyver[0] != 266:
                self.size_banner_gyver[0] += 2
            if self.size_get_into_the_game[1] != 320:
                self.size_get_into_the_game[1] += 2
            if self.size_chevron_select_left[0] != 80:
                self.size_chevron_select_left[0] += 1
            if self.size_chevron_select_right[0] != 490:
                self.size_chevron_select_right[0] -= 1        
            self.window.fill((0, 0, 0))
            self.draw_gui_menu()
            self.handle_events_gui_menu()
            pygame.display.update()
            self.fps_clock.tick(30)

    def draw_gui_menu(self):
        self.window.blit(self.mac, self.size_banner_mac)        
        self.window.blit(self.gyver, self.size_banner_gyver)
        self.window.blit(self.logo, self.size_banner_logo)
        self.window.blit(self.macgyver, self.size_banner_macgyver)
        self.window.blit(self.select_get_into_the_game,
                        self.size_get_into_the_game)        
        self.window.blit(self.chevron_select_left,
                        self.size_chevron_select_left)
        self.window.blit(self.chevron_select_right,
                        self.size_chevron_select_right)        
        self.window.blit(self.info_menu, self.size_info_menu)
        if self.choice_gui_menu == 0:
            self.window.blit(self.enter,self.size_enter)
            self.window.blit(self.exit_small, self.size_exit_small)
        if self.choice_gui_menu == 1:
            self.window.blit(self.enter_small, self.size_enter_small)
            self.window.blit(self.exit, self.size_exit) 
    
    def run_gui_message(self, result):
        while self.loop_gui_message:
            self.window.fill((0, 0, 0))
            self.window.blit(
                self.you_won_img if result == "win" 
                else self.you_lost_img, 
                self.size
            )
            if self.choice_gui_message == 0:
                self.window.blit(self.continue_big, self.size_continue_big)
                self.window.blit(self.exit_small, self.size_exit_small)
            if self.choice_gui_message == 1:
                self.window.blit(self.continue_small, self.size_continue_small)
                self.window.blit(self.exit, self.size_exit)
            self.handle_events_gui_message()
            pygame.display.update()
            self.fps_clock.tick(30)

    def handle_events_gui_menu(self):
        for event in pygame.event.get():
            self.handle_event_gui_menu(event)

    def handle_event_gui_menu(self, event):
        #Si l'utilisateur quitte, on met la variable qui continue le jeu
        #ET la variable générale à 0 pour fermer la fenêtre
        if event.type == QUIT:
            self.loop_gui_menu = False
        if event.type == KEYDOWN:
            if event.key in [13, 271, 32]:  # Enter or Spacebar
                if self.choice_gui_menu == 0:
                    self.choice_gui_menu = "enter" 
                    self.loop_gui_menu = False
                if self.choice_gui_menu == 1:
                    self.loop_gui_menu = False
                
            #Touches de déplacement du menu
            elif event.key == K_UP:
                self.choice_gui_menu = 0
            elif event.key == K_DOWN:
                self.choice_gui_menu = 1

    def handle_events_gui_message(self):
        for event in pygame.event.get():
            self.handle_event_gui_message(event)
                
    def handle_event_gui_message(self, event):
        #Si l'utilisateur quitte, on met la variable qui continue le jeu
        #ET la variable générale à 0 pour fermer la fenêtre
        if event.type == QUIT:
            self.loop_gui_message = False
            self.exit = False
        if event.type == KEYDOWN:
            if event.key in [13, 271, 32]:  # Enter or Spacebar
                if self.choice_gui_message == 0:
                    self.loop_gui_message = False
                if self.choice_gui_message == 1:
                    self.choice_gui_message = "exit"
                    self.loop_gui_message = False
            #Touches de déplacement du menu
            elif event.key == K_UP:
                self.choice_gui_message = 0
            elif event.key == K_DOWN:
                self.choice_gui_message = 1

    # méthode de réinitialisation 
    def re_init(self):
        pygame.init()
        self.game = Game()
        self.window = self.game.window
        self.fps_clock = pygame.time.Clock()
        self.loop_gui_menu = True
        self.loop_gui_message = True
        self.choice_gui_menu = 0
        self.choice_gui_message = 0
