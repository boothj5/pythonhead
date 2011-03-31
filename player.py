from deck import Hand

class Player:
    """Represents a player"""

    def __init__(self, name):
        self.name = name
        self.hand = Hand('Hand')
        self.faceup = Hand('Face up')
        self.facedown = Hand('Face down')

    def swap(self, h_card, f_card):
        hand_card = self.hand.pop_card_at(h_card)
        face_card = self.faceup.pop_card_at(f_card)
        self.hand.add_card(face_card)
        self.faceup.add_card(hand_card)
        self.hand.sort()

