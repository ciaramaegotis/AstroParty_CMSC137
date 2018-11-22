#! /usr/bin/python

from proto.tcp_packet_pb2 import TcpPacket
# from threading import Thread
import socket
from sys import stdout
from threading import Thread
import pygame as pg

syntax = "proto2"

def receiveData(callback):
    while True:
        data = sock.recv(2048)
        callback(data)


def evaluateData(data):
    packet.ParseFromString(data)
    if (packet.type == packet.CONNECT):
        chat_packet.ParseFromString(data)
        print("\n{} joined the chat.".format(chat_packet.player.name))
    elif (packet.type == packet.CHAT):
        chat_send.ParseFromString(data)
        print("\n{}: {}".format(chat_send.player.name, chat_send.message))
    elif (packet.type == packet.ERR_LDNE):
        print("This prints if the Lobby doesn't exist")
        createNewLobby()
    elif (packet.type == packet.DISCONNECT):
        print("\n{} disconnected from chat.".format(chat_packet.player.name))
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
    bg = pg.image.load("background.jpeg")
    start_panel = pg.image.load("obstacle.png")
    astro_party = pg.image.load("astro_party.png")
    start_panel = pg.transform.scale(start_panel, (150, 50))
    join_panel = start_panel
    exit_panel = start_panel
    screen = pg.display.set_mode((850, 450))
    clock = pg.time.Clock()
    active = False
    text = ''
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                if start_button.collidepoint(event.pos):
                    print("start button was pressed!")
                    packet.type = packet.CREATE_LOBBY
                    lobbyDetails = packet.CreateLobbyPacket()
                    lobbyDetails.type = packet.CREATE_LOBBY
                    max_hosts = int(input("Enter Max Number of Hosts: "))
                    lobbyDetails.max_players = max_hosts

                    room = sock.send(lobbyDetails.SerializeToString())
                    room = sock.recv(2048)
                    lobbyDetails.ParseFromString(room)
                    lobbyID = lobbyDetails.lobby_id
                    print("\nlobbyID: {}".format(lobbyID))
                    username = input("\nEnter username: ")
                    chat_packet.player.name = username
                    chat_packet.lobby_id = lobbyID
                    try:
                        connect = sock.send(chat_packet.SerializeToString())
                    except:
                        print("\nError in creating/entering a lobby~")
                    return lobbyID, username
                elif continue_button.collidepoint(event.pos):
                    print("continue button was pressed!")
                    lobbyID = input("\nEnter lobby ID: ")
                    username = input("\nEnter username: ")
                    chat_packet.player.name = username
                    chat_packet.lobby_id = lobbyID
                    try:
                        connect = sock.send(chat_packet.SerializeToString())
                    except:
                        print("\nError in creating/entering a lobby~")
                    return lobbyID, username
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
        start_button = pg.draw.rect(screen,(0,0,0),(360,250,149,49));
        continue_button = pg.draw.rect(screen,(0,0,0),(280,330,149,49));
        quit_button = pg.draw.rect(screen,(0,0,0),(450,330,140,49));
        screen.blit(start_panel, (360, 250))
        screen.blit(join_panel, (280, 330))
        screen.blit(exit_panel, (450, 330))
        screen.blit(astro_party, (270, 100))
        pg.display.flip()
        clock.tick(30)
def listPlayers():
    data = sock.send(listp_packet.SerializeToString())
    data = sock.recv(1024)
    listp_packet.ParseFromString(data)
    return listp_packet.player_list


def startChat():
    chat_send.player.name = username
    chat_send.lobby_id = lobbyID
    receiving_thread = Thread(target=receiveData, args=[evaluateData])
    receiving_thread.start()

    while (True):
        try:
            message = input("")
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
            break


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
    lobbyID, username = createNewLobby()
    startChat()
    pg.quit()
