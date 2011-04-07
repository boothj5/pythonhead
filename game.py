from deck import Deck
from player import Player
from card import sh_cmp

class Game:

    def __init__(self, num_players, num_cards_each, player_names):
        self.num_players = num_players
        self.num_cards_each = num_cards_each
        self.players = []
        self.deck = Deck(self.num_players * self.num_cards_each * 3) 
        self.pile = []
        self.burnt = []
        self.turn = 0
        
        for i in range(num_players):
            player = Player(player_names[i])
            self.players.append(player)

    def deal(self):
        self.deck.shuffle()
        
        for i in range(self.num_players):
            for j in range(self.num_cards_each):
                self.players[i].hand.append(self.deck.pop_card())
                self.players[i].faceup.append(self.deck.pop_card())
                self.players[i].facedown.append(self.deck.pop_card())

        for i in range(self.num_players):
            self.players[i].hand.sort(key=sh_cmp)

    def first_move(self):
        player_with_lowest = self.players[0]
        
        for player in self.players[1:]:
            if min(player.hand, key=sh_cmp) < min(player_with_lowest.hand, key=sh_cmp):
                player_with_lowest = player
                
        print "Lowest player = " + player_with_lowest.name
    
        cards_to_lay = [min(player_with_lowest.hand, key=sh_cmp)]
        
        cards_to_lay.extend([c for c in player_with_lowest.hand
                             if c.rank == cards_to_lay[0].rank
                             and c != cards_to_lay[0]])
        
        for card in cards_to_lay:
            print str(card)
            
    def _lowest_card_player(self):
        lowest_player = self.players[0]
        
        
        