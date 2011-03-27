from random import shuffle
from player import Player
from console import clearScreen, showGame, cardListToString
from card import Card


def createBigEnoughDeck(numps, numcs):
    cardsNeeded = numps * numcs * 3
    while len(deck) < cardsNeeded:
        deck.extend(deck)

def charToBool(c):
    return c.upper() == 'Y'

deck = [Card(x,y) for y in Card.suits for x in Card.ranks]
pile = []
burnt = []
players = []
turn = 0

clearScreen()

print "Welcome to Pythonhead!"
print

numPlayers = int(raw_input("Enter number of players: "))
numCardsEach = int(raw_input("Enter number of cards each: "))

createBigEnoughDeck(numPlayers, numCardsEach)
shuffle(deck)

for i in range(numPlayers):
    playerName = raw_input("Enter name of player " + str(i+1) +  ": ")
    player = Player(playerName)
    
    for j in range(numCardsEach):
        player.hand.append(deck.pop())
        player.faceup.append(deck.pop())
        player.facedown.append(deck.pop())

    players.append(player)

clearScreen()
showGame(pile, burnt, deck, players)

raw_input("Press enter")

for player in players:
    clearScreen()
    print cardListToString("Hand   : ", player.hand)
    print cardListToString("faceup : ", player.faceup)
    print
    swap = charToBool(raw_input(player.name + " do you want to swap cards?"))

    if swap:
        clearScreen()
        print player.name
        print
        print "Hand    : "
        print player.hand
        print "Face up : "
        print player.faceup
        print
        hCard = int(raw_input("Which card from your hand do you wish to swap? "))
        fCard = int(raw_input("Which card from your face up pile do you wish to swap? "))
        player.swap(hCard-1, fCard-1)

clearScreen()
showGame(pile, burnt, deck, players)


