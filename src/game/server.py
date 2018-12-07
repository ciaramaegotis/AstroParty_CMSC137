import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind('0.0.0.0', 10000)

while True:
    