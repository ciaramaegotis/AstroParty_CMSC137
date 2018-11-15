#! /usr/bin/python

from proto.tcp_packet_pb2 import TcpPacket
# from threading import Thread
import socket
import sys
import select
import pickle
from threading import Thread

syntax = "proto2"


def receiveData(callback):
	while True:
		data = sock.recv(2048)
		callback(data)

def evaluateData(data):
	packet.ParseFromString(data)
	if (packet.type == packet.CONNECT):
		chat_packet.ParseFromString(data)
		print("\n{} joined chat.".format(chat_packet.player.name))
	elif (packet.type == packet.CHAT):
		chat_send.ParseFromString(data)
		print("\n{}: {}".format(chat_send.player.name, chat_send.message))

def createLobby(sock):
    lobbyDetails = TcpPacket()
    lobbyDetails.type = 1
    lobbyDetails.max_players = 3
    sock.send(bytes())

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ("202.92.144.45", 80)
#print("connecting to %s port %s" % server_address, file=sys.stderr)
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
    print("\nlobbyID: {}".format(lobbyID))
else:
	lobbyID = input("\nEnter lobby ID: ")


username = input("\nEnter username: ")

#connects the new user
packet.type = packet.CONNECT
chat_packet.player.name = username
chat_packet.lobby_id = lobbyID

try:
	connect = sock.send(chat_packet.SerializeToString())
except:
	print("\nError in creating a lobby~")


chat_send = packet.ChatPacket()
chat_send.type = packet.CHAT
chat_send.player.name = username
chat_send.lobby_id = lobbyID

receiving_thread = Thread(target=receiveData, args=[evaluateData])
receiving_thread.start()

while (True):
	try:
		message = input("\nChat >> ")
		chat_send.message = message
		sock.send(chat_send.SerializeToString())
	except OSError:
		print("\nError")
		break