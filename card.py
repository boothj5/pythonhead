class Card:
    """represents a standard playing card."""
        
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    suit_names = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
    rank_names = ['', '', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 
                 'EIGHT', 'NINE', 'TEN', 'JACK', 'QUEEN', 'KING']
         
    def __str__(self):
        return ((Card.rank_names[self.rank]) +  ' of ' + (Card.suit_names[self.suit]))

    def __cmp__(self, other):
        if self.rank > other.rank: return 1
        if self.rank < other.rank: return -1
        return 0  
