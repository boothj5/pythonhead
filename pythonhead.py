from random import shuffle
from player import Player

def createBigEnoughDeck(numps, numcs):
    cardsNeeded = numps * numcs * 3
    while len(deck) < cardsNeeded:
        deck.extend(deck)

suits = ["HEARTS", "SPADES", "DIAMONDS", "CLUBS"]
ranks = ["TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING", "ACE"]

deck = [(x,y) for y in suits for x in ranks]

players = []

print deck
print

print "Deck size =", len(deck)

numPlayers = int(raw_input("Enter number of players: "))
numCardsEach = int(raw_input("Enter number of cards each: "))

print 
print "Players =", numPlayers
print "Cards each =", numCardsEach
print

createBigEnoughDeck(numPlayers, numCardsEach)
shuffle(deck)


print deck

print
print len(deck)

for i in range(numPlayers):
    playerName = raw_input("Enter name of player " + str(i+1) +  ": ")
    player = Player(playerName)
    players.append(player)

players[0].addToHand([deck[0]])


for player in players:
    print player.name
    print player.hand
    print player.faceup
    print player.facedown


