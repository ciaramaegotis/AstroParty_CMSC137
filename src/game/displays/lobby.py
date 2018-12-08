import sys
import pygame as pg

# move up one directory to be able to import the images
sys.path.append("..")
from utils.button import Button
from utils.variables import *
from utils.images import *
from chat import Chat

class Lobby:
    def __init__(self, game, lobbyType):
        self.game = game
        # Create and join lobby 
        self.game.chat = Chat(self.game)
        if lobbyType == 'create':
            self.game.lobby_id = self.game.chat.createLobby(4).lobby_id
            self.game.chat.connectToLobby(self.game.lobby_id, self.game.username)
            self.game.createLobby(self.game.lobby_id, self.game.username)
        elif lobbyType == 'join':
            self.game.joinLobby(self.game.username)
        
        back = Button('backButton', 530, 600, 224, 64)
        start = Button('nextButton', 950, 600, 220, 63)
        
        message = ""
        while self.game.currentDisplay == PLAYER_CREATELOBBY or self.game.currentDisplay == PLAYER_JOINLOBBY:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.game.running = False
                    self.game.currentDisplay = MAIN_MENU
                    quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    if back.raw.get_rect(topleft=(back.x,back.y)).collidepoint(event.pos):
                        self.game.currentDisplay = MAIN_MENU
                        self.game.chatTranscript = []
                        break
                    elif start.raw.get_rect(topleft=(start.x,start.y)).collidepoint(event.pos):
                        self.game.getPlayers()
                        if self.game.currentPlayers >= 2:
                            self.game.startGame()
                            self.game.currentDisplay = GAMEPLAY
                        # break
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        try:
                            if(message == "dc()"):
                                self.game.disconnectChat(self.game.userID)
                            elif(message == "list()"):
                                self.game.chat.listPlayers()
                            else:
                                self.game.chat.sendMessage(message)
                        except OSError:
                            print("\nError")
                        done = True
                        message = ''
                    elif event.key == pg.K_BACKSPACE:
                        message = message[:-1]
                    else:
                        message += event.unicode
            self.game.getGame()
            if self.game.gameStart == 1:
                self.game.currentDisplay = GAMEPLAY
            # Render background elements
            self.game.screen.blit(menuBackground, (0,0))
            self.game.screen.blit(chatPanel, (-20, 33))
            self.game.screen.blit(waitOtherPlayers, (415, 70))
            self.game.screen.blit(player1, (600, 200))
            self.game.screen.blit(noPlayer, (900, 200))
            self.game.screen.blit(noPlayer, (600, 350))
            self.game.screen.blit(noPlayer, (900, 350))
            self.game.screen.blit(back.raw, (back.x, back.y))
            if lobbyType == 'create':
                self.game.screen.blit(start.raw, (start.x, start.y))
            
            self.game.getPlayers()
            if self.game.currentPlayers >= 2:
                self.game.screen.blit(player2, (900, 200))    
            if self.game.currentPlayers == 3:
                self.game.screen.blit(player2, (900, 200))  
                self.game.screen.blit(player3, (600, 350))
            if self.game.currentPlayers == 4:
                self.game.screen.blit(player2, (900, 200))  
                self.game.screen.blit(player3, (600, 350))
                self.game.screen.blit(player4, (900, 350))

        
            # Render Chat elements
            font = pg.font.Font(None, 28)
            input_box = pg.Rect(10, 655, 380, 30)
            color = pg.Color("white")
            pg.draw.rect(self.game.screen, pg.Color("white"), input_box, 2)
            # Print text in chat box
            if (len(message) > 25):
                message = message[0:28]
                txt_surface = font.render(message, True, pg.Color("white"))
                self.game.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
            else:
                txt_surface = font.render(message, True, pg.Color("white"))
                self.game.screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

            # Print text in chat panel
            start_y = 50
            panelFont = pg.font.Font(None, 25)
            for content in self.game.chatTranscript:
                label = panelFont.render(content, 1, (255,255,255))
                self.game.screen.blit(label, (20, start_y))
                start_y += 20
        
            pg.display.flip()