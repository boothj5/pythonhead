class Player:
    """Represents a player"""
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.faceup = []
        self.facedown = []