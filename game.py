from deck import Deck
from player import Player
from card import Card, sh_cmp

class Game:

    def __init__(self, num_players, num_cards, player_names):
        self.num_players = num_players
        self.num_cards = num_cards
        self.players = []
        self.deck = Deck(self.num_players * self.num_cards * 3) 
        self.pile = []
        self.burnt = []
        self.turn = 0
        self.last_move = ""
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
        self.turn = self.players.index(self.lowest_player())
        cards = self.lowest_cards()
        self.lay_cards(cards)
        self.next_turn()
            
    def lay_cards(self, cards):
        self.pile.extend(cards)
        player = self.current_player()
        player.hand = filter(lambda c : c not in cards, player.hand)
        player.hand.extend(self.deck.pop_cards(len(cards)))
        player.hand.sort(key=sh_cmp)
        self.last_move = player.name + " laid: " +  ", ".join(map(str, cards))
        
    def current_player(self):
        return self.players[self.turn]
    
    def valid_move(self, cards):
        if not Game.same_rank(cards):
            return False
        elif Game.can_lay(cards[0], self.pile):
            return True
        else:
            return False

    def can_play(self):
        player = self.current_player()
        if player.has_hand():
            return self.can_play_from_hand()
        elif player.had_faceup():
            return self.can_play_from_faceup()
        else:
            return False
        
    def can_play_from_hand(self):
        player = self.current_player()
        return any(map(lambda c : Game.can_lay(c, self.pile), player.hand))
        
    def can_play_from_faceup(self):
        player = self.current_player()
        return any(map(lambda c : Game.can_lay(c, self.pile), player.faceup))

    def next_turn(self):
        self.turn = self.turn + 1
        if self.turn == len(self.players):
            self.turn = 0

    def lowest_player(self):
        player_lowest = self.players[0]
        for player in self.players:
            if min(player.hand, key=sh_cmp) < min(player_lowest.hand,
                                                  key=sh_cmp):
                player_lowest = player
        return player_lowest       
    
    def get_cards(self, card_indexes):
        player = self.current_player()
        if player.has_hand():
            return map(lambda i : player.hand[i], card_indexes)
        else:
            return map(lambda i : player.faceup[i], card_indexes)

    def lowest_cards(self):
        player = self.current_player()
        cards = [min(player.hand, key=sh_cmp)]
        cards.extend([c for c in player.hand
                             if c.rank == cards[0].rank
                             and c != cards[0]])
        return cards

    @staticmethod
    def same_rank(cards):
        return all(map(lambda c : c.rank == cards[0].rank, cards))

    @staticmethod
    def can_lay(card, pile):
        card_on_pile = pile[len(pile) -1]
        rest_of_pile = pile[0:len(pile) -1]
        if not pile:
            return True
        elif card.rank in Card.lay_on_anything_ranks:
            return True
        elif card_on_pile.rank == Card.invisible:
            return Game.can_lay(card, rest_of_pile)
        elif card.rank >= card_on_pile.rank:
            return True
        else:
            return False
