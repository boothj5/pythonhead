from player import Player
from console import *
from card import Card
from game import Game

def swap_cards(player):
    clear_screen()
    show_player_swap(player)
    hCard = request_hand_swap()
    fCard = request_faceup_swap()
    player.swap(hCard-1, fCard-1)
    clear_screen()
    show_player_swap(player)
    swap_more = request_swap_more()
    if swap_more:
        swap_cards(player)

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

wait_user()

for player in game.players:
    clear_screen()
    show_player_swap(player)
    swap = request_swap(player.name)

    if swap:
        swap_cards(player)

clear_screen()
show_game(game)


