import socket
from threading import Thread

# Import protobuf files
import os
import sys
script_dir = sys.path[0]
script_dir = script_dir[:-4]
chat_path = os.path.join(script_dir, 'proto/')
sys.path.insert(0, chat_path)
import tcp_packet_pb2

# Import file settings
from utils.variables import *

packet = tcp_packet_pb2.TcpPacket()

class Chat:
	def __init__(self, game):
		self.game = game
		self.packet = packet
		# Initialize Server
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect(('202.92.144.45',80))

	def evaluateData(self):
		while self.game.running:
			# Receive Data
			data = self.sock.recv(1024)
			self.packet.ParseFromString(data)
			if(packet.type == packet.DISCONNECT):
				self.game.chatTranscript.append(chat.player.name + " disconnected from chat.")
				if self.game.username == chat.player.name:
					self.game.running = False
					self.game.currentDisplay = MAIN_MENU
					quit()
			elif (packet.type == packet.CHAT):
				chat = self.packet.ChatPacket()
				chat.ParseFromString(data)	
				if(len(self.game.chatTranscript) >= 29):
					self.game.chatTranscript.pop(0)
				self.game.chatTranscript.append(chat.player.name + ": " + chat.message)
			elif (packet.type == packet.PLAYER_LIST):
				players = self.packet.PlayerListPacket()
				players.ParseFromString(data)
				print(players.player_list)
				
			elif (packet.type == packet.ERR_LDNE):
				print("This prints if the Lobby doesn't exist")
				quit()	
			elif (packet.type == packet.ERR_LFULL):
				print("This prints if the Lobby is already full")
			elif (packet.type == packet.ERR):
				print("An error occured.")
        
	def createLobby(self, number):
		# instantiate Packet
		lobby = self.packet.CreateLobbyPacket()
		lobby.type = self.packet.CREATE_LOBBY
		lobby.max_players = number

		# Send/Receive Data
		self.sock.send(lobby.SerializeToString())
		data = self.sock.recv(1024)
		lobby.ParseFromString(data)
		
		# Return lobby to get ID
		return lobby

	def connectToLobby(self, lobby_id, name):
		# Instantiate Packet
		connect = self.packet.ConnectPacket()
		connect.type = self.packet.CONNECT
		connect.lobby_id = lobby_id
		connect.player.name = name
		
		# Send/Receive Data
		self.sock.send(connect.SerializeToString())
		data = self.sock.recv(1024)
		connect.ParseFromString(data)
		
		# Start Thread
		receivingThread = Thread(target=self.evaluateData)
		receivingThread.start()

	def listPlayers(self):
		# Instantiate Packet
		players = self.packet.PlayerListPacket()
		players.type = self.packet.PLAYER_LIST
		
		# Send Data
		self.sock.send(players.SerializeToString())
		
	def sendMessage(self, message):
		# Instantiate Packet
		chat = self.packet.ChatPacket()
		chat.type = self.packet.CHAT
		chat.message = message
		# Send message
		self.sock.send(chat.SerializeToString())
		
	def disconnectChat(self):
		# Instantiate Packet
		disconnect = self.packet.DisconnectPacket()
		disconnect.type = self.packet.DISCONNECT

		self.sock.send(disconnect.SerializeToString())
		data = self.sock.recv(1024)
		disconnect.ParseFromString(data)