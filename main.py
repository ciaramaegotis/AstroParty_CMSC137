#! /usr/bin/python

from proto.tcp_packet_pb2 import TcpPacket
import socket
import sys
import select
import pickle

syntax = "proto2"


def createLobby(sock):
    lobbyDetails = TcpPacket()
    lobbyDetails.type = 1
    lobbyDetails.max_players = 3
    sock.send(bytes())


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port where the server is listening
server_address = ("202.92.144.45", 80)
print("connecting to %s port %s" % server_address, file=sys.stderr)
sock.connect(server_address)

packet = TcpPacket()
connection = packet.ConnectPacket()
connection.type = packet.CONNECT


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
