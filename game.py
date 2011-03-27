from random import shuffle

from player import Player
from card import Card

class Game:

    def __init__(self, num_players, num_cards_each, player_names):
        self.num_players = num_players
        self.num_cards_each = num_cards_each
        self.players = []
        self.deck = []
        self.pile = []
        self.burnt = []
        for i in range(num_players):
            player = Player(player_names[i])
            self.players.append(player)

    def deal(self):
        self.__create_deck()
        for i in range(self.num_players):
            for j in range(self.num_cards_each):
                self.players[i].hand.append(self.deck.pop())
                self.players[i].faceup.append(self.deck.pop())
                self.players[i].facedown.append(self.deck.pop())


    def __create_deck(self):
        self.deck = [Card(x,y) for y in Card.suits for x in Card.ranks]
        cards_needed = self.num_players * self.num_cards_each * 3
        while len(self.deck) < cards_needed:
            self.deck.extend(self.deck)
        shuffle(self.deck)


