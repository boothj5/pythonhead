def clear_screen():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

def show_game(game):
    print card_list_to_string('Pile: ', game.pile)
    print len(game.burnt), "burnt"
    print len(game.deck), "left on deck"

    for player in game.players:
        print player.name
        print card_list_to_string('Hand     : ', player.hand)
        print card_list_to_string('Faceup   : ', player.faceup)
        print card_list_to_string('Facedown : ', player.facedown)

def card_list_to_string(label, cards):
    result = label
    for card in cards:
        result = result + (str(card))
        result = result +  ', '
    return result

def request_num_players():
    return int(raw_input("Enter number of players: "))

def request_num_cards_each():
    return int(raw_input("Enter number of cards each: "))

def welcome():
    print "Welcome to Pythonhead!"
    print


