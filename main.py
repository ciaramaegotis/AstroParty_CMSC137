#! /usr/bin/python

from proto.tcp_packet_pb2 import TcpPacket
import socket
import sys

syntax = "proto2"


def PromptForName(player):
    player.id = int(input("Enter player ID: "))
    player.name = input("Enter name: ")


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ("202.92.144.45", 80)
print("connecting to %s port %s" % server_address, file=sys.stderr)
sock.connect(server_address)