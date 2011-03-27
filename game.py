from random import shuffle

from player import Player
from card import Card
from deck import Deck, Hand

class Game:

    def __init__(self, num_players, num_cards_each, player_names):
        self.num_players = num_players
        self.num_cards_each = num_cards_each
        self.players = []
        self.deck = Deck(self.num_players * self.num_cards_each * 3) 
        self.pile = Hand('Pile')
        self.burnt = Hand('Burnt')
        for i in range(num_players):
            player = Player(player_names[i])
            self.players.append(player)

    def deal(self):
        for i in range(self.num_players):
            for j in range(self.num_cards_each):
                self.players[i].hand.add_card(self.deck.pop_card())
                self.players[i].faceup.add_card(self.deck.pop_card())
                self.players[i].facedown.add_card(self.deck.pop_card())
