from player import Player
import console
from card import Card, sh_cmp
from game import Game

console.clear_screen()
console.welcome()

num_players = console.request_num_players()
num_cards_each = console.request_num_cards_each()

player_names = []
for i in range(num_players):
    player_name = console.request_player_name(i)
    player_names.append(player_name)

game = Game(num_players, num_cards_each, player_names)
game.deal()

console.clear_screen()
console.show_game(game)

console.wait_user()

for player in game.players:
    console.clear_screen()
    console.show_player_swap(player)
    swap = console.request_swap(player.name)

    while swap:
        console.clear_screen()
        console.show_player_swap(player)
        hCard = console.request_hand_swap() - 1
        fCard = console.request_faceup_swap() - 1
        player.swap(hCard, fCard)
        console.clear_screen()
        console.show_player_swap(player)
        swap = console.request_swap_more()

console.clear_screen()
console.show_game(game)


