import pygame as pg
import os
os.chdir("..")

menuBackground = pg.image.load("./images/bg/background.png")

icon = pg.image.load("./images/misc/icon.png")
ship1 = pg.image.load("./images/misc/ship1.png")
ship2 = pg.image.load("./images/misc/ship2.png")
ship3 = pg.image.load("./images/misc/ship3.png")
ship4 = pg.image.load("./images/misc/ship4.png")
bullet = pg.image.load("./images/misc/bullet.png")

enterUsername = pg.image.load("./images/misc/enterUsername.png")
astroParty = pg.image.load("./images/misc/astropartyLogo.png")
enterHosts = pg.image.load("./images/misc/enterHosts.png")
lobbyIDPic = pg.image.load("./images/misc/lobbyID.png")
lobbyidVal = pg.image.load("./images/misc/lobbyidValue.png")
enterLobbyID = pg.image.load("./images/misc/enterLobbyID.png")
chatPanel = pg.image.load("./images/misc/chatPanel.png")
waitOtherPlayers = pg.image.load("./images/misc/waitingPlayers.png")

# start_button = pg.image.load("./images/backbut.png")
player1 = pg.image.load("./images/misc/p1.png")
player2 = pg.image.load("./images/misc/p2.png")
player3 = pg.image.load("./images/misc/p3.png")
player4 = pg.image.load("./images/misc/p4.png")
noPlayer = pg.image.load("./images/misc/noPlayer.png")

# Guide Images
rotate = pg.image.load("./images/guide/rotate.png")
fire = pg.image.load("./images/guide/fire.png")
rounds = pg.image.load("./images/guide/rounds.png")
wins = pg.image.load("./images/guide/most_wins.png")
goodluck = pg.image.load("./images/guide/goodluck.png")
next = pg.image.load("./images/guide/space.png")