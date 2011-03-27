def clearScreen():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

def showGame(pile, burnt, deck, players):
    print cardListToString('Pile: ', pile)
    print len(burnt), "burnt"
    print len(deck), "left on deck"

    for player in players:
        print player.name
        print cardListToString('Hand     : ', player.hand)
        print cardListToString('Faceup   : ', player.faceup)
        print cardListToString('Facedown : ', player.facedown)

def cardListToString(label, cards):
    result = label
    for card in cards:
        result = result + (str(card))
        result = result +  ', '
    return result


