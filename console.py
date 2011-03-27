def clear_screen():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

def show_game(game):
    print game.pile
    print len(game.burnt), "burnt"
    print len(game.deck), "left on deck"

    for player in game.players:
        print player.name
        print player.hand
        print player.faceup
        print player.facedown

def request_num_players():
    return int(raw_input("Enter number of players: "))

def request_num_cards_each():
    return int(raw_input("Enter number of cards each: "))

def welcome():
    print "Welcome to Pythonhead!"
    print

def request_player_name(num):
    return raw_input("Enter name of player " + str(num+1) +  ": ")

def wait_user():
    raw_input("Press enter to continue:")

def char_to_bool(c):
    return c.upper() == 'Y'

def request_swap(name):
    return char_to_bool(raw_input(name + " do you want to swap cards?"))

def request_swap_more():
    return char_to_bool(raw_input('Do you want to swap more cards?'))

