def createBigEnoughDeck(numPlayers, numCards):
    cardsNeeded = players * numCardsEach * 3
    while len(deck) < cardsNeeded:
        deck.extend(deck)

suits = ["hearts", "spades", "diamonds", "clubs"]
ranks = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]

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

print deck

print
print len(deck)







