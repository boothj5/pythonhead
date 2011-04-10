from game import Game
import console as c

game = None

def welcome():
    c.clear_screen()
    c.welcome()

def create_game():
    global game
    num_players = c.request_num_players()
    num_cards_each = c.request_num_cards_each()
    player_names = []
    for i in range(num_players):
        player_name = c.request_player_name(i)
        player_names.append(player_name)
    game = Game(num_players, num_cards_each, player_names)
    game.deal()
    c.clear_screen()
    c.show_game(game)
    c.wait_user()

def swap_cards():
    global game
    for player in game.players:
        c.clear_screen()
        c.show_player_swap(player)
        swap = c.request_swap(player.name)
        while swap:
            c.clear_screen()
            c.show_player_swap(player)
            hCard = c.request_hand_swap() - 1
            fCard = c.request_faceup_swap() - 1
            player.swap(hCard, fCard)
            c.clear_screen()
            c.show_player_swap(player)
            swap = c.request_swap_more()
    c.clear_screen()
    c.show_game(game)

def first_move():
    global game
    game.first_move()
    c.wait_user()
    c.clear_screen()
    c.show_game(game)
    c.line()

def main_game():
    global game
    if game.can_play(game.current_player()):
        make_move()
    else:
        print "Cannot play!!"

def make_move():
    global game
    cards = c.request_move(game.current_player())
    if not game.valid_move(cards):
        print "BAD MOVE"
    else:
        print "MOVE OK"
    

welcome()
create_game()
swap_cards()
first_move()
main_game()

