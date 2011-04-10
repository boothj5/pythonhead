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
        player = self.__lowest_player()
        cards = self.__lowest_cards(player)
        self.lay_cards(player, cards)
        self.turn = self.players.index(player)
        self.__next_turn()
        self.last_move = player.name + " laid: " +  ", ".join(map(str, cards))
            
    def lay_cards(self, player, cards):
        self.pile.extend(cards)
        player.hand = filter(lambda c : c not in cards, player.hand)
        player.hand.extend(self.deck.pop_cards(len(cards)))
        player.hand.sort(key=sh_cmp)
        
    def current_player(self):
        return self.players[self.turn]
    
    def valid_move(self, card_indexes):
        cards = self.__get_cards(card_indexes)
        if not self.__same_rank(cards):
            return False
        elif self.__can_lay(cards[0], self.pile):
            return True
        else:
            return False

    def can_play(self, player):
        if player.has_hand():
            return self.can_play_from_hand(player)
        elif player.had_faceup():
            return self.can_play_from_faceup(player)
        else:
            return False
        
    def can_play_from_hand(self, player):
        return any(map(lambda c : self.__can_lay(c, self.pile), player.hand))
        
    def can_play_from_faceup(self, player):
        return any(map(lambda c : self.__can_lay(c, self.pile), player.faceup))

    def __next_turn(self):
        self.turn = self.turn + 1
        if self.turn == len(self.players):
            self.turn = 0

    def __lowest_player(self):
        player_lowest = self.players[0]
        for player in self.players:
            if min(player.hand, key=sh_cmp) < min(player_lowest.hand,
                                                  key=sh_cmp):
                player_lowest = player
        return player_lowest       
    
    def __get_cards(self, card_indexes):
        player = self.current_player()
        if player.has_hand():
            return map(lambda i : player.hand[i], card_indexes)
        else:
            return map(lambda i : player.faceup[i], card_indexes)

    @staticmethod
    def __lowest_cards(player):
        cards = [min(player.hand, key=sh_cmp)]
        cards.extend([c for c in player.hand
                             if c.rank == cards[0].rank
                             and c != cards[0]])
        return cards

    @staticmethod
    def __same_rank(cards):
        return all(map(lambda c : c.rank == cards[0].rank, cards))

    @staticmethod
    def __can_lay(card, pile):
        if not pile:
            return True
        elif card.rank in [2,7,10]:
            return True
        elif card.rank == 7:
            return can_lay(card, pile[1:])
        elif card.rank >= pile[0].rank:
            return True
        else:
            return False
