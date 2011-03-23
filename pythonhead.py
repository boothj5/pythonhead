from random import shuffle
from player import Player

def createBigEnoughDeck(numps, numcs):
    cardsNeeded = numps * numcs * 3
    while len(deck) < cardsNeeded:
        deck.extend(deck)

def clearScreen():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"


def charToBool(c):
    return c.upper() == 'Y'

def showPlayers():
    for player in players:
        print player.name
        print player.hand
        print player.faceup
        print player.facedown

suits = ["HEARTS", "SPADES", "DIAMONDS", "CLUBS"]
ranks = ["TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING", "ACE"]

deck = [(x,y) for y in suits for x in ranks]
pile = []
burnt = []
players = []


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
    
    for j in range(numCardsEach):
        player.hand.append(deck.pop())
        player.faceup.append(deck.pop())
        player.facedown.append(deck.pop())

    players.append(player)

    showPlayers()

print "Dealt cards"
print "Cards remaining: ", len(deck)

raw_input("Press enter")

for player in players:
    clearScreen()
    print "HAND:"
    print player.hand
    print "FACEUP:"
    print player.faceup
    print

    swap = charToBool(raw_input(player.name + " do you want to swap cards?"))

    if swap:
        clearScreen()
        print player.name
        print
        print "HAND:"
        print player.hand
        print "FACEUP:"
        print player.faceup
        print

        hCard = int(raw_input("Which card from your hand do you wish to swap? "))
    
        fCard = int(raw_input("Which card from your face up pile do you wish to swap? "))

        player.swap(hCard-1, fCard-1)



    raw_input()

showPlayers()

