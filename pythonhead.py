from player import Player
from console import *
from card import Card
from game import Game

clear_screen()
welcome()

num_players = request_num_players()
num_cards_each = request_num_cards_each()

player_names = []
for i in range(num_players):
    player_name = request_player_name(i)
    player_names.append(player_name)

game = Game(num_players, num_cards_each, player_names)
game.deal()

clear_screen()
show_game(game)

raw_input("Press enter to continue:")

for player in game.players:
    clear_screen()
    print player.hand
    print player.faceup
    print
    swap = request_swap(player.name)

    if swap:
        clear_screen()
        print player.name
        print
        print player.hand
        print player.faceup
        print
        hCard = int(raw_input("Which card from your hand do you wish to swap? "))
        fCard = int(raw_input("Which card from your face up pile do you wish to swap? "))
        player.swap(hCard-1, fCard-1)

clear_screen()
show_game(game)


