class Player:
    """Represents a player"""

    def __init__(self, name):
        self.name = name
        self.hand = []
        self.faceup = []
        self.facedown = []

    def add_to_hand(self, cards):
        self.hand.extend(cards)

    def swap(self, h_card, f_card):
        hand_card = self.hand.pop(h_card)
        face_card = self.faceup.pop(f_card)
        self.hand.append(face_card)
        self.faceup.append(hand_card)

