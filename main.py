#! /usr/bin/python

import socket
import sys

from proto.tcp_packet_pb2 import TcpPacket

from threading import Thread


syntax = "proto2"


# def createLobby(sock):
# def createMessage(data):
# def listPlayers()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ("202.92.144.45", 80)
# print("connecting to %s port %s" % server_address, file=sys.stderr)
sock.connect(server_address)

packet = TcpPacket()
connection = packet.ConnectPacket()
connection.type = packet.CONNECT

chat_packet = packet.ConnectPacket()
chat_packet.type = packet.CONNECT


choice = input("Create New Lobby? Y/N: ")
if choice == 'Y':
    packet.type = packet.CREATE_LOBBY
    lobbyDetails = packet.CreateLobbyPacket()
    lobbyDetails.type = packet.CREATE_LOBBY
    lobbyDetails.max_players = 4

    room = sock.send(lobbyDetails.SerializeToString())
    room = sock.recv(2048)
    lobbyDetails.ParseFromString(room)
    lobbyID = lobbyDetails.lobby_id
    print("lobbyID: {}".format(lobbyID))
else:
    lobbyID = input("Enter lobby ID: ")


username = input("Enter username: ")

# Instantiate CONNECT Packet
packet.type = packet.CONNECT
chat_packet.player.name = username
chat_packet.lobby_id = lobbyID

sock.send(chat_packet.SerializeToString())

# Instantiate ChatPacket
chat_send = packet.ChatPacket()
chat_send.type = packet.CHAT
chat_send.player.name = username
chat_send.lobby_id = lobbyID


def parseData(data):
    packet.ParseFromString(data)

    if(packet.type == packet.CONNECT):
        chat_send.ParseFromString(data)
        print("%s gas joined the chat room" % chat_send.player.name)
    elif packet.type == packet.CHAT:
        chat_send.ParseFromString(data)
        print('[{}] {}'.format(chat_send.player.name, chat_send.message))
    else:
        print('Packet received')

        # Listen for other chats
listening_thread = Thread(target=sock.recv, args=[])
while (True):
    message = input("Message: ")
    try:
        chat_send.message = message
        sock.send(chat_send.SerializeToString())
        # receive = sock.recv(2048)
        # finalMessage = chat_send.ParseFromString(receive)
        # print("{}".format(finalMessage))
    except OSError:
        print("Error")
        break
