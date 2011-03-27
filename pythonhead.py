from player import Player
from console import *
from card import Card
from game import Game

def char_to_bool(c):
    return c.upper() == 'Y'

clear_screen()
welcome()

num_players = request_num_players()
num_cards_each = request_num_cards_each()

player_names = []
for i in range(num_players):
    player_name = raw_input("Enter name of player " + str(i+1) +  ": ")
    player_names.extend(player_name)
 
game = Game(num_players, num_cards_each, player_names)
game.deal()

clear_screen()
show_game(game)

raw_input("Press enter")

for player in game.players:
    clear_screen()
    print card_list_to_string("Hand   : ", player.hand)
    print card_list_to_string("faceup : ", player.faceup)
    print
    swap = char_to_bool(raw_input(player.name + " do you want to swap cards?"))

    if swap:
        clear_screen()
        print player.name
        print
        print card_list_to_string("Hand   : ", player.hand)
        print card_list_to_string("faceup : ", player.faceup)
        print
        hCard = int(raw_input("Which card from your hand do you wish to swap? "))
        fCard = int(raw_input("Which card from your face up pile do you wish to swap? "))
        player.swap(hCard-1, fCard-1)

clear_screen()
show_game(game)


