#! /usr/bin/python

from proto.tcp_packet_pb2 import TcpPacket
# from threading import Thread
import socket
from sys import stdout
from threading import Thread
import pygame as pg

syntax = "proto2"

screen = pg.display.set_mode((850, 450))
bg = pg.image.load("./images/background.jpeg")
clock = pg.time.Clock()
current_num_of_players = 0
chat_transcript = []

def gameProper():
    while (True):
        screen.blit(bg, (0, 0))
        chat_panel = pg.image.load("./images/chat_panel.png");
        chat_panel = pg.transform.scale(chat_panel, (250, 440))
        screen.blit(chat_panel, (5, 5))
        pg.display.flip()
        clock.tick(30)

        font = pg.font.Font(None, 20)
        input_box = pg.Rect(20, 400, 220, 40)
        message = ""
        color = pg.Color("white")
        #listen to the start button and to the chatbox and to the incoming players
        while (True):
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    quit()
                    break
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        #send the message
                        try:
                            if(message == "dc()"):
                                chat_disconnect.player.name = username
                                sock.send(chat_disconnect.SerializeToString())
                                isBreak = True
                                quit()
                            elif(message == "list()"):
                                playersList = listPlayers()
                                for player in playersList:
                                    print(player)
                                print(">> ", end='')
                            else:
                                chat_send.message = message
                                sock.send(chat_send.SerializeToString())
                        except OSError:
                            print("\nError")
                        done = True
                        message = ''
                    elif event.key == pg.K_BACKSPACE:
                        message = message[:-1]
                    else:
                        message += event.unicode
            screen.blit(bg, (0, 0))
            screen.blit(chat_panel, (5, 5))
            #split the display in the chat box if length exceeds 22
            if (len(message) > 25):
                start_y = 0
                for i in range(0, len(message), 25):
                    output = message[i:i+25]
                    txt_surface = font.render(output, True, pg.Color("white"))
                    screen.blit(txt_surface, (input_box.x+5, input_box.y+5+start_y))
                    start_y += 15
            else:
                txt_surface = font.render(message, True, pg.Color("white"))
                screen.blit(txt_surface, (input_box.x+5, input_box.y+5))

            global chat_transcript
            start_y = 30
            myfont = pg.font.SysFont("monospace", 15)
            toPrint = []
            for content in chat_transcript:
                if len(content) > 22:
                    for i in range(0, len(content), 22):
                        toPrint.append(content[i:i+22])
                    for i in toPrint:
                        label = myfont.render(i, 1, (255,255,255))
                        screen.blit(label, (30, start_y))
                        start_y += 20
                    toPrint = []
                else:
                    label = myfont.render(content, 1, (255,255,255))
                    screen.blit(label, (30, start_y))
                    start_y += 20
            # for trans in chat_transcript:
            #     label = myfont.render(trans, 1, color)
            #     screen.blit(label, (20, start_y))
            #     start_y += 20
            #width = max(200, txt_surface.get_width()+10)
            # input_box.w = 200
            pg.draw.rect(screen, color, input_box, 2)
            pg.display.flip()
            clock.tick(30)


def receiveData(callback):
    while True:
        data = sock.recv(2048)
        callback(data)

#this method creates a black triangle and paints it on the window everytime a new player arrives (should be displayed in the lobby)
def paintNewPlayer():
    global current_num_of_players
    current_num_of_players = len(listPlayers())
    if (current_num_of_players == 1):
        pg.draw.rect(screen,(0,0,0),(700,200,50,50))
    elif (current_num_of_players == 2):
        pg.draw.rect(screen,(0,0,0),(700,200,50,50))
        pg.draw.rect(screen,(0,0,0),(700,250,50,50))
    elif (current_num_of_players == 3):
        pg.draw.rect(screen,(0,0,0),(700,200,50,50))
        pg.draw.rect(screen,(0,0,0),(700,250,50,50))
        pg.draw.rect(screen,(0,0,0),(700,300,50,50))
    else:
        pg.draw.rect(screen,(0,0,0),(700,200,50,50))
        pg.draw.rect(screen,(0,0,0),(700,250,50,50))
        pg.draw.rect(screen,(0,0,0),(700,300,50,50))
        pg.draw.rect(screen,(0,0,0),(700,350,50,50))
    pg.display.flip()
    clock.tick(30)

def evaluateData(data):
    global current_num_of_players
    packet.ParseFromString(data)
    if (packet.type == packet.CONNECT):
        chat_packet.ParseFromString(data)
        print("\n{} joined the chat.".format(chat_packet.player.name))
        chat_transcript.append(chat_packet.player.name + " joined the chat.")
        #TO DO: temporary comment bc of listPlayers()
        #paintNewPlayer()
    elif (packet.type == packet.CHAT):
        chat_send.ParseFromString(data)
        print("\n{}: {}".format(chat_send.player.name, chat_send.message))
        chat_transcript.append(chat_send.player.name + ": " + chat_send.message)
    elif (packet.type == packet.ERR_LDNE):
        print("This prints if the Lobby doesn't exist")
        createNewLobby()
    elif (packet.type == packet.DISCONNECT):    #TO DO: should repaint the lobby if a player disconnected in the lobby 
        print("\n{} disconnected from chat.".format(chat_packet.player.name))
        chat_transcript.append(chat_packet.player.name + " disconnected from chat.")
        if (chat_packet.player.name == username):
            quit()
    elif (packet.type == packet.ERR_LFULL):
        print("This prints if the Lobby is already full")
        createNewLobby()
    elif (packet.type == packet.ERR):
        print("An error occured.")
    print(">> ", end='')
    stdout.flush()


def createNewLobby():
    start_panel = pg.image.load("./images/CreateLobby.png")
    join_panel = pg.image.load("./images/joinlobby.png")
    exit_panel = pg.image.load("./images/exit.png")
    astro_party = pg.image.load("./images/astro_party.png")
    enterUsername = pg.image.load("./images/enterUsername.png")
    enterHosts = pg.image.load("./images/EnterHosts.png")
    lobbyIDPic = pg.image.load("./images/LobbyID.png")
    lobbyidval = pg.image.load("./images/lobbyidval.png")
    enterUsername = pg.transform.scale(enterUsername, (180, 20))
    start_panel = pg.transform.scale(start_panel, (250, 150))
    join_panel = pg.transform.scale(join_panel, (250, 150))
    exit_panel = pg.transform.scale(exit_panel, (250, 150))
    
    active = False
    text = ''
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                # done = True
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("You selected Create Lobby!\n")
                    font = pg.font.Font(None, 32)
                    input_box = pg.Rect(320, 250, 140, 32)
                    text = ""
                    color = pg.Color("white")
                    done = False
                    max_hosts = 0
                    while not done:
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                quit()
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_RETURN:
                                    print(text + " is the chosen max players.")
                                    max_hosts = int(text)
                                    done = True
                                    text = ''
                                elif event.key == pg.K_BACKSPACE:
                                    text = text[:-1]
                                else:
                                    text += event.unicode
                        txt_surface = font.render(text, True, color)
                        # Render elements
                        screen.blit(bg, (0, 0))
                        screen.blit(enterHosts, (-10, -10))
                        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                        pg.draw.rect(screen, pg.Color("#EB5500"), input_box, 2)
                        pg.display.flip()
                        clock.tick(30)
                    pg.display.flip()
                    clock.tick(30)

                    packet.type = packet.CREATE_LOBBY
                    lobbyDetails = packet.CreateLobbyPacket()
                    lobbyDetails.type = packet.CREATE_LOBBY
                    lobbyDetails.max_players = max_hosts

                    room = sock.send(lobbyDetails.SerializeToString())
                    room = sock.recv(2048)
                    lobbyDetails.ParseFromString(room)
                    lobbyID = lobbyDetails.lobby_id

                    # Enter Username Screen
                    myfont = pg.font.SysFont("monospace", 50)
                    font = pg.font.Font(None, 32)
                    input_box = pg.Rect(340, 250, 140, 32)
                    text = ""
                    color = pg.Color("white")
                    done = False
                    username = ""
                    while not done:
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                quit()
                                # done = True
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_RETURN:
                                    print(text + " is the host's username")
                                    username = text
                                    done = True
                                    text = ''
                                elif event.key == pg.K_BACKSPACE:
                                    text = text[:-1]
                                else:
                                    text += event.unicode
                        txt_surface = font.render(text, True, color)
                        # width = max(200, txt_surface.get_width()+10)
                        # input_box.w = width
                        # Render Elements
                        screen.blit(bg, (0, 0))
                        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                        screen.blit(lobbyIDPic, (10, -100))
                        screen.blit(lobbyidval, (-10, -30))
                        screen.blit(enterUsername, (350, 290))
                        pg.draw.rect(screen, pg.Color("#EB5500"), input_box, 2)
                        # Render Lobby ID
                        lobbyID_start_x = 280
                        for char in str(lobbyID):
                            label = myfont.render(char, 1, (255,140,0))
                            screen.blit(label, (lobbyID_start_x, 180))
                            lobbyID_start_x += 70
                        pg.display.flip()
                        clock.tick(30)
                        pg.display.flip()
                        clock.tick(30)

                    print("\nlobbyID: {}".format(lobbyID))
                    chat_packet.player.name = username
                    chat_packet.lobby_id = lobbyID
                    try:
                        connect = sock.send(chat_packet.SerializeToString())
                    except:
                        print("\nError in creating/entering a lobby~")
                        quit()
                    return lobbyID, username, max_hosts
                elif continue_button.collidepoint(event.pos):
                    screen.blit(bg, (0, 0))
                    enterLobbyID = pg.image.load("./images/EnterLobbyID.png")
                    screen.blit(enterLobbyID, (0, 0))
                    pg.display.flip()
                    clock.tick(30)

                    font = pg.font.Font(None, 32)
                    input_box = pg.Rect(340, 275, 140, 32)
                    text = ""
                    color = pg.Color("white")
                    done = False
                    lobbyID = ""
                    while not done:
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                quit()
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_RETURN:
                                    lobbyID = text
                                    done = True
                                    text = ''
                                elif event.key == pg.K_BACKSPACE:
                                    text = text[:-1]
                                else:
                                    text += event.unicode
                        txt_surface = font.render(text, True, color)
                        screen.blit(bg, (0, 0))
                        screen.blit(enterLobbyID, (0, 0))
                        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                        pg.draw.rect(screen, pg.Color("#EB5500"), input_box, 2)
                        pg.display.flip()
                        clock.tick(30)

                    screen.blit(bg, (0, 0))
                    screen.blit(enterUsername, (350, 200))
                    pg.display.flip()
                    clock.tick(30)
                    input_box = pg.Rect(340, 235, 140, 32)
                    text = ""
                    color = pg.Color("white")
                    done = False
                    username = ""
                    while not done:
                        for event in pg.event.get():
                            if event.type == pg.QUIT:
                                quit()
                            if event.type == pg.KEYDOWN:
                                if event.key == pg.K_RETURN:
                                    username = text
                                    done = True
                                    text = ''
                                elif event.key == pg.K_BACKSPACE:
                                    text = text[:-1]
                                else:
                                    text += event.unicode
                        txt_surface = font.render(text, True, color)
                        screen.blit(bg, (0, 0))
                        screen.blit(enterUsername, (350, 200))
                        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
                        pg.draw.rect(screen, pg.Color("#EB5500"), input_box, 2)
                        pg.display.flip()
                        clock.tick(30)

                    chat_packet.player.name = username
                    chat_packet.lobby_id = lobbyID
                    try:
                        connect = sock.send(chat_packet.SerializeToString())
                    except:
                        print("\nError in creating/entering a lobby~")
                        quit()
                    return lobbyID, username, 0
                elif quit_button.collidepoint(event.pos):
                    print("quit button was pressed!")
                    quit()
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode
        screen.fill((10, 10, 10))
        screen.blit(bg, (0, 0))
        start_button = pg.draw.rect(screen,(0,0,0),(360,250,149,49))
        continue_button = pg.draw.rect(screen,(0,0,0),(280,330,149,49))
        quit_button = pg.draw.rect(screen,(0,0,0),(450,330,140,49))
        screen.blit(start_panel, (310, 200))
        screen.blit(join_panel, (230, 280))
        screen.blit(exit_panel, (398, 280))
        screen.blit(astro_party, (270, 100))
        pg.display.flip()
        clock.tick(30)


def listPlayers():
    data = sock.send(listp_packet.SerializeToString())
    data = sock.recv(1024)
    listp_packet.ParseFromString(data)
    return listp_packet.player_list


def startChat():
    #TO DO: temporary comment because of listPlayers()
    #paintNewPlayer()
    screen.blit(bg, (0, 0))
    waitOtherPlayers = pg.image.load("./images/waitingPlayers.png")
    waitOtherPlayers = pg.transform.scale(waitOtherPlayers, (700, 300))
    chat_panel = pg.image.load("./images/chat_panel.png")
    chat_panel = pg.transform.scale(chat_panel, (220, 425))
    start_button = pg.image.load("./images/backbut.png")
    start_button = pg.transform.scale(start_button, (400, 250))
    start_button = pg.transform.flip(start_button, True, False)

    player_1 = pg.image.load("./images/chat_panel2.png")
    player_1 = pg.transform.scale(player_1, (150, 150))
    player_2 = pg.image.load("./images/chat_panel2.png")
    player_2 = pg.transform.scale(player_2, (150, 150))
    player_3 = pg.image.load("./images/chat_panel2.png")
    player_3 = pg.transform.scale(player_3, (150, 150))
    player_4 = pg.image.load("./images/chat_panel2.png")
    player_4 = pg.transform.scale(player_4, (150, 150))

    pg.display.flip()
    clock.tick(30)

    chat_send.player.name = username
    chat_send.lobby_id = lobbyID
    receiving_thread = Thread(target=receiveData, args=[evaluateData])
    receiving_thread.start()

    font = pg.font.Font(None, 20)
    input_box = pg.Rect(30, 400, 200, 40)
    message = ""
    color = pg.Color("white")
    #listen to the start button and to the chatbox and to the incoming players
    while (True):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.display.quit()
                pg.quit()
                quit()
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_button_detector.collidepoint(event.pos):
                    print("START GAME!")
                    gameProper()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_RETURN:
                    #send the message
                    try:
                        if(message == "dc()"):
                            chat_disconnect.player.name = username
                            sock.send(chat_disconnect.SerializeToString())
                            isBreak = True
                            quit()
                        elif(message == "list()"):
                            playersList = listPlayers()
                            for player in playersList:
                                print(player)
                            print(">> ", end='')
                        else:
                            chat_send.message = message
                            sock.send(chat_send.SerializeToString())
                    except OSError:
                        print("\nError")
                    done = True
                    message = ''
                elif event.key == pg.K_BACKSPACE:
                    message = message[:-1]
                else:
                    message += event.unicode
        # Render Elements
        screen.blit(bg, (0, 0))
        screen.blit(waitOtherPlayers, (200, -100))
        screen.blit(chat_panel, (20, 20))
        screen.blit(player_1, (380, 90))
        screen.blit(player_2, (380, 270))
        screen.blit(player_3, (570, 90))
        screen.blit(player_4, (570, 270))
        start_button_detector = pg.draw.rect(screen,(0,0,0),(760,230,50,30))
        screen.blit(start_button, (600, 120))
        # Split string in text box para kumasya ang inputs
        textbox = []

        #split the display in the chat box if length exceeds 22
        if (len(message) > 25):
            start_y = 0
            for i in range(0, len(message), 25):
                output = message[i:i+25]
                txt_surface = font.render(output, True, pg.Color("white"))
                screen.blit(txt_surface, (input_box.x+5, input_box.y+5+start_y))
                start_y += 15
        else:
            txt_surface = font.render(message, True, pg.Color("white"))
            screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        global chat_transcript
        start_y = 30
        myfont = pg.font.SysFont("monospace", 15)
        # Split strings printed para kumasya lol
        toPrint = []
        for content in chat_transcript:
            if len(content) > 22:
                for i in range(0, len(content), 22):
                    toPrint.append(content[i:i+22])
                for i in toPrint:
                    label = myfont.render(i, 1, (255,255,255))
                    screen.blit(label, (30, start_y))
                    start_y += 20
                toPrint = []
            else:
                label = myfont.render(content, 1, (255,255,255))
                screen.blit(label, (30, start_y))
                start_y += 20
        # width = max(200, txt_surface.get_width()+10)
        # input_box.w = width
        pg.draw.rect(screen, color, input_box, 2)
        pg.display.flip()
        clock.tick(30)



######################################################################################
# Create a TCP/IP socket and connect the socket to the port where the server is listening
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ("202.92.144.45", 80)
sock.connect(server_address)

# declare different types of packets
packet = TcpPacket()

# Connect Packet
connection = packet.ConnectPacket()
connection.type = packet.CONNECT

# Chat Packet
chat_packet = packet.ConnectPacket()
chat_packet.type = packet.CONNECT

# Send Packet
chat_send = packet.ChatPacket()
chat_send.type = packet.CHAT

# Disconnect Packet
chat_disconnect = packet.DisconnectPacket()
chat_disconnect.type = packet.DISCONNECT

# List Players Packet
listp_packet = packet.PlayerListPacket()
listp_packet.type = packet.PLAYER_LIST

isBreak = False
if (isBreak == False):
    pg.init()
    lobbyID, username, max_hosts = createNewLobby()
    startChat()
    pg.quit()