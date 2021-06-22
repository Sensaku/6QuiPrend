from card import Card
from Action import *

class Player:

    def __init__(self, name: str):
        self.hand = []
        self.name = name
        self.score = 0

    def get_Hand(self):
        return self.hand

    def set_Hand(self, hand: list):
        self.hand = hand

    def add_Card(self, card: Card):
        """
        Méthode qui permet d'ajouter une carte
        :param card:
        :return:
        """
        if isinstance(card, Card):
            self.hand.append(card)
        else:
            raise NotImplementedError("Mauvaise instance de carte")

    def choose_card(self):
        carte = min(self.hand, key=lambda x: x.value)
        self.hand.remove(carte)
        return PlayerAction(self, carte)



    def __repr__(self):
        return f"Nom: {self.name}\nMain: {self.hand}"