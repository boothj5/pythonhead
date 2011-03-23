class Player:
    """Represents a player"""
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.faceup = []
        self.facedown = []

    def addToHand(self, cards):
        self.hand.extend(cards)

    def swap(self, hCard, fCard):
        handCard = self.hand.pop(hCard)
        faceCard = self.faceup.pop(fCard)
        self.hand.append(faceCard)
        self.faceup.append(handCard)

