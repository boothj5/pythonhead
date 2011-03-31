class Card:
    """represents a card."""
        
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    suits = {1: 'CLUBS', 2: 'DIAMONDS', 3:'HEARTS', 4:'SPADES'}
    ranks = {2:'TWO', 3:'THREE', 4:'FOUR', 5:'FIVE', 6:'SIX', 7:'SEVEN', 
            8:'EIGHT',9: 'NINE', 10:'TEN', 11:'JACK', 12:'QUEEN', 13:'KING', 14:'ACE'}
         
    def __str__(self):
        return ((Card.ranks[self.rank]) +  ' of ' + (Card.suits[self.suit]))

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __eq__(self, other):
        return self.rank == other.rank
    
    def __ne__(self, other):
        return self.rank != other.rank
    
    def __gt__(self, other):
        return self.rank > other.rank
    
    def __ge__(self, other):
        return self.rank >= other.rank

def sh_cmp(card1, card2):
        special = [2,7,10]
        if card1.rank in special and card2.rank in special:
            return 0
        elif card1.rank in special and card2.rank not in special:
            return 1
        elif card1.rank not in special and card2.rank in special:
            return -1
        else:
            if card1 > card2:
                return 1
            elif card1 == card2:
                return 0
            else:
                return -1
            