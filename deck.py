from random import shuffle

from card import Card

class Deck:

    def __init__(self, cards_required):
        self.cards = [Card(x,y) for y in Card.suits for x in Card.ranks]
        while len(self.cards) < cards_required:
            self.cards.extend(self.deck)

    def __len__(self):
        return len(self.cards)

    def shuffle(self):
        shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()
