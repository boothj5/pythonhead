from random import shuffle

from card import Card, sh_cmp

class Deck:

    def __init__(self, cards_required):
        self.cards = [Card(x,y) for y in Card.suits for x in Card.ranks]
        while len(self.cards) < cards_required:
            self.cards.extend(self.deck)

    def __len__(self):
        return len(self.cards)

    def shuffleDeck(self):
        shuffle(self.cards)

    def pop_card(self):
        return self.cards.pop()

    def pop_card_at(self, index):
        return self.cards.pop(index)

class Hand(Deck):

    def __init__(self, name):
        self.cards = []
        self.name = name

    def __str__(self):
        result = self.name + ': '
        for card in self.cards:
            result = result + (str(card))
            result = result +  ', '
        return result

    def add_card(self, card):
        self.cards.append(card)
        self.cards.sort()
        
    def sort(self):
        self.cards.sort(sh_cmp)

