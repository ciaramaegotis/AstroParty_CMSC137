import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 10000))


# create needed variables

numPlayers = 0
lobby_id = 0
payload = []
players = []
players_coordinates = []
players_scores = []

startGame = 0

while True:
    # Receive Data
    data, address = sock.recvfrom(1024)

    payload = data.decode().split(':')
    payloadType = payload[0]
    
    if payloadType == 'CREATE_LOBBY':
        lobby_id = payload[1]
        newPlayer = {
            "name": payload[2],
            "id": numPlayers
        }
        numPlayers += 1
        players.append(newPlayer)
        data = 'CREATE_LOBBY:' + str(newPlayer["id"])
        data = str.encode(data)

    elif payloadType == 'JOIN_LOBBY':
        newPlayer = {
            "name": payload[1],
            "id": numPlayers
        }
        numPlayers += 1
        players.append(newPlayer)
        data = 'JOIN_LOBBY:' + str(lobby_id) + ':' + str(newPlayer["id"]) 
        data = str.encode(data)

    elif payloadType == 'GET_PLAYERS':
        data = 'GET_PLAYERS:' + str(len(players))
        data = str.encode(data)
    
    elif payloadType == 'START_GAME':
        startGame = 1

    elif payloadType == 'UPDATE_GAME':
        print("Update Game!")

    elif payloadType == 'DISCONNECT':
        players[:] = [d for d in players if d.get("id") != int(payload[1])]
        print(players)
        data = 'DISCONNECT'
        data = str.encode(data)
    
    elif payloadType == 'GET_GAME':
        data = 'GET_GAME:' + str(startGame)
        data = str.encode(data)
        # thelist[:] = [d for d in thelist if d.get('id') != 2]
    # Send data back
    sock.sendto(data, address)