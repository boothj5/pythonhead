from random import shuffle

def createBigEnoughDeck(numPlayers, numCards):
    cardsNeeded = players * numCardsEach * 3
    while len(deck) < cardsNeeded:
        deck.extend(deck)

suits = ["HEARTS", "SPADES", "DIAMONDS", "CLUBS"]
ranks = ["TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE", "TEN", "JACK", "QUEEN", "KING", "ACE"]

deck = [(x,y) for y in suits for x in ranks]

print deck
print

print "Deck size =", len(deck)

players = int(raw_input("Enter number of players: "))
numCardsEach = int(raw_input("Enter number of cards each: "))

print 
print "Players =", players
print "Cards each =", numCardsEach
print

createBigEnoughDeck(players, numCardsEach)
shuffle(deck)


print deck

print
print len(deck)







