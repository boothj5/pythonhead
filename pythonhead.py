from random import shuffle
from player import Player
from console import clearScreen, showGame
from card import Card


def createBigEnoughDeck(numps, numcs):
    cardsNeeded = numps * numcs * 3
    while len(deck) < cardsNeeded:
        deck.extend(deck)

def charToBool(c):
    return c.upper() == 'Y'

suits = ["HEARTS", "SPADES", "DIAMONDS", "CLUBS"]
ranks = ["TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING", "ACE"]

deck = [(x,y) for y in suits for x in ranks]
pile = []
burnt = []
players = []
turn = 0

clearScreen()

card1 = Card(2,3)
card2 = Card(2,0)

print card1
print card2

print card1.__cmp__(card2)


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
    print "HAND:", player.hand
    print "FACEUP:", player.faceup
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

clearScreen()
showGame(pile, burnt, deck, players)


