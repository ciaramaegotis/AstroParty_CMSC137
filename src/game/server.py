import socket
import json
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 10000))


# create needed variables

numPlayers = 0
lobby_id = 0
payload = []
players = {}
bullets = {}
bullets['listB'] = []
players['listP'] = []
players_coordinates = []
players_scores = []

startGame = 0

while True:
    # Receive Data
    data, address = sock.recvfrom(1024)

    payload = data.decode().split(' ')
    payloadType = payload[0]
    
    if payloadType == 'CREATE_LOBBY':
        lobby_id = payload[1]
        newPlayer = {
            "name": payload[2],
            "id": numPlayers,
            "score": 0,
            "status": "alive"
        }
        numPlayers += 1
        players['listP'].append(newPlayer)
        data = 'CREATE_LOBBY ' + str(newPlayer["id"])
        data = str.encode(data)

    elif payloadType == 'JOIN_LOBBY':
        newPlayer = {
            "name": payload[1],
            "id": numPlayers,
            "score": 0,
            "status": "alive"
        }
        numPlayers += 1
        players['listP'].append(newPlayer)
        data = 'JOIN_LOBBY ' + str(lobby_id) + ' ' + str(newPlayer["id"]) 
        data = str.encode(data)

    elif payloadType == 'GET_PLAYERS':
        data = 'GET_PLAYERS ' + str(len(players['listP']))
        data = str.encode(data)
    
    elif payloadType == 'START_GAME':
        startGame = 1

    elif payloadType == 'UPDATE_GAME':
        print("Update Game!")

    elif payloadType == 'DISCONNECT':
        players['listP'][:] = [d for d in players['listP'] if d.get("id") != int(payload[1])]
        print(players['listP'])
        data = 'DISCONNECT'
        data = str.encode(data)

    elif payloadType == 'GET_GAME':
        data = 'GET_GAME ' + str(startGame)
        data = str.encode(data)

    elif payloadType == 'UPDATE_PLAYER_LIST':
        data = 'UPDATE_PLAYER_LIST '
        data += json.dumps(players)
        data = str.encode(data)
    
    elif payloadType == 'UPDATE_BULLET_LIST':
        data = 'UPDATE_BULLET_LIST '
        data += json.dumps(bullets)
        data = str.encode(data)

    elif payloadType == 'SEND_PLAYER_STATS':
        for p in players['listP']:
            if p['id'] == int(payload[3]):
                p['x'] = int(payload[1])
                p['y'] = int(payload[2])
                p['r'] = payload[4]
    
    elif payloadType == 'SEND_BULLET_STATS':
        newBullet = {
            'id': payload[3],
            'x': payload[1],
            'y': payload[2],
            'dir': payload[4]
        }
        bullets['listB'].append(newBullet)
    
    elif payloadType == 'PURGE_BULLETS':
        bullets = {}
        bullets['listB'] = []
    
    elif payloadType == 'KILL_SCORE':
        # players['listP'][:] = [d for d in players['listP'] if d.get("id") != int(payload[1])]
        for p in players['listP']:
            if p["id"] == int(payload[1]):
                p["status"] = "dead"
            if p["id"] == int(payload[2]):
                p["score"] = p["score"] + 1  
    # Send data back
    sock.sendto(data, address)