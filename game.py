from deck import Deck
from player import Player
from card import sh_cmp

class Game:

    def __init__(self, num_players, num_cards, player_names):
        self.num_players = num_players
        self.num_cards = num_cards
        self.players = []
        self.deck = Deck(self.num_players * self.num_cards * 3) 
        self.pile = []
        self.burnt = []
        self.turn = 0
        for i in range(num_players):
            player = Player(player_names[i])
            self.players.append(player)

    def deal(self):
        self.deck.shuffle()
        for i in range(self.num_players):
            for j in range(self.num_cards):
                self.players[i].hand.append(self.deck.pop_card())
                self.players[i].faceup.append(self.deck.pop_card())
                self.players[i].facedown.append(self.deck.pop_card())
        for i in range(self.num_players):
            self.players[i].hand.sort(key=sh_cmp)

    def first_move(self):
        player = self._player_with_lowest()
        cards = self._lowest_cards_to_lay(player)
        self.lay_cards(player, cards)
        self.turn = self.players.index(player)
        self._next_turn()
            
    def lay_cards(self, player, cards):
        self.pile.extend(cards)
        player.hand = filter(lambda c : not c in cards, player.hand)
        player.hand.extend(self.deck.pop_cards(len(cards)))
        player.hand.sort(key=sh_cmp)
        
    def _player_with_lowest(self):
        player_lowest = self.players[0]
        for player in self.players:
            if min(player.hand, key=sh_cmp) < min(player_lowest.hand,
                                                  key=sh_cmp):
                player_lowest = player
        return player_lowest       
    
    def _lowest_cards_to_lay(self, player):
        cards = [min(player.hand, key=sh_cmp)]
        cards.extend([c for c in player.hand
                             if c.rank == cards[0].rank
                             and c != cards[0]])
        return cards
    
    def _next_turn(self):
        self.turn = self.turn + 1
        if self.turn == len(self.players):
            self.turn = 0
