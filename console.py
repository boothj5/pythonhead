def clear_screen():
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
    print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"

def show_game(game):
    print game.pile
    print len(game.burnt), "burnt"
    print len(game.deck), "left on deck"

    for player in game.players:
        print player.name
        print "Hand      : " + ", ".join(map(str, player.hand))
        print "Face up   : " + ", ".join(map(str, player.faceup))
        print "Face down : " + ", ".join(map(str, player.facedown))

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

def show_player_swap(player):
    print player.name
    print "Hand      : " + ", ".join(map(str, player.hand))
    print "Face up   : " + ", ".join(map(str, player.faceup))
    print
 
def request_hand_swap():
    return int(raw_input("Which card from your hand do you wish to swap? "))

def request_faceup_swap():
    return int(raw_input("Which card from your face up pile " + 
                         "do you wish to swap? "))
