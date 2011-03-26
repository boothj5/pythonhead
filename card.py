class Card:
    """represents a card."""
        
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    suit_names = ['CLUBS', 'DIAMONDS', 'HEARTS', 'SPADES']
    rank_names = {2:'TWO', 3:'THREE', 4:'FOUR', 5:'FIVE', 6:'SIX', 7:'SEVEN', 
            8:'EIGHT',9: 'NINE', 10:'TEN', 11:'JACK', 12:'QUEEN', 13:'KING', 14:'ACE'}
         
    def __str__(self):
        return ((Card.rank_names[self.rank]) +  ' of ' + (Card.suit_names[self.suit]))

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


