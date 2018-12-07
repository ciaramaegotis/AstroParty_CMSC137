import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 10000))


# create needed variables

lobby_id = 0
payload = []
players = []
while True:
    # Receive Data
    data, address = sock.recvfrom(1024)

    payload = data.decode().split(':')
    payloadType = payload[0]
    
    if payloadType == 'CREATE_LOBBY':
        lobby_id = payload[1]
        newPlayer = {
            'name': payload[2]
        }
        players.append(newPlayer)
        data = 'CREATE_LOBBY'
        data = str.encode(data)

    elif payloadType == 'JOIN_LOBBY':
        newPlayer = {
            'name': payload[1]
        }
        players.append(newPlayer)
        data = 'JOIN_LOBBY:' + str(lobby_id)
        data = str.encode(data)

    elif payloadType == 'GET_PLAYERS':
        data = 'GET_PLAYERS:' + str(len(players))
        data = str.encode(data)
    # Send data back
    sock.sendto(data, address)